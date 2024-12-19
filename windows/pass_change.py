
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PasswordChange(object):
    def setupUi(self, PasswordChange):
        PasswordChange.setObjectName("PasswordChange")
        PasswordChange.resize(325, 138)
        self.centralwidget = QtWidgets.QWidget(PasswordChange)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCurrentPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelCurrentPassword.setGeometry(QtCore.QRect(20, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCurrentPassword.setFont(font)
        self.labelCurrentPassword.setObjectName("labelCurrentPassword")
        self.lineEditCurrentPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCurrentPassword.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEditCurrentPassword.setText("")
        self.lineEditCurrentPassword.setObjectName("lineEditCurrentPassword")
        self.BtnApply = QtWidgets.QPushButton(self.centralwidget)
        self.BtnApply.setGeometry(QtCore.QRect(220, 80, 91, 23))
        self.BtnApply.setObjectName("BtnApply")
        self.lineEditNewPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewPassword.setGeometry(QtCore.QRect(20, 80, 181, 20))
        self.lineEditNewPassword.setText("")
        self.lineEditNewPassword.setObjectName("lineEditNewPassword")
        self.labelNewPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelNewPassword.setGeometry(QtCore.QRect(20, 60, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelNewPassword.setFont(font)
        self.labelNewPassword.setObjectName("labelNewPassword")
        PasswordChange.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PasswordChange)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 21))
        self.menubar.setObjectName("menubar")
        PasswordChange.setMenuBar(self.menubar)

        self.retranslateUi(PasswordChange)
        QtCore.QMetaObject.connectSlotsByName(PasswordChange)

    def retranslateUi(self, PasswordChange):
        _translate = QtCore.QCoreApplication.translate
        PasswordChange.setWindowTitle(_translate("PasswordChange", "Смена пароля"))
        self.labelCurrentPassword.setText(_translate("PasswordChange", "Введите текущий пароль:"))
        self.BtnApply.setText(_translate("PasswordChange", "Применить"))
        self.labelNewPassword.setText(_translate("PasswordChange", "Введите новый пароль:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordChange = QtWidgets.QMainWindow()
    ui = Ui_PasswordChange()
    ui.setupUi(PasswordChange)
    PasswordChange.show()
    sys.exit(app.exec_())
