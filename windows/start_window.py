# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(292, 158)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
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

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Начальное окно"))
        self.BtnManager.setText(_translate("StartWindow", "Менеджер по заказам"))
        self.BtnEngineer.setText(_translate("StartWindow", "Инженер"))
        self.BtnProduction.setText(_translate("StartWindow", "Производство"))
        self.BtnSettings.setText(_translate("StartWindow", "Настройки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())
