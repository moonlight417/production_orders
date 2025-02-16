
from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_PasswordChange(object):
    def setupUi(self, PasswordChange):
        PasswordChange.setObjectName("PasswordChange")
        # PasswordChange.resize(400, 200)

        self.centralwidget = QtWidgets.QWidget(PasswordChange)
        self.centralwidget.setObjectName("centralwidget")

        # Создание сетки для размещения элементов
        self.layout = QtWidgets.QGridLayout(self.centralwidget)

        self.labelRoleChoice = QtWidgets.QLabel(self.centralwidget)
        # self.labelRoleChoice.setGeometry(QtCore.QRect(70, 5, 221, 20))
        # Устанавливаем стиль шрифта через setStyleSheet
        self.labelRoleChoice.setStyleSheet("font-size: 16px;")  # Устанавливаем размер шрифта 20px

        self.labelRoleChoice.setObjectName("labelRoleChoice")

        # Размещаем labelRoleChoice
        self.layout.addWidget(self.labelRoleChoice, 0, 1)

        # Текущий пароль
        self.lineEditCurrentPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCurrentPassword.setFixedHeight(40)
        # self.lineEditCurrentPassword.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEditCurrentPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditCurrentPassword.setObjectName("lineEditCurrentPassword")

        # Устанавливаем текст-заполнитель (placeholder) и его стиль
        self.lineEditCurrentPassword.setPlaceholderText("Введите пароль")
        self.lineEditCurrentPassword.setStyleSheet("""
                            QLineEdit {
                                font-size: 20px;  /* Размер шрифта для текста ввода */
                            }
                            QLineEdit::placeholder {
                                font-size: 20px;  /* Размер шрифта для текста-заполнителя */
                                color: gray;      /* Цвет текста-заполнителя */
                            }
                        """)
        # Размещаем lineEditCurrentPassword
        self.layout.addWidget(self.lineEditCurrentPassword, 1, 0, 1, 2)

        # Новый пароль
        self.lineEditNewPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewPassword.setFixedHeight(40)
        # self.lineEditNewPassword.setGeometry(QtCore.QRect(20, 80, 181, 20))
        self.lineEditNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditNewPassword.setObjectName("lineEditNewPassword")

        # Устанавливаем текст-заполнитель (placeholder) и его стиль
        self.lineEditNewPassword.setPlaceholderText("Введите пароль")
        self.lineEditNewPassword.setStyleSheet("""
                                    QLineEdit {
                                        font-size: 20px;  /* Размер шрифта для текста ввода */
                                    }
                                    QLineEdit::placeholder {
                                        font-size: 20px;  /* Размер шрифта для текста-заполнителя */
                                        color: gray;      /* Цвет текста-заполнителя */
                                    }
                                """)
        # Размещаем lineEditNewPassword
        self.layout.addWidget(self.lineEditNewPassword, 2, 0, 1, 2)

        self.comboBoxRole = QtWidgets.QComboBox(self.centralwidget)
        # self.comboBoxRole.setGeometry(210, 30, 100, 20)
        self.comboBoxRole.addItems(["Менеджер", "Инженер", "Производство"])

        self.comboBoxRole.setStyleSheet("""
                QComboBox {
                font-size: 17px;
                }
                """)

        # Размещаем comboBoxRole
        self.layout.addWidget(self.comboBoxRole, 0, 2)

        # Кнопка "Применить"
        self.BtnApply = QtWidgets.QPushButton(self.centralwidget)
        # self.BtnApply.setGeometry(QtCore.QRect(210, 80, 100, 23))
        self.BtnApply.setObjectName("BtnApply")
        # Размещаем BtnApply
        self.layout.addWidget(self.BtnApply, 2, 2)

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
        self.labelRoleChoice.setText(_translate("PasswordChange", "Выберите вашу роль:"))
        self.BtnApply.setText(_translate("PasswordChange", "Применить"))
        # self.labelNewPassword.setText(_translate("PasswordChange", "Введите новый пароль:"))
        self.lineEditCurrentPassword.setPlaceholderText(_translate("PasswordChange", "Введите текущий пароль"))
        self.lineEditNewPassword.setPlaceholderText(_translate("PasswordChange", "Введите новый пароль"))


class PasswordChange(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PasswordChange()
        self.ui.setupUi(self)

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(400, 230)

        # Подключаем кнопку "Применить" к методу смены пароля
        self.ui.BtnApply.clicked.connect(self.apply_password_change)

    def apply_password_change(self, role):
        current_password = self.ui.lineEditCurrentPassword.text()
        new_password = self.ui.lineEditNewPassword.text()

        # Проверка заполнения полей
        if not current_password or not new_password:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Заполните оба поля!")
            return

        # Запрос на сервер
        try:
            role = self.ui.comboBoxRole.currentText()  # Замените на реальное значение или получите из пользовательского ввода
            response = requests.post(
                "http://127.0.0.1:8000/employees/change_password/",
                json={
                    "role": role,
                    "current_password": current_password,
                    "new_password": new_password,
                },
            )
            print(f"Отправляется запрос: {current_password}, {new_password}")
            print(response.status_code)

            if response.status_code == 200 and response.json().get("success"):
                QtWidgets.QMessageBox.information(self, "Успех", "Пароль успешно изменен!")
                self.close()
            else:
                error_message = response.json().get("message", "Не удалось сменить пароль.")
                QtWidgets.QMessageBox.warning(self, "Ошибка", error_message)
        except requests.RequestException as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к серверу: {e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = PasswordChange()
    window.show()
    sys.exit(app.exec_())

