from re import U
from PySide6 import QtWidgets
import PySide6
from uic.main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QDoubleValidator, QIcon, QPixmap, QImage, QPicture
from PySide6.QtCore import Qt, SIGNAL
import qdarktheme
from resources import MainIcon
import sys, os
import ctypes
import ipaddress
from utils.logger import get_logger as Logging
import utils.utility as utility
import utils.settings as settings
import requests
from utils.kthread import KThread
from time import sleep

logger = Logging("Main")
app = QApplication(sys.argv)


def GetMainWindow():
    global window
    return window


class Configuration(settings.Config):
    def __init__(self) -> None:
        super(Configuration, self).__init__("StepperControl", utility.get_root_directory())
        self.last_ip = self.add_param("LastIP", "None")
        self.timeout = self.add_param("Timeout", 1.0)
        self.speedPct = self.add_param("SpeedPct", 0.2)
        self.accelPct = self.add_param("AccelPct", 0.2)
        self.maxSpeed = self.add_param("MaxSpeedRPM", 500.0)
        self.maxAccel = self.add_param("MaxAccelFactor", 10.0)
        self.desiredPos = self.add_param("DesiredPos", 0.0)
        self.reset_device = False


config = Configuration()


def check_ip_address(ip_str: str) -> object:
    """Checks if IP address is correct."""
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip
    except ValueError:
        return None
    
    
class StepperIface():
    MainURLPrefix = "update"
    DefaultPort = 8888
    
    def __init__(self) -> None:
        self.is_connected = False
        self.conn_state: str = "Disconnected"
        self._pct_open = 0.0
        
        self._run_thread = KThread(name="StepperThread", target=self.thread_func)
        self._run_thread.start()
        self.log = Logging("Stepper")
        
    def connect(self):
        try:
            self.is_connected = False
            url = self._get_url()
            
            data = {}
            # add data like data["SetCurPcnt"] = 1.0
            resp = requests.get(url, data=data, timeout=config.timeout.value)

            if resp.status_code != 200:
                return False, "Bad resp {}".format(str(resp.status_code))
            
            self.is_connected = True
            self.conn_state = "Connected"
        except Exception as e:
            if "timeout" in str(e):
                self.conn_state = "Timeout"
            else:
                self.conn_state = "Error"
            self.is_connected = False
        
    def _get_url(self):
        return "http://{}:{}/{}".format(config.last_ip.value, self.DefaultPort, self.MainURLPrefix)

    def kill(self):
        self._run_thread.kill()
            
    def thread_func(self):
        try:
            while True:
                try:
                    if self.is_connected:
                        data = dict()

                        if config.speedPct.updated:
                            config.speedPct.reset_updated()
                            data["Speed"] = "{:.2f}".format(config.speedPct.value * config.maxSpeed.value)
                            
                        if config.accelPct.updated:
                            config.accelPct.reset_updated()
                            data["Accel"] = "{:.2f}".format(config.accelPct.value * config.maxAccel.value)
                            
                        if config.desiredPos.updated:
                            config.desiredPos.reset_updated()
                            data["TgtPct"] = "{:.2f}".format(config.desiredPos.value * 100.0)
                            
                        if config.reset_device:
                            config.reset_device = False
                            data["Reset"] = "1"        
                            self.is_connected = False
                            self.conn_state = "Reset"
                            GetMainWindow().update_connection_ui()

                        if len(data) < 1:
                            sleep(0.01)
                            continue

                        # add data like data["SetCurPcnt"] = 1.0
                        #print(self._get_url())
                        resp = requests.get(self._get_url() + "?", data=data, timeout=config.timeout.value)

                        if resp.status_code != 200:
                            self.is_connected = False
                            self.conn_state = "Resp code: {}".format(resp.status_code)
                            GetMainWindow().update_connection_ui()
                    else:
                        sleep(0.01)
                except SystemExit:
                    self.log.info("Stop requested")
                    break
                except Exception as e:
                    if "timeout" in str(e):
                        self.conn_state = "Timeout"
                        self.is_connected = False
                        GetMainWindow().update_connection_ui()
                        continue
                    self.log.error("Error in ctrl loop: \n\t> {}".format(str(e)))
        finally:
            self.log.info("Thread stopped")
            

stepper = StepperIface()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("StepperControl - PotatoMeat Labs")
        self.generate_icons()        
        self.actionAbout.setStatusTip("Details about StepperControl")
       
        self.actionQuit.setText("Quit StepperControl")
        self.actionQuit.setStatusTip("Quit application")
        self.actionQuit.setShortcut("Ctrl+Q")
        #self.actionQuit.triggered.connect(self.quit_action)
        self.actionQuit.triggered.connect(self.quit_action)

        self.ipAddress_LineEdit.textChanged[str].connect(self.ip_address_edit_action)
        self.ipAddress_LineEdit.setText(config.last_ip.value)
        
        self.timeout_LineEdit.textChanged[str].connect(self.timeout_edit_action)
        self.timeout_LineEdit.setValidator(QDoubleValidator(0.0, 60.0, 3, self))
        self.timeout_LineEdit.setText(str(config.timeout.value))
        self.timeout_edit_action(str(config.timeout.value))
        
        self.speedPct_Slider.setValue(self.pct_to_slider(config.speedPct.value))
        self.speedPct_Slider.valueChanged[int].connect(self.speed_changed_action)
        
        self.accelPct_Slider.setValue(self.pct_to_slider(config.accelPct.value))
        self.accelPct_Slider.valueChanged[int].connect(self.accel_changed_action)
        
        self.maxAccel_LineEdit.setText(str(config.maxAccel.value))
        self.maxAccel_LineEdit.textChanged[str].connect(self.max_accel_edit_action)
        
        self.maxSpeed_LineEdit.setText(str(config.maxSpeed.value))
        self.maxSpeed_LineEdit.textChanged[str].connect(self.max_speed_edit_action)
        
        self.posPct_Slider.setValue(self.pct_to_slider(config.desiredPos.value))
        self.posPct_Slider.valueChanged[int].connect(self.position_changed_action)

        self.resetButton.clicked.connect(self.reset_button_action)

        self.connectButton.clicked.connect(self._connect_action)        
        self.update_connection_ui()
        self.update_text_boxes()
      
    @staticmethod
    def quit_action():
        sys.exit(0)
        
    @staticmethod
    def slider_to_pct(val: int) -> float:
        return float(val) / 99.0
    
    @staticmethod
    def pct_to_slider(val: float) -> int:
        return int(round(val * 99.0))
    
    @staticmethod
    def reset_button_action():
        config.reset_device = True
    
    @staticmethod
    def max_accel_edit_action(val: str):
        config.maxAccel.set_to(float(val))
    
    @staticmethod
    def max_speed_edit_action(val: str):
        config.maxSpeed.set_to(float(val))
        
    def speed_changed_action(self, val: int):
        config.speedPct.set_to(self.slider_to_pct(val))
        self.update_text_boxes()
       
    def accel_changed_action(self, val: int):
        config.accelPct.set_to(self.slider_to_pct(val))
        self.update_text_boxes()
        
    def position_changed_action(self, val: int):
        config.desiredPos.set_to(self.slider_to_pct(val))
        self.update_text_boxes()
        
    def update_text_boxes(self):
        self.curSpeedPcnt_Label.setText("{}%".format(int(round(config.speedPct.value * 100.0))))
        self.curAccelPct_Label.setText("{}%".format(int(round(config.accelPct.value* 100.0))))
        self.desiredPosPct_Label.setText("{}%".format(int(round(config.desiredPos.value * 100.0))))
        
    def generate_icons(self):
        """Generates icons for window."""
        icon_pixmap = QPixmap.fromImage(QImage.fromData(MainIcon))
        scale_mode = Qt.TransformationMode.SmoothTransformation
        icon48 = icon_pixmap.scaled(48, 48, mode=scale_mode)
        icon256 = icon_pixmap.scaled(256, 256, mode=scale_mode)
        app_icon = QIcon()
        app_icon.addPixmap(icon48)
        app_icon.addPixmap(icon256)
        app.setWindowIcon(app_icon)
        self.setWindowIcon(app_icon)
        self.iconLabel.setPixmap(icon48)
        
        myappid = 'potatomeat.stepper.control.1' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
    def _connect_action(self):
        stepper.connect()
        self.update_connection_ui()

    @staticmethod
    def timeout_edit_action(text: str):
        config.timeout.set_to(float(text))

    def ip_address_edit_action(self, text: str):
        ip = check_ip_address(text)
        if ip is not None:
            config.last_ip.set_to(text)
            self.ipAddress_LineEdit.setStyleSheet("""QLineEdit {
                    color: rgb(244, 244, 244);
                }""")
        else:
            self.ipAddress_LineEdit.setStyleSheet("""QLineEdit {
                    color: rgb(120, 120, 120);
                }""")
            
    def update_connection_ui(self):
        """Updates UI vars for connection state."""
        if stepper.is_connected:
            self.connectionStatus_Label.setText("Connected")
            self.connectionStatus_Label.setStyleSheet("""QLabel {
                    color: rgb(100, 255, 100);
                }""")
        else:
            if len(stepper.conn_state) < 1:
                self.connectionStatus_Label.setText("Disconnected")
            else:
                self.connectionStatus_Label.setText(stepper.conn_state)
            self.connectionStatus_Label.setStyleSheet("""QLabel {
                    color: rgb(255, 100, 100);
                }""")
        
window = MainWindow()

if __name__ == "__main__":
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window.show()    
    logger.info("Application launched.")
    app.exec()
    config.save()
    stepper.kill()


