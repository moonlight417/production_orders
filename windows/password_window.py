import os
import django
import sys

from windows.customizing import CustomizingWindow, Ui_Customizing
from windows.main_engineer_window import MainWindowEngineer
from windows.main_manager_window import MainWindowManager
from windows.main_production_window import MainWindowProduction
from windows.start_window import StartWindow

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'base.settings')  # Замените 'base.settings' на путь к вашему файлу настроек
django.setup()
from PyQt5 import QtCore, QtWidgets, QtGui
import requests
# from employees.auth import authenticate
from pass_change import PasswordChange, Ui_PasswordChange
from PyQt5.QtWidgets import QMessageBox


class Ui_EnterPassword(object):
    def setupUi(self, EnterPassword, change_password_callback):
        EnterPassword.setObjectName("EnterPassword")
        # EnterPassword.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(EnterPassword)

        # Создание сетки для размещения элементов
        self.layout = QtWidgets.QGridLayout(self.centralwidget)

        # Поле для ввода пароля
        self.lineEditEnterPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEnterPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditEnterPassword.setFixedHeight(40)
        self.lineEditEnterPassword.setObjectName("lineEditEnterPassword")

        # Устанавливаем текст-заполнитель (placeholder) и его стиль
        self.lineEditEnterPassword.setPlaceholderText("Введите пароль")
        self.lineEditEnterPassword.setStyleSheet("""
                    QLineEdit {
                        font-size: 20px;  /* Размер шрифта для текста ввода */
                    }
                    QLineEdit::placeholder {
                        font-size: 20px;  /* Размер шрифта для текста-заполнителя */
                        color: gray;      /* Цвет текста-заполнителя */
                    }
                """)

        # Размещаем поле для пароля в первой строке, второй колонке
        self.layout.addWidget(self.lineEditEnterPassword, 0, 0)

        # Кнопка "Войти"
        self.BtnEnter = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEnter.setObjectName("BtnEnter")
        self.BtnEnter.setMinimumWidth(150)
        self.BtnEnter.setMaximumWidth(200)
        self.BtnEnter.setText("Войти")

        # Размещаем кнопку "Войти"
        self.layout.addWidget(self.BtnEnter, 0, 2)

        # Кнопка "Назад"
        self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
        self.BtnBack.setObjectName("BtnBack")

        self.BtnBack.setText("Назад")

        # Размещаем кнопку "Назад"
        self.layout.addWidget(self.BtnBack, 3, 2)

        # Устанавливаем центральный виджет
        EnterPassword.setCentralWidget(self.centralwidget)
        self.retranslateUi(EnterPassword)
        QtCore.QMetaObject.connectSlotsByName(EnterPassword)

        # Меню
        self.menubar = QtWidgets.QMenuBar(EnterPassword)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        EnterPassword.setMenuBar(self.menubar)

        # Создание меню "Правка"
        fileMenu = self.menubar.addMenu("Правка")

        # Создание действия "Сменить пароль"
        changePasswordAction = QtWidgets.QAction("Сменить пароль", EnterPassword)
        changePasswordAction.triggered.connect(change_password_callback)  # Подключаем действие к методу
        fileMenu.addAction(changePasswordAction)

    def retranslateUi(self, EnterPassword):
        _translate = QtCore.QCoreApplication.translate
        self.lineEditEnterPassword.setPlaceholderText(_translate("EnterPassword", "Введите пароль"))

class PasswordWindow(QtWidgets.QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.ui = Ui_EnterPassword()
        self.ui.setupUi(self, self.change_password)  # Передаем метод change_password
        self.role = role
        self.password_change_window = None  # Инициализируем как None

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(400, 200)

        # Подключаем сигналы
        self.ui.BtnEnter.clicked.connect(self.check_password)
        # self.ui.BtnBack.clicked.connect(self.close)
        # self.ui.BtnChangePassword.clicked.connect(self.change_password)

        self.ui.BtnBack.clicked.connect(self.back_role_selection)

        self.ui.lineEditEnterPassword.returnPressed.connect(self.check_password)

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
                f"http://127.0.0.1:8000/employees/check_password/{self.role}/",
                data={"password": entered_password},
            )
            if response.status_code == 200 and response.json().get("success"):
                self.open_role_window(self.role)
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный пароль.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к серверу: {e}")

    def open_role_window(self, role):
        role = role.strip()  # Убираем лишние пробелы
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
            self.admin_window = CustomizingWindow()  # Создаем экземпляр окна для администратора
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



if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = PasswordWindow("Администратор")
        window.show()
        sys.exit(app.exec_())  # Запуск основного цикла
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        sys.exit(1)
