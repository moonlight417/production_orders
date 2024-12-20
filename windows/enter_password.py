from PyQt5 import QtCore, QtWidgets, QtGui
from auth import check_password

class Ui_EnterPassword(object):
    def setupUi(self, EnterPassword):
        EnterPassword.setObjectName("EnterPassword")
        EnterPassword.resize(242, 143)
        self.centralwidget = QtWidgets.QWidget(EnterPassword)

        self.labelEnterPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelEnterPassword.setGeometry(QtCore.QRect(10, 15, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelEnterPassword.setFont(font)
        self.labelEnterPassword.setObjectName("labelEnterPassword")

        self.lineEditEnterPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEnterPassword.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.lineEditEnterPassword.setEchoMode(QtWidgets.QLineEdit.Password)
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
        self.retranslateUi(EnterPassword)
        QtCore.QMetaObject.connectSlotsByName(EnterPassword)

    def retranslateUi(self, EnterPassword):
        _translate = QtCore.QCoreApplication.translate
        EnterPassword.setWindowTitle(_translate("EnterPassword", "Пароль"))
        self.labelEnterPassword.setText(_translate("EnterPassword", "Введите пароль:"))
        self.BtnChangePassword.setText(_translate("EnterPassword", "Смена пароля"))
        self.BtnEnter.setText(_translate("EnterPassword", "Войти"))
        self.BtnBack.setText(_translate("EnterPassword", "Назад"))

    # def check_password(self):
    #     password = self.lineEditEnterPassword.text()
    #     # Проверяем пароль
    #     if password == "engineer":
    #         self.open_engineer()
    #     elif password == "manager":
    #         self.open_manager()
    #     elif password == "prod":
    #         self.open_production()
    #     else:
    #         QtWidgets.QMessageBox.critical(self, "Ошибка", "Неверный пароль")
    #         self.lineEditEnterPassword.clear()