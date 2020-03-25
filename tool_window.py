# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tool_window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionTutorial = QAction(MainWindow)
        self.actionTutorial.setObjectName(u"actionTutorial")
        self.actionStart_RCIS = QAction(MainWindow)
        self.actionStart_RCIS.setObjectName(u"actionStart_RCIS")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ActiveInterfaces = QScrollArea(self.centralwidget)
        self.ActiveInterfaces.setObjectName(u"ActiveInterfaces")
        self.ActiveInterfaces.setGeometry(QRect(539, 59, 261, 491))
        self.ActiveInterfaces.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 259, 489))
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 231, 20))
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 50, 21, 25))
        self.pushButton.setStyleSheet(u"background-color: rgb(204, 0, 0);")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 50, 191, 17))
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 90, 191, 17))
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 90, 21, 25))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(204, 0, 0);")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 130, 191, 17))
        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 130, 21, 25))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(204, 0, 0);")
        self.ActiveInterfaces.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 29, 531, 521))
        self.MonitoringTab = QWidget()
        self.MonitoringTab.setObjectName(u"MonitoringTab")
        self.tabWidget.addTab(self.MonitoringTab, "")
        self.ControllingTab = QWidget()
        self.ControllingTab.setObjectName(u"ControllingTab")
        self.ControllingTab.setEnabled(False)
        self.verticalLayoutWidget = QWidget(self.ControllingTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 100, 431, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.setSpeed = QSpinBox(self.verticalLayoutWidget)
        self.setSpeed.setObjectName(u"setSpeed")
        self.setSpeed.setMinimum(-250)
        self.setSpeed.setMaximum(250)

        self.horizontalLayout.addWidget(self.setSpeed)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.speedSlider = QSlider(self.verticalLayoutWidget)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setMinimum(-250)
        self.speedSlider.setMaximum(250)
        self.speedSlider.setValue(0)
        self.speedSlider.setOrientation(Qt.Horizontal)
        self.speedSlider.setTickPosition(QSlider.TicksBothSides)
        self.speedSlider.setTickInterval(25)

        self.verticalLayout.addWidget(self.speedSlider)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.setAngularSpeed = QDoubleSpinBox(self.verticalLayoutWidget)
        self.setAngularSpeed.setObjectName(u"setAngularSpeed")
        self.setAngularSpeed.setMinimum(-1.500000000000000)
        self.setAngularSpeed.setMaximum(1.500000000000000)
        self.setAngularSpeed.setSingleStep(0.100000000000000)

        self.horizontalLayout_6.addWidget(self.setAngularSpeed)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.AngularSlider = QSlider(self.verticalLayoutWidget)
        self.AngularSlider.setObjectName(u"AngularSlider")
        self.AngularSlider.setMinimum(-15)
        self.AngularSlider.setMaximum(15)
        self.AngularSlider.setSingleStep(1)
        self.AngularSlider.setPageStep(5)
        self.AngularSlider.setValue(0)
        self.AngularSlider.setSliderPosition(0)
        self.AngularSlider.setOrientation(Qt.Horizontal)
        self.AngularSlider.setTickPosition(QSlider.TicksBothSides)
        self.AngularSlider.setTickInterval(10)

        self.verticalLayout.addWidget(self.AngularSlider)

        self.label_8 = QLabel(self.ControllingTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 70, 231, 17))
        self.tabWidget.addTab(self.ControllingTab, "")
        self.ToolsTab = QWidget()
        self.ToolsTab.setObjectName(u"ToolsTab")
        self.stackedWidget = QStackedWidget(self.ToolsTab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 90, 331, 141))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.tabWidget.addTab(self.ToolsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSimulator = QMenu(self.menubar)
        self.menuSimulator.setObjectName(u"menuSimulator")
        self.menuComponents = QMenu(self.menubar)
        self.menuComponents.setObjectName(u"menuComponents")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimulator.menuAction())
        self.menubar.addAction(self.menuComponents.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuSimulator.addAction(self.actionStart_RCIS)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionTutorial)

        self.retranslateUi(MainWindow)
        self.speedSlider.valueChanged.connect(self.setSpeed.setValue)
        self.setSpeed.valueChanged.connect(self.speedSlider.setValue)
        self.actionExit.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionTutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.actionStart_RCIS.setText(QCoreApplication.translate("MainWindow", u"Start RCIS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Active Interface", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Differential Robot", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Laser", None))
        self.pushButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.pushButton_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MonitoringTab), QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Robot Set Speed", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Robot Set Angular Speed", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Setting Properties in Real Time", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ControllingTab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ToolsTab), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSimulator.setTitle(QCoreApplication.translate("MainWindow", u"Simulator", None))
        self.menuComponents.setTitle(QCoreApplication.translate("MainWindow", u"Components", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

