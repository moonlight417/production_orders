import sys
import os
import django
from PyQt5 import QtCore, QtWidgets

# Настраиваем Django окружение
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

# Настройка масштабирования DPI
app = QtWidgets.QApplication(sys.argv)

# Включаем масштабирование для всех экранов
app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

# Применяем стиль ко всем кнопкам в приложении
app.setStyleSheet("""
    QPushButton {
        height: 20px;
        font-family: Arial;
        font-size: 11pt;
        background-color: #f0f0f0;
        border: 1px solid #808a9c;
        color: black;
        border-radius: 4px;
        padding: 8px;
    }
    QPushButton:hover {
        background-color: #dae5f7;
        border: 1px solid #0a66fa;
    }
    QPushButton:pressed {
        background-color: #d0d0d0;
    }
    QLineEdit {
        font-family: Arial;
        font-size: 11pt;
        padding: 5px;
        border: 1px solid #808a9c;
        border-radius: 4px;
        background-color: #ffffff;
        color: #333333;
    }
    QLineEdit:focus {
        border: 1px solid #0a66fa;
        background-color: #f7faff;
    }
    QDateEdit {
        font-family: Arial;
        font-size: 11pt;
        padding: 5px;
        border: 1px solid #808a9c;
        border-radius: 4px;
        background-color: #ffffff;
        color: #333333;
    }
    
    QLabel {
        font-family: Arial;
        font-size: 9pt;
    }
""")

# Создание главного окна приложения
class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(400, 300)

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        StartWindow.setCentralWidget(self.centralwidget)

        # Создаём вертикальный layout для кнопок
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Кнопки
        self.BtnManager = QtWidgets.QPushButton(self.centralwidget)
        self.BtnManager.setObjectName("BtnManager")
        self.layout.addWidget(self.BtnManager)

        self.BtnEngineer = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEngineer.setObjectName("BtnEngineer")
        self.layout.addWidget(self.BtnEngineer)

        self.BtnProduction = QtWidgets.QPushButton(self.centralwidget)
        self.BtnProduction.setObjectName("BtnProduction")
        self.layout.addWidget(self.BtnProduction)

        self.BtnSettings = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSettings.setObjectName("BtnSettings")
        self.layout.addWidget(self.BtnSettings)

        # Меню (по желанию)
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        StartWindow.setMenuBar(self.menubar)

        # Подключаем кнопки
        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Стартовое окно"))
        self.BtnManager.setText(_translate("StartWindow", "Менеджер по заказам"))
        self.BtnEngineer.setText(_translate("StartWindow", "Инженер"))
        self.BtnProduction.setText(_translate("StartWindow", "Производство"))
        self.BtnSettings.setText(_translate("StartWindow", "Настройки"))

class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)

        # Подключаем кнопки к методам
        self.ui.BtnManager.clicked.connect(lambda: self.open_password_window("Менеджер"))
        self.ui.BtnEngineer.clicked.connect(lambda: self.open_password_window("Инженер"))
        self.ui.BtnProduction.clicked.connect(lambda: self.open_password_window("Производство"))
        self.ui.BtnSettings.clicked.connect(lambda: self.open_password_window("Администратор"))

    def open_password_window(self, role):
        from password_window import PasswordWindow  # Импортируем внутри метода для избежания циклического импорта
        self.password_window = PasswordWindow(role)
        self.password_window.show()
        self.close()

if __name__ == "__main__":
    # Создаем экземпляр приложения
    window = StartWindow()  # Создаем главное окно
    window.show()  # Показываем главное окно
    sys.exit(app.exec_())  # Запускаем основной цикл приложения
