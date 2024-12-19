
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterPassword(object):
    def setupUi(self, EnterPassword):
        EnterPassword.setObjectName("EnterPassword")
        EnterPassword.resize(242, 143)
        self.centralwidget = QtWidgets.QWidget(EnterPassword)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEnterPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelEnterPassword.setGeometry(QtCore.QRect(10, 15, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelEnterPassword.setFont(font)
        self.labelEnterPassword.setObjectName("labelEnterPassword")
        self.lineEditEnterPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEnterPassword.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.lineEditEnterPassword.setObjectName("lineEditEnterPassword")
        self.BtnChangePassword = QtWidgets.QPushButton(self.centralwidget)
        self.BtnChangePassword.setGeometry(QtCore.QRect(155, 80, 81, 23))
        self.BtnChangePassword.setObjectName("BtnChangePassword")
        self.BtnEnter = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEnter.setGeometry(QtCore.QRect(180, 40, 51, 23))
        self.BtnEnter.setObjectName("BtnEnter")
        self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
        self.BtnBack.setGeometry(QtCore.QRect(10, 80, 81, 23))
        self.BtnBack.setObjectName("BtnBack")
        EnterPassword.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EnterPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 242, 21))
        self.menubar.setObjectName("menubar")
        EnterPassword.setMenuBar(self.menubar)

        self.retranslateUi(EnterPassword)
        QtCore.QMetaObject.connectSlotsByName(EnterPassword)

    def retranslateUi(self, EnterPassword):
        _translate = QtCore.QCoreApplication.translate
        EnterPassword.setWindowTitle(_translate("EnterPassword", "Пароль"))
        self.labelEnterPassword.setText(_translate("EnterPassword", "Введите пароль:"))
        self.BtnChangePassword.setText(_translate("EnterPassword", "Смена пароля"))
        self.BtnEnter.setText(_translate("EnterPassword", "Войти"))
        self.BtnBack.setText(_translate("EnterPassword", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterPassword = QtWidgets.QMainWindow()
    ui = Ui_EnterPassword()
    ui.setupUi(EnterPassword)
    EnterPassword.show()
    sys.exit(app.exec_())
