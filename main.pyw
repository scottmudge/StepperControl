from PySide6 import QtWidgets
import PySide6
from uic.main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon, QPixmap, QImage, QPicture
from PySide6.QtCore import Qt
import qdarktheme
from resources import MainIcon
import sys, base64, os

app = QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
                        
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("StepperControl - PotatoMeat Labs")
        icon_svg_data = base64.b64decode(MainIcon)
        icon_pixmap = QPixmap.fromImage(QImage.fromData(icon_svg_data))
        icon_pixmap_32 = icon_pixmap.scaled(48, 48, mode=Qt.TransformationMode.SmoothTransformation)
        self.setWindowIcon(QIcon(icon_pixmap))
        self.iconLabel.setPixmap(icon_pixmap_32)
        
        self.actionAbout.setStatusTip("Details about StepperControl")
        
        self.actionQuit.setText("Quit StepperControl")
        self.actionQuit.setStatusTip("Quit application")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(self.quit_action)
        
    def quit_action(self):
        sys.exit(0)

if __name__ == "__main__":
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()
    window.show()    
    app.exec()


