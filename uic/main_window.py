# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(580, 480)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, -1, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.iconLabel = QLabel(self.centralwidget)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setMinimumSize(QSize(40, 40))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.iconLabel.setMargin(4)

        self.horizontalLayout_2.addWidget(self.iconLabel)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 48))
        font = QFont()
        font.setPointSize(24)
        font.setBold(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setIndent(0)

        self.horizontalLayout_2.addWidget(self.titleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.controlTab = QWidget()
        self.controlTab.setObjectName(u"controlTab")
        self.gridLayout_5 = QGridLayout(self.controlTab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 6, 4, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resetButton = QPushButton(self.controlTab)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout.addWidget(self.resetButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.connectionStatus_Label = QLabel(self.controlTab)
        self.connectionStatus_Label.setObjectName(u"connectionStatus_Label")
        self.connectionStatus_Label.setMinimumSize(QSize(120, 0))
        self.connectionStatus_Label.setFrameShape(QFrame.NoFrame)
        self.connectionStatus_Label.setFrameShadow(QFrame.Plain)
        self.connectionStatus_Label.setMidLineWidth(1)
        self.connectionStatus_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.connectionStatus_Label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.connectButton = QPushButton(self.controlTab)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout.addWidget(self.connectButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.controlTab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 8, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.accelPct_Slider = QSlider(self.controlTab)
        self.accelPct_Slider.setObjectName(u"accelPct_Slider")
        self.accelPct_Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.accelPct_Slider)

        self.curAccelPct_Label = QLabel(self.controlTab)
        self.curAccelPct_Label.setObjectName(u"curAccelPct_Label")
        self.curAccelPct_Label.setMinimumSize(QSize(80, 0))
        self.curAccelPct_Label.setStyleSheet(u"QFrame {\n"
"	border: 2px dashed rgb(54, 86, 140);\n"
"	font: 700 11pt \"Consolas\";\n"
"}")
        self.curAccelPct_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.curAccelPct_Label)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 6, 1, 1, 1)

        self.label = QLabel(self.controlTab)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 10, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 10, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.speedPct_Slider = QSlider(self.controlTab)
        self.speedPct_Slider.setObjectName(u"speedPct_Slider")
        self.speedPct_Slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.speedPct_Slider)

        self.curSpeedPcnt_Label = QLabel(self.controlTab)
        self.curSpeedPcnt_Label.setObjectName(u"curSpeedPcnt_Label")
        self.curSpeedPcnt_Label.setMinimumSize(QSize(80, 0))
        self.curSpeedPcnt_Label.setStyleSheet(u"QFrame {\n"
"	border: 2px dashed rgb(54, 86, 140);\n"
"	font: 700 11pt \"Consolas\";\n"
"}")
        self.curSpeedPcnt_Label.setFrameShape(QFrame.Box)
        self.curSpeedPcnt_Label.setLineWidth(2)
        self.curSpeedPcnt_Label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.curSpeedPcnt_Label)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)

        self.label_7 = QLabel(self.controlTab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 9, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.degrees_LineEdit = QLineEdit(self.controlTab)
        self.degrees_LineEdit.setObjectName(u"degrees_LineEdit")
        self.degrees_LineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.degrees_LineEdit)

        self.degrees_Button = QPushButton(self.controlTab)
        self.degrees_Button.setObjectName(u"degrees_Button")

        self.horizontalLayout_6.addWidget(self.degrees_Button)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 9, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.label_5 = QLabel(self.controlTab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 7, 0, 1, 1)

        self.ipAddress_LineEdit = QLineEdit(self.controlTab)
        self.ipAddress_LineEdit.setObjectName(u"ipAddress_LineEdit")

        self.gridLayout_4.addWidget(self.ipAddress_LineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.controlTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.negMicrostep_Button = QPushButton(self.controlTab)
        self.negMicrostep_Button.setObjectName(u"negMicrostep_Button")

        self.horizontalLayout_31.addWidget(self.negMicrostep_Button)

        self.posMicrostep_Button = QPushButton(self.controlTab)
        self.posMicrostep_Button.setObjectName(u"posMicrostep_Button")

        self.horizontalLayout_31.addWidget(self.posMicrostep_Button)

        self.neg_StepButton = QPushButton(self.controlTab)
        self.neg_StepButton.setObjectName(u"neg_StepButton")

        self.horizontalLayout_31.addWidget(self.neg_StepButton)

        self.posStep_Button = QPushButton(self.controlTab)
        self.posStep_Button.setObjectName(u"posStep_Button")

        self.horizontalLayout_31.addWidget(self.posStep_Button)


        self.gridLayout_4.addLayout(self.horizontalLayout_31, 7, 1, 1, 1)

        self.label_61 = QLabel(self.controlTab)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_4.addWidget(self.label_61, 6, 0, 1, 1)

        self.timeout_LineEdit = QLineEdit(self.controlTab)
        self.timeout_LineEdit.setObjectName(u"timeout_LineEdit")
        self.timeout_LineEdit.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.gridLayout_4.addWidget(self.timeout_LineEdit, 2, 1, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.microsteps_LineEdit = QLineEdit(self.controlTab)
        self.microsteps_LineEdit.setObjectName(u"microsteps_LineEdit")
        self.microsteps_LineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.microsteps_LineEdit)

        self.microsteps_Button = QPushButton(self.controlTab)
        self.microsteps_Button.setObjectName(u"microsteps_Button")

        self.horizontalLayout_51.addWidget(self.microsteps_Button)

        self.steps_LineEdit = QLineEdit(self.controlTab)
        self.steps_LineEdit.setObjectName(u"steps_LineEdit")
        self.steps_LineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.steps_LineEdit)

        self.steps_Button = QPushButton(self.controlTab)
        self.steps_Button.setObjectName(u"steps_Button")

        self.horizontalLayout_51.addWidget(self.steps_Button)


        self.gridLayout_4.addLayout(self.horizontalLayout_51, 8, 1, 1, 1)

        self.label_51 = QLabel(self.controlTab)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_4.addWidget(self.label_51, 5, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.controlTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.curDeg_LineEdit = QLineEdit(self.controlTab)
        self.curDeg_LineEdit.setObjectName(u"curDeg_LineEdit")
        self.curDeg_LineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.curDeg_LineEdit.setAlignment(Qt.AlignCenter)
        self.curDeg_LineEdit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.curDeg_LineEdit)

        self.label_10 = QLabel(self.controlTab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.targetDeg_LineEdit = QLineEdit(self.controlTab)
        self.targetDeg_LineEdit.setObjectName(u"targetDeg_LineEdit")
        self.targetDeg_LineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.targetDeg_LineEdit.setAlignment(Qt.AlignCenter)
        self.targetDeg_LineEdit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.targetDeg_LineEdit)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 11, 1, 1, 1)

        self.label_8 = QLabel(self.controlTab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 11, 0, 1, 1)

        self.label_11 = QLabel(self.controlTab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)

        self.syncPeriod_LineEdit = QLineEdit(self.controlTab)
        self.syncPeriod_LineEdit.setObjectName(u"syncPeriod_LineEdit")

        self.gridLayout_4.addWidget(self.syncPeriod_LineEdit, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.controlTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settingsTab.sizePolicy().hasHeightForWidth())
        self.settingsTab.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.settingsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 6, 4, 2)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.settingsTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.maxSpeed_LineEdit = QLineEdit(self.settingsTab)
        self.maxSpeed_LineEdit.setObjectName(u"maxSpeed_LineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.maxSpeed_LineEdit.sizePolicy().hasHeightForWidth())
        self.maxSpeed_LineEdit.setSizePolicy(sizePolicy2)
        self.maxSpeed_LineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.maxSpeed_LineEdit, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.label_3 = QLabel(self.settingsTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.maxAccel_LineEdit = QLineEdit(self.settingsTab)
        self.maxAccel_LineEdit.setObjectName(u"maxAccel_LineEdit")

        self.gridLayout_3.addWidget(self.maxAccel_LineEdit, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.discardSettingsButton = QPushButton(self.settingsTab)
        self.discardSettingsButton.setObjectName(u"discardSettingsButton")
        self.discardSettingsButton.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.discardSettingsButton)

        self.horizontalSpacer_3 = QSpacerItem(8, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.saveSettingsButton = QPushButton(self.settingsTab)
        self.saveSettingsButton.setObjectName(u"saveSettingsButton")
        self.saveSettingsButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.saveSettingsButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.settingsTab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 580, 22))
        self.menuFIle = QMenu(self.menuBar)
        self.menuFIle.setObjectName(u"menuFIle")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuFIle.addAction(self.actionAbout)
        self.menuFIle.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.iconLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"StepperControl", None))
#if QT_CONFIG(statustip)
        self.tabWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.controlTab.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.resetButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Reset motor", None))
#endif // QT_CONFIG(statustip)
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(statustip)
        self.connectionStatus_Label.setStatusTip(QCoreApplication.translate("MainWindow", u"Status of motor", None))
#endif // QT_CONFIG(statustip)
        self.connectionStatus_Label.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
#if QT_CONFIG(statustip)
        self.connectButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Connect to motor at IP address", None))
#endif // QT_CONFIG(statustip)
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Stepping", None))
        self.curAccelPct_Label.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.curSpeedPcnt_Label.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Move (deg)", None))
        self.degrees_LineEdit.setInputMask("")
        self.degrees_LineEdit.setText("")
        self.degrees_Button.setText(QCoreApplication.translate("MainWindow", u"Degrees", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Single Stepping", None))
#if QT_CONFIG(statustip)
        self.ipAddress_LineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"IP address of motor (no port)", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Timeout (s)", None))
        self.negMicrostep_Button.setText(QCoreApplication.translate("MainWindow", u"- \u00b5Step", None))
        self.posMicrostep_Button.setText(QCoreApplication.translate("MainWindow", u"+ \u00b5Step", None))
        self.neg_StepButton.setText(QCoreApplication.translate("MainWindow", u"- Step", None))
        self.posStep_Button.setText(QCoreApplication.translate("MainWindow", u"+ Step", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Acceleration", None))
#if QT_CONFIG(statustip)
        self.timeout_LineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Timeout for connection requests (seconds)", None))
#endif // QT_CONFIG(statustip)
        self.microsteps_Button.setText(QCoreApplication.translate("MainWindow", u"\u00b5Step", None))
        self.steps_Button.setText(QCoreApplication.translate("MainWindow", u"Step", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Current Deg:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Target Deg:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sync Period (s)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.controlTab), QCoreApplication.translate("MainWindow", u"Control", None))
#if QT_CONFIG(statustip)
        self.settingsTab.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max RPMs", None))
#if QT_CONFIG(statustip)
        self.maxSpeed_LineEdit.setStatusTip(QCoreApplication.translate("MainWindow", u"Max speed of motor in RPMs", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Acceleration of motor", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max Accel Factor", None))
#if QT_CONFIG(statustip)
        self.discardSettingsButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Discard saved settings", None))
#endif // QT_CONFIG(statustip)
        self.discardSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Discard", None))
#if QT_CONFIG(statustip)
        self.saveSettingsButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Save modified settings", None))
#endif // QT_CONFIG(statustip)
        self.saveSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
    # retranslateUi

