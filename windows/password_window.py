import os
import django
import sys

from windows.castomizing import CastomizingWindow, Ui_Castomizing
from windows.main_engineer_window import MainWindowEngineer
from windows.main_manager_window import MainWindowManager
from windows.main_production_window import MainWindowProduction
from windows.start_window import StartWindow

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')  # Замените 'base.settings' на путь к вашему файлу настроек
django.setup()
from PyQt5 import QtCore, QtWidgets, QtGui
import requests
from employees.auth import authenticate
from pass_change import PasswordChange, Ui_PasswordChange
from PyQt5.QtWidgets import QMessageBox

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

class PasswordWindow(QtWidgets.QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.ui = Ui_EnterPassword()
        self.ui.setupUi(self)
        self.role = role
        self.password_change_window = None  # Инициализируем как None

        # Подключаем сигналы
        self.ui.BtnEnter.clicked.connect(self.check_password)
        # self.ui.BtnBack.clicked.connect(self.close)
        self.ui.BtnChangePassword.clicked.connect(self.change_password)

        self.ui.BtnBack.clicked.connect(self.back_role_selection)

    def back_role_selection(self):
        try:
            self.role_selection_window = StartWindow()  # Создаем экземпляр окна для выбора роли
            self.role_selection_window.show()  # Показываем окно
            self.close()  # Закрываем текущее окно
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно выбора роли: {e}")

    def check_password(self):
        entered_password = self.ui.lineEditEnterPassword.text()
        try:
            response = requests.post(
                f"http://127.0.0.1:8000/api/check_password/{self.role}/",
                data={"password": entered_password},
            )
            if response.status_code == 200 and response.json().get("success"):

                self.open_role_window(self.role)
                # QMessageBox.information(self, "Успех", f"Добро пожаловать, {self.role}!")
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный пароль.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к серверу: {e}")

    def open_role_window(self, role):
        role = role.strip()  # Убираем лишние пробелы
        # Здесь нужно открыть окно для соответствующей роли.
        if role == "Администратор":
            self.open_admin_window()
        elif role == "Менеджер":
            self.open_manager_window()
        elif role == "Инженер":
            self.open_engineer_window()
        elif role == "Производство":
            self.open_production_window()

    def open_admin_window(self):
        try:
            self.admin_window = CastomizingWindow()  # Создаем экземпляр окна для администратора
            self.admin_window.show()  # Показываем окно
            self.close()  # Закрываем текущее окно
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно администратора: {e}")

    def open_manager_window(self):
        try:
            self.manager_window = MainWindowManager()  # Создаем экземпляр окна для менеджера
            self.manager_window.show()  # Показываем окно
            self.close()  # Закрываем текущее окно
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно менеджера: {e}")

    def open_engineer_window(self):
        try:
            self.engineer_window = MainWindowEngineer()  # Создаем экземпляр окна для инженера
            self.engineer_window.show()  # Показываем окно
            self.close()  # Закрываем текущее окно
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно инженера: {e}")

    def open_production_window(self):
        try:
            self.production_window = MainWindowProduction()  # Создаем экземпляр окна для производства
            self.production_window.show()  # Показываем окно
            self.close()  # Закрываем текущее окно
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно производства: {e}")

    def change_password(self):
        if self.password_change_window is None:  # Проверяем, создано ли окно
            self.password_change_window = PasswordChange()  # Создаем новое окно
        self.password_change_window.show()  # Показываем окно


class PasswordChange(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PasswordChange()
        self.ui.setupUi(self)

        # Подключаем кнопку "Применить" к методу смены пароля
        self.ui.BtnApply.clicked.connect(self.apply_password_change)

    def apply_password_change(self):
        current_password = self.ui.lineEditCurrentPassword.text()
        new_password = self.ui.lineEditNewPassword.text()

        # Логика проверки и смены пароля
        if not current_password or not new_password:
            QMessageBox.warning(self, "Ошибка", "Заполните оба поля!")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/change_password/",
                data={"current_password": current_password, "new_password": new_password},
            )
            if response.status_code == 200 and response.json().get("success"):
                QMessageBox.information(self, "Успех", "Пароль успешно изменен!")
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось сменить пароль.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к серверу: {e}")


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = PasswordWindow("Администратор")
        window.show()
        sys.exit(app.exec_())  # Запуск основного цикла
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        sys.exit(1)