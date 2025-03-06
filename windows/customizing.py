from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from task_filling import TaskFilling
from tasks_list import TasksList
from search_design_document import SearchDesignDoc

from new_tasks import NewTasks
from customizing_materials import Materials
from customizing_forms import Forms
from customizing_employees import Employees
from customizing_passwords import Passwords

class Ui_Customizing(object):
    def setupUi(self, Customizing):
        Customizing.setObjectName("Customizing")
        Customizing.resize(1200, 700)

        self.centralwidget = QtWidgets.QWidget(Customizing)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # Верхняя панель с кнопками (левая и правая части)
        self.top_panel = QHBoxLayout()

        # Левая часть верхней панели (основные кнопки)
        self.left_top_panel = QHBoxLayout()
        self.BtnMaterials = QtWidgets.QPushButton("Материалы")
        self.BtnForm = QtWidgets.QPushButton("Формы")
        self.BtnEmployees = QtWidgets.QPushButton("Сотрудники")
        self.BtnPasswords = QtWidgets.QPushButton("Пароли")

        self.bottom_panel = QHBoxLayout()
        self.BtnRoleSelection = QPushButton("К выбору роли")

        self.left_top_panel.addWidget(self.BtnMaterials)
        self.left_top_panel.addWidget(self.BtnForm)
        self.left_top_panel.addWidget(self.BtnEmployees)
        self.left_top_panel.addWidget(self.BtnPasswords)

        # Добавляем левую и правую части в верхнюю панель
        self.top_panel.addLayout(self.left_top_panel)
        self.top_panel.addStretch()  # Отступ между левой и правой частью
        # self.top_panel.addLayout(self.right_top_panel)
        self.top_panel.addWidget(self.BtnRoleSelection)

        # Стек для переключаемых окон
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)



        # Добавляем все элементы в главный layout
        self.main_layout.addLayout(self.top_panel)
        self.main_layout.addWidget(self.stacked_widget)
        # self.main_layout.addLayout(self.bottom_panel)

        Customizing.setCentralWidget(self.centralwidget)
        self.retranslateUi(Customizing)

    def retranslateUi(self, Customizing):
        _translate = QtCore.QCoreApplication.translate
        Customizing.setWindowTitle(_translate("Customizing", "Настройки"))


class Customizing(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Customizing()
        self.ui.setupUi(self)

        # Подключение кнопок к методам
        self.ui.BtnPasswords.clicked.connect(lambda: self.switch_window(self.passwords_window))
        self.ui.BtnMaterials.clicked.connect(lambda: self.switch_window(self.materials_window))
        self.ui.BtnRoleSelection.clicked.connect(self.back_role_selection)
        self.ui.BtnEmployees.clicked.connect(lambda: self.switch_window(self.employees_window))
        self.ui.BtnForm.clicked.connect(lambda: self.switch_window(self.form_window))

        # Создание экземпляров окон
        self.empty_window = QWidget()
        self.passwords_window = Passwords()
        self.materials_window = Materials()
        self.employees_window = Employees()
        self.form_window = Forms()

        # Добавление окон в QStackedWidget
        self.ui.stacked_widget.addWidget(self.empty_window)
        self.ui.stacked_widget.addWidget(self.passwords_window)
        self.ui.stacked_widget.addWidget(self.materials_window)
        self.ui.stacked_widget.addWidget(self.employees_window)
        self.ui.stacked_widget.addWidget(self.form_window)

        # Устанавливаем пустое окно как текущее
        self.ui.stacked_widget.setCurrentWidget(self.empty_window)


    def switch_window(self, window):
        """Переключение на указанное окно"""
        self.ui.stacked_widget.setCurrentWidget(window)


    def back_role_selection(self):
        """Переход к окну выбора роли"""
        try:
            from windows.start_window import StartWindow
            self.role_selection_window = StartWindow()
            self.role_selection_window.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно выбора роли: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Customizing()
    window.show()
    sys.exit(app.exec_())