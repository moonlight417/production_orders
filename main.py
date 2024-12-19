import sys
from PyQt5 import QtWidgets
from auth import check_password
from windows.start_window import Ui_StartWindow
from windows.enter_password import Ui_EnterPassword
from windows.customizing import Ui_Customizing


class MainApp:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.current_window = None

    def show_start_window(self):
        self.close_current_window()
        self.current_window = QtWidgets.QMainWindow()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self.current_window)

        # Подключаем кнопки перехода
        self.ui.BtnManager.clicked.connect(self.show_enter_password_window)
        self.ui.BtnEngineer.clicked.connect(self.show_enter_password_window)
        self.ui.BtnProduction.clicked.connect(self.show_enter_password_window)
        self.ui.BtnSettings.clicked.connect(self.show_customizing_window)

        # Подключаем кнопку "Настройки"
        self.ui.BtnSettings.clicked.connect(self.show_start_window)

        self.current_window.show()

    def show_enter_password_window(self):
        self.close_current_window()
        self.current_window = QtWidgets.QMainWindow()
        self.ui = Ui_EnterPassword()
        self.ui.setupUi(self.current_window)

        # Подключаем кнопку "Назад"
        self.ui.BtnBack.clicked.connect(self.show_start_window)

        # entered_password = self.lineEditEnterPassword.text()
        # if check_password(entered_password, "инженер"):
        #     pass
        # if check_password(entered_password, "менеджер"):
        #     pass
        # if check_password(entered_password, "производство"):
        #     pass

        self.current_window.show()


    def show_customizing_window(self):
        self.close_current_window()
        self.current_window = QtWidgets.QMainWindow()
        self.ui = Ui_Customizing()
        self.ui.setupUi(self.current_window)

        # Подключаем кнопку "Назад"
        self.ui.BtnBack.clicked.connect(self.show_start_window)

        self.current_window.show()

    def close_current_window(self):
        if self.current_window:
            self.current_window.close()

    def run(self):
        self.show_start_window()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = MainApp()
    app.run()