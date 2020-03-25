#!/usr/bin/python3
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, QTimer
from tool_window import Ui_MainWindow
from gen import *
from multiprocessing import Process

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.setSpeed.valueChanged.connect(self.setSpeedMethod)
        self.ui.setAngularSpeed.valueChanged.connect(self.setAngularSpeedMethod)
        self.ui.AngularSlider.valueChanged.connect(self.AngularSliderHandler)
        self.ui.actionStart_RCIS.triggered.connect(self.startSimulator)
        timer = QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.compute)
        timer.start()

        self.basePrx = Ice.initialize(sys.argv).stringToProxy("differentialrobot:tcp -h localhost -p 10004")
        self.differentialrobot_proxy = DifferentialRobotPrx.uncheckedCast(self.basePrx)


    def compute(self):
        try:
            # self.basePrx.ice_ping()
            self.differentialrobot_proxy.ice_ping()
            print("connected")
            #change indicator to green
            self.ui.pushButton.setStyleSheet(u"background-color: rgb(0, 204, 0);")
            self.ui.ControllingTab.setEnabled(True)
            # self.differentialrobot_proxy.setSpeedBase(100, 0)
        except Ice.Exception as e:
            print("not connected")
            # change indicator to red
            self.ui.pushButton.setStyleSheet(u"background-color: rgb(204, 0, 0);")
            self.ui.ControllingTab.setEnabled(False)
    def setSpeedMethod(self,value):
        self.differentialrobot_proxy.setSpeedBase(value, self.ui.setAngularSpeed.value())

    def AngularSliderHandler(self, intValue):
        self.ui.setAngularSpeed.setValue(intValue/10)

    def setAngularSpeedMethod(self, value):
        self.differentialrobot_proxy.setSpeedBase(self.ui.setSpeed.value(), value)

    def startSimulator(self):
        print("start")
        self.rcisthread = Process(target=lambda: os.popen("rcis ~/robocomp/files/innermodel/simpleworld.xml"))
        self.rcisthread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
