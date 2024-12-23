from PyQt5 import QtCore, QtWidgets


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(292, 158)
        self.centralwidget = QtWidgets.QWidget(StartWindow)

        self.BtnManager = QtWidgets.QPushButton(self.centralwidget)
        self.BtnManager.setGeometry(QtCore.QRect(20, 20, 141, 23))
        self.BtnManager.setObjectName("BtnManager")

        self.BtnEngineer = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEngineer.setGeometry(QtCore.QRect(20, 60, 141, 23))
        self.BtnEngineer.setObjectName("BtnEngineer")

        self.BtnProduction = QtWidgets.QPushButton(self.centralwidget)
        self.BtnProduction.setGeometry(QtCore.QRect(20, 100, 141, 23))
        self.BtnProduction.setObjectName("BtnProduction")

        self.BtnSettings = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSettings.setGeometry(QtCore.QRect(195, 100, 75, 23))
        self.BtnSettings.setObjectName("BtnSettings")

        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))
        self.menubar.setObjectName("menubar")
        StartWindow.setMenuBar(self.menubar)

        StartWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Начальное окно"))
        self.BtnManager.setText(_translate("StartWindow", "Менеджер по заказам"))
        self.BtnEngineer.setText(_translate("StartWindow", "Инженер"))
        self.BtnProduction.setText(_translate("StartWindow", "Производство"))
        self.BtnSettings.setText(_translate("StartWindow", "Настройки"))