from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QStackedWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from task_filling import TaskFilling
from tasks_list import TasksList
from search_design_document import SearchDesignDoc
from windows.design_document_filling_form import DesignDocumentFillingForm
from new_tasks import NewTasks
from windows.new_orders import NewOrders
from orders_archive import OrdersArchive

class Ui_MainWindowProduction(object):
    def setupUi(self, MainWindowProduction):
        MainWindowProduction.setObjectName("MainWindowProduction")
        MainWindowProduction.resize(1200, 700)

        self.centralwidget = QtWidgets.QWidget(MainWindowProduction)
        self.main_layout = QVBoxLayout(self.centralwidget)

        # Верхняя панель с кнопками (левая и правая части)
        self.top_panel = QHBoxLayout()

        # Левая часть верхней панели (основные кнопки)
        self.left_top_panel = QHBoxLayout()
        # self.BtnViewTasks = QtWidgets.QPushButton("Задания")
        self.BtnOrderBase = QtWidgets.QPushButton("База заказов")
        self.BtnDrowingArchive = QtWidgets.QPushButton("Архив КД")
        # self.BtnAddNewDesignDoc = QtWidgets.QPushButton("Новый КД")

        # self.left_top_panel.addWidget(self.BtnViewTasks)
        self.left_top_panel.addWidget(self.BtnOrderBase)
        self.left_top_panel.addWidget(self.BtnDrowingArchive)
        # self.left_top_panel.addWidget(self.BtnAddNewDesignDoc)


        # Правая часть верхней панели (лейбл и кнопка проверки)
        self.right_top_panel = QHBoxLayout()
        self.LbCheckOrders = QLabel()  # Лейбл с числом заказов
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.LbCheckOrders.setFont(font)
        self.LbCheckOrders.setAlignment(QtCore.Qt.AlignCenter)
        self.BtnCheckOrders = QPushButton("Открыть")
        self.BtnRefresh = QPushButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/utils/icons/refresh.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.BtnRefresh.setIcon(icon)

        self.right_top_panel.addWidget(self.LbCheckOrders)
        self.right_top_panel.addWidget(self.BtnRefresh)
        self.right_top_panel.addWidget(self.BtnCheckOrders)

        # Добавляем левую и правую части в верхнюю панель
        self.top_panel.addLayout(self.left_top_panel)
        self.top_panel.addStretch()  # Отступ между левой и правой частью
        self.top_panel.addLayout(self.right_top_panel)

        # Стек для переключаемых окон
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Нижняя панель с кнопкой "Назад"
        self.bottom_panel = QHBoxLayout()
        self.BtnRoleSelection = QPushButton("К выбору роли")
        self.bottom_panel.addStretch()  # Добавляем отступ, чтобы кнопка была справа
        self.bottom_panel.addWidget(self.BtnRoleSelection)

        # Добавляем все элементы в главный layout
        self.main_layout.addLayout(self.top_panel)
        self.main_layout.addWidget(self.stacked_widget)
        self.main_layout.addLayout(self.bottom_panel)

        MainWindowProduction.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindowProduction)

    def retranslateUi(self, MainWindowEngineer):
        _translate = QtCore.QCoreApplication.translate
        MainWindowEngineer.setWindowTitle(_translate("MainWindowProduction", "Главное окно производства"))


class MainWindowProduction(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowProduction()
        self.ui.setupUi(self)

        # Подключение кнопок к методам
        # self.ui.BtnAddNewDesignDoc.clicked.connect(lambda: self.switch_window(self.design_document_filling_window))
        # self.ui.BtnViewTasks.clicked.connect(lambda: self.switch_window(self.tasks_list_window))
        self.ui.BtnRoleSelection.clicked.connect(self.back_role_selection)
        self.ui.BtnDrowingArchive.clicked.connect(lambda: self.switch_window(self.search_design_doc_window))
        self.ui.BtnCheckOrders.clicked.connect(lambda: self.switch_window(self.new_orders_list_window))
        self.ui.BtnOrderBase.clicked.connect(lambda: self.switch_window(self.view_orders_window))

        self.new_orders = 1  # Начальное значение числа заказов
        self.update_order_count_label()
        self.ui.BtnCheckOrders.setEnabled(self.new_orders != 0)  # Включение/отключение кнопки

        # Создание экземпляров окон
        self.empty_window = QWidget()
        self.design_document_filling_window = DesignDocumentFillingForm(parent=None)
        self.tasks_list_window = TasksList()
        self.search_design_doc_window = SearchDesignDoc(parent=None)
        self.new_orders_list_window = NewOrders(parent=None)
        self.view_orders_window = OrdersArchive()

        self.check_orders_window = self.create_check_orders()
        # self.view_orders_window = self.create_view_orders_window()
        self.open_new_tasks = self.create_open_new_orders()

        # Добавление окон в QStackedWidget
        self.ui.stacked_widget.addWidget(self.empty_window)
        self.ui.stacked_widget.addWidget(self.design_document_filling_window)
        self.ui.stacked_widget.addWidget(self.tasks_list_window)
        self.ui.stacked_widget.addWidget(self.search_design_doc_window)
        self.ui.stacked_widget.addWidget(self.check_orders_window)
        self.ui.stacked_widget.addWidget(self.view_orders_window)
        self.ui.stacked_widget.addWidget(self.new_orders_list_window)

        # Устанавливаем пустое окно как текущее
        self.ui.stacked_widget.setCurrentWidget(self.empty_window)


    def switch_window(self, window):
        """Переключение на указанное окно"""
        self.ui.stacked_widget.setCurrentWidget(window)


    # def design_document_filling_window(self):
    #     """Создание окна 'Новый КД'"""
    #     window = QWidget()
    #     layout = QVBoxLayout(window)
    #     label = QLabel("Окно: Новый КД")
    #     layout.addWidget(label)
    #     return window

    def create_tasks_list_window(self):
        """Создание окна 'Список заданий'"""
        window = QWidget()
        layout = QVBoxLayout(window)
        label = QLabel("Окно: Список заданий")
        layout.addWidget(label)
        return window

    def create_view_orders_window(self):
        """Создание окна 'Список заданий'"""
        window = QWidget()
        layout = QVBoxLayout(window)
        label = QLabel("Окно: Заказы")
        layout.addWidget(label)
        return window

    def create_search_design_doc_window(self):
        """Создание окна 'Архив КД'"""
        window = QWidget()
        layout = QVBoxLayout(window)
        label = QLabel("Окно: Архив КД")
        layout.addWidget(label)
        return window

    def create_check_orders(self):
        window = QWidget()
        layout = QVBoxLayout(window)
        label = QLabel("Окно: Проверка заказов")
        layout.addWidget(label)
        return window

    def create_open_new_orders(self):
        """Создание окна 'Новое задание'"""
        window = QWidget()
        layout = QVBoxLayout(window)
        label = QLabel("Окно: Новое задание")
        layout.addWidget(label)
        return window


    def update_order_count_label(self):
        """Обновление текста лейбла с числом заказов"""
        self.ui.LbCheckOrders.setText(str(f"Новых заказов: {self.new_orders} "))

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
    window = MainWindowProduction()
    window.show()
    sys.exit(app.exec_())
