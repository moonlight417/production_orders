from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
import sqlite3
import requests

class Ui_TasksList(object):
    def setupUi(self, TasksList):


         TasksList.setObjectName("TasksList")
         TasksList.resize(1132, 798)
         self.centralwidget = QtWidgets.QWidget(TasksList)
         self.centralwidget.setObjectName("centralwidget")

         self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
         self.scrollArea.setGeometry(QtCore.QRect(10, 110, 1111, 601))
         self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
         self.scrollArea.setWidgetResizable(True)
         self.scrollArea.setObjectName("scrollArea")
         self.scrollAreaWidgetContents = QtWidgets.QWidget()
         self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
         self.layoutTask = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
         self.layoutTask.setContentsMargins(5, 5, 5, 5)
         self.layoutTask.setSpacing(5)
         self.scrollAreaWidgetContents.setLayout(self.layoutTask)
         self.scrollArea.setWidget(self.scrollAreaWidgetContents)

         self.lineEditSearchCustomer = QtWidgets.QLineEdit(self.centralwidget)
         self.lineEditSearchCustomer.setGeometry(QtCore.QRect(20, 29, 321, 31))
         self.lineEditSearchCustomer.setObjectName("lineEditSearchCustomer")

         self.BtnSearchCustomer = QtWidgets.QPushButton(self.centralwidget)
         self.BtnSearchCustomer.setGeometry(QtCore.QRect(350, 30, 31, 31))
         icon = QtGui.QIcon()
         icon.addPixmap(QtGui.QPixmap("../utils/icons/search.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         self.BtnSearchCustomer.setIcon(icon)
         self.BtnSearchCustomer.setObjectName("BtnSearchCustomer")

         # TasksList.setCentralWidget(self.centralwidget)
         #
         # self.retranslateUi(TasksList)
         # QtCore.QMetaObject.connectSlotsByName(TasksList)

         self.frame_3 = QtWidgets.QFrame(self.centralwidget)
         self.frame_3.setGeometry(QtCore.QRect(10, 65, 1111, 41))
         self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
         self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
         self.frame_3.setObjectName("frame_3")

         self.labelProductName = QtWidgets.QLabel(self.frame_3)
         self.labelProductName.setGeometry(QtCore.QRect(660, 15, 200, 16))
         self.labelProductName.setObjectName("labelProductName")

         self.labelCheckNumber = QtWidgets.QLabel(self.frame_3)
         self.labelCheckNumber.setGeometry(QtCore.QRect(10, 15, 51, 16))
         self.labelCheckNumber.setObjectName("labelCheckNumber")

         self.labelDate = QtWidgets.QLabel(self.frame_3)
         self.labelDate.setGeometry(QtCore.QRect(95, 15, 31, 16))
         self.labelDate.setObjectName("labelDate")

         self.labelCustomer = QtWidgets.QLabel(self.frame_3)
         self.labelCustomer.setGeometry(QtCore.QRect(240, 15, 171, 16))
         self.labelCustomer.setObjectName("labelCustomer")

         # self.BtnSortNumericUp = QtWidgets.QPushButton(self.frame_3)
         # self.BtnSortNumericUp.setGeometry(QtCore.QRect(35, 20, 21, 20))
         # self.BtnSortNumericUp.setText("")
         # icon = QtGui.QIcon()
         # icon.addPixmap(QtGui.QPixmap("../utils/icons/sort-numeric-down-alt.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         # self.BtnSortNumericUp.setIcon(icon)
         # self.BtnSortNumericUp.setObjectName("BtnSortNumericUp")

         # self.BtnSortNumericDown = QtWidgets.QPushButton(self.frame_3)
         # self.BtnSortNumericDown.setGeometry(QtCore.QRect(10, 20, 21, 20))
         # self.BtnSortNumericDown.setText("")
         # icon1 = QtGui.QIcon()
         # icon1.addPixmap(QtGui.QPixmap("../utils/icons/sort-numeric-down.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         # self.BtnSortNumericDown.setIcon(icon1)
         # self.BtnSortNumericDown.setObjectName("BtnSortNumericDown")

         # self.BtnSortDown = QtWidgets.QPushButton(self.frame_3)
         # self.BtnSortDown.setGeometry(QtCore.QRect(85, 20, 21, 20))
         # self.BtnSortDown.setText("")
         # icon2 = QtGui.QIcon()
         # icon2.addPixmap(QtGui.QPixmap("../utils/icons/sort-down.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         # self.BtnSortDown.setIcon(icon2)
         # self.BtnSortDown.setObjectName("BtnSortDown")

         # self.BtnSortUp = QtWidgets.QPushButton(self.frame_3)
         # self.BtnSortUp.setGeometry(QtCore.QRect(110, 20, 21, 20))
         # self.BtnSortUp.setText("")
         # icon3 = QtGui.QIcon()
         # icon3.addPixmap(QtGui.QPixmap("../utils/icons/sort-down-alt.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         # self.BtnSortUp.setIcon(icon3)
         # self.BtnSortUp.setObjectName("BtnSortUp")

         self.line_5 = QtWidgets.QFrame(self.frame_3)
         self.line_5.setGeometry(QtCore.QRect(50, 8, 20, 31))
         self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
         self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
         self.line_5.setObjectName("line_5")

         self.line_6 = QtWidgets.QFrame(self.frame_3)
         self.line_6.setGeometry(QtCore.QRect(160, 10, 20, 31))
         self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
         self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
         self.line_6.setObjectName("line_6")

         self.line_7 = QtWidgets.QFrame(self.frame_3)
         self.line_7.setGeometry(QtCore.QRect(480, 10, 20, 31))
         self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
         self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
         self.line_7.setObjectName("line_7")

         self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
         self.frame_4.setGeometry(QtCore.QRect(10, 10, 1071, 51))
         self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
         self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
         self.frame_4.setObjectName("frame_4")

         # self.frameLineTask = QtWidgets.QFrame(self.frame_4)
         # self.frameLineTask.setGeometry(QtCore.QRect(0, 0, 1071, 41))
         # self.frameLineTask.setStyleSheet("background-color: rgb(255, 255, 255);\n"
         #                                 "border-color: rgb(0, 0, 0);")
         # self.frameLineTask.setFrameShape(QtWidgets.QFrame.StyledPanel)
         # self.frameLineTask.setFrameShadow(QtWidgets.QFrame.Sunken)
         # self.frameLineTask.setLineWidth(2)
         # self.frameLineTask.setMidLineWidth(1)
         # self.frameLineTask.setObjectName("frameLineTask")
         #
         # self.line = QtWidgets.QFrame(self.frameLineTask)
         # self.line.setGeometry(QtCore.QRect(40, 1, 18, 39))
         # self.line.setFrameShape(QtWidgets.QFrame.VLine)
         # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
         # self.line.setObjectName("line")
         #
         # self.line_2 = QtWidgets.QFrame(self.frameLineTask)
         # self.line_2.setGeometry(QtCore.QRect(150, 1, 18, 39))
         # self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
         # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
         # self.line_2.setObjectName("line_2")

         # self.LbCheckNumber = QtWidgets.QLabel(self.frameLineTask)
         # self.LbCheckNumber.setGeometry(QtCore.QRect(10, 10, 31, 21))
         # font = QtGui.QFont()
         # font.setPointSize(12)
         # self.LbCheckNumber.setFont(font)
         # self.LbCheckNumber.setObjectName("LbCheckNumber")
         #
         # self.LbCustomer = QtWidgets.QLabel(self.frameLineTask)
         # self.LbCustomer.setGeometry(QtCore.QRect(170, 10, 301, 21))
         # font = QtGui.QFont()
         # font.setPointSize(12)
         # font.setBold(False)
         # font.setWeight(50)
         # self.LbCustomer.setFont(font)
         # self.LbCustomer.setObjectName("LbCustomer")
         #
         # self.LbDate = QtWidgets.QLabel(self.frameLineTask)
         # self.LbDate.setGeometry(QtCore.QRect(60, 10, 81, 21))
         # font = QtGui.QFont()
         # font.setPointSize(12)
         # font.setBold(False)
         # font.setWeight(50)
         # self.LbDate.setFont(font)
         # self.LbDate.setObjectName("LbDate")
         #
         # self.comboBoxProductName = QtWidgets.QComboBox(self.frameLineTask)
         # self.comboBoxProductName.setGeometry(QtCore.QRect(480, 0, 543, 41))
         # font = QtGui.QFont()
         # font.setPointSize(12)
         # self.comboBoxProductName.setFont(font)
         # self.comboBoxProductName.setStyleSheet("background-color: rgb(240, 240, 240);")
         # self.comboBoxProductName.setModelColumn(8)
         # self.comboBoxProductName.setObjectName("comboBoxProductName")
         #
         # self.BtnEditTask = QtWidgets.QPushButton(self.frame_4)
         # self.BtnEditTask.setGeometry(QtCore.QRect(1030, 5, 31, 31))
         # self.BtnEditTask.setText("")
         # icon4 = QtGui.QIcon()
         # icon4.addPixmap(QtGui.QPixmap("../utils/icons/pencil-square.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         # self.BtnEditTask.setIcon(icon4)
         # self.BtnEditTask.setIconSize(QtCore.QSize(23, 23))
         # self.BtnEditTask.setObjectName("BtnEditTask")

         # self.scrollArea.setWidget(self.scrollAreaWidgetContents)



         self.BtnSearchCustomer = QtWidgets.QPushButton(self.centralwidget)
         self.BtnSearchCustomer.setGeometry(QtCore.QRect(350, 30, 31, 31))
         self.BtnSearchCustomer.setText("")
         icon5 = QtGui.QIcon()
         icon5.addPixmap(QtGui.QPixmap("../utils/icons/search.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
         self.BtnSearchCustomer.setIcon(icon5)
         self.BtnSearchCustomer.setObjectName("BtnSearchCustomer")

         self.lineEditSearchCustomer = QtWidgets.QLineEdit(self.centralwidget)
         self.lineEditSearchCustomer.setGeometry(QtCore.QRect(20, 29, 321, 31))
         self.lineEditSearchCustomer.setObjectName("lineEditSearchCustomer")

         self.current_date = datetime.now()
         self.last_year_date = self.current_date.replace(year=self.current_date.year - 1)
         self.last_year_qdate = QDate(self.last_year_date.year, self.last_year_date.month, self.last_year_date.day)
         self.dateEditStartPeriod = QtWidgets.QDateEdit(self.centralwidget)
         self.dateEditStartPeriod.setGeometry(QtCore.QRect(885, 37, 81, 22))
         self.dateEditStartPeriod.setCalendarPopup(True)
         self.dateEditStartPeriod.setDate(QDate(self.last_year_qdate))
         self.dateEditStartPeriod.setObjectName("dateEditStartPeriod")

         self.dateEditEndPeriod = QtWidgets.QDateEdit(self.centralwidget)
         self.dateEditEndPeriod.setGeometry(QtCore.QRect(995, 37, 81, 22))
         self.dateEditEndPeriod.setCalendarPopup(True)
         self.dateEditEndPeriod.setDate(QDate.currentDate())
         self.dateEditEndPeriod.setObjectName("dateEditEndPeriod")

         self.label_7 = QtWidgets.QLabel(self.centralwidget)
         self.label_7.setGeometry(QtCore.QRect(975, 40, 16, 16))
         self.label_7.setObjectName("label_7")

         self.checkBoxPeriodOn = QtWidgets.QCheckBox(self.centralwidget)
         self.checkBoxPeriodOn.setGeometry(QtCore.QRect(800, 40, 81, 17))
         self.checkBoxPeriodOn.setObjectName("checkBoxPeriodOn")

         self.lineEditSearchProductName = QtWidgets.QLineEdit(self.centralwidget)
         self.lineEditSearchProductName.setGeometry(QtCore.QRect(410, 30, 321, 31))
         self.lineEditSearchProductName.setObjectName("lineEditSearchProductName")

         self.BtnSearchProductName = QtWidgets.QPushButton(self.centralwidget)
         self.BtnSearchProductName.setGeometry(QtCore.QRect(740, 31, 31, 31))
         self.BtnSearchProductName.setText("")
         self.BtnSearchProductName.setIcon(icon5)
         self.BtnSearchProductName.setObjectName("BtnSearchProductName")

         self.labelSearchCustomer = QtWidgets.QLabel(self.centralwidget)
         self.labelSearchCustomer.setGeometry(QtCore.QRect(70, 5, 221, 20))
         self.labelSearchCustomer.setObjectName("labelSearchCustomer")

         self.labelSearchProductName = QtWidgets.QLabel(self.centralwidget)
         self.labelSearchProductName.setGeometry(QtCore.QRect(480, 5, 171, 20))
         self.labelSearchProductName.setObjectName("labelSearchProductName")

         self.line_11 = QtWidgets.QFrame(self.centralwidget)
         self.line_11.setGeometry(QtCore.QRect(390, 20, 20, 51))
         self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
         self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
         self.line_11.setObjectName("line_11")

         self.line_12 = QtWidgets.QFrame(self.centralwidget)
         self.line_12.setGeometry(QtCore.QRect(780, 20, 20, 51))
         self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
         self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
         self.line_12.setObjectName("line_12")

         TasksList.setCentralWidget(self.centralwidget)
         self.menubar = QtWidgets.QMenuBar(TasksList)
         self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 21))
         self.menubar.setObjectName("menubar")
         TasksList.setMenuBar(self.menubar)
         self.statusbar = QtWidgets.QStatusBar(TasksList)
         self.statusbar.setObjectName("statusbar")
         TasksList.setStatusBar(self.statusbar)

         self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
         self.BtnBack.setGeometry(QtCore.QRect(10, 720, 111, 31))
         font = QtGui.QFont()
         font.setPointSize(10)
         self.BtnBack.setFont(font)
         self.BtnBack.setObjectName("BtnBack")
         # self.BtnBack.setText("Назад")

         self.retranslateUi(TasksList)
         QtCore.QMetaObject.connectSlotsByName(TasksList)

    def retranslateUi(self, TasksList):
        _translate = QtCore.QCoreApplication.translate
        TasksList.setWindowTitle(_translate("TasksList", "Список заданий"))
        self.lineEditSearchCustomer.setPlaceholderText(_translate("TasksList", "Введите название фирмы заказчика"))
        self.lineEditSearchProductName.setPlaceholderText(_translate("TasksList", "Введите наименование изделия"))
        self.BtnSearchCustomer.setToolTip(_translate("TasksList", "Искать задания по названию заказчика"))
        self.BtnBack.setText(_translate("TasksList", "Назад"))
        self.labelProductName.setText(_translate("TasksList", "Наименование изделия/ Количество"))
        self.labelCheckNumber.setText(_translate("TasksList", "№ счёта"))
        self.labelDate.setText(_translate("TasksList", "Дата"))
        self.labelCustomer.setText(_translate("TasksList", "Название организации заказчика"))
        self.checkBoxPeriodOn.setText(_translate("TasksList", "В период от"))
        self.label_7.setText(_translate("TasksList", "по"))

    # def retranslateUi(self, TasksList):
    #     _translate = QtCore.QCoreApplication.translate
    #     TasksList.setWindowTitle(_translate("TasksList", "Список заданий"))
    #     self.labelProductName.setText(_translate("TasksList", "Наименование изделия/ Количество"))
    #     self.labelCheckNumber.setText(_translate("TasksList", "№ счёта"))
    #     self.labelDate.setText(_translate("TasksList", "Дата"))
    # #     # self.labelQuantity.setText(_translate("TasksList", "Количество"))
    #     self.labelCustomer.setText(_translate("TasksList", "Название организации заказчика"))
    #     self.LbCheckNumber.setText(_translate("TasksList", "142"))
    #     self.LbCustomer.setText(_translate("TasksList", "ООО \"Белагро Бел\""))
    #     self.LbDate.setText(_translate("TasksList", "26.07.2024"))
    #     # self.LbQuantity.setText(_translate("TasksList", "1000"))
    #     self.BtnBack.setText(_translate("TasksList", "Назад"))
    #     self.label_7.setText(_translate("TasksList", "по"))
    #     self.checkBoxPeriodOn.setText(_translate("TasksList", "В период от"))
    #     self.labelSearchCustomer.setText(_translate("TasksList", "Поиск по названию организации заказчика"))
    #     self.labelSearchProductName.setText(_translate("TasksList", "Поиск по наименованию изделия"))
#
# class TasksList(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_TasksList()
#         self.ui.setupUi(self)
#
#         # Обработчики для кнопок
#         self.ui.BtnSearchCustomer.clicked.connect(self.search_tasks_by_customer)
#         self.ui.BtnBack.clicked.connect(self.back_main_manager_window)
#
#         # Получаем данные из базы данных для названий организаций-заказчиков
#         customer = self.get_words_from_database("orders_customer", "organization_name")
#         # Настраиваем QCompleter для поля lineEditSearchCustomer
#         completer = QtWidgets.QCompleter(customer, self)
#         completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
#         self.ui.lineEditSearchCustomer.setCompleter(completer)
#
#         # Получаем данные из базы данных для наименований изделий
#         product_names = self.get_words_from_database("products_product", "name")
#         # Настраиваем QCompleter для поля lineEditSearchProductName
#         completer = QtWidgets.QCompleter(product_names, self)
#         completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
#         self.ui.lineEditSearchProductName.setCompleter(completer)
#
#         # # Пустой заполнитель
#         # self.empty_placeholder = QtWidgets.QWidget()
#         # self.empty_placeholder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         # self.ui.layoutTask.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout
#
#     def search_tasks_by_customer(self):
#         pass
#     #     # try:
#     #     # Создаем новый фрейм для выводимой строки
#     #     frame_task_line = QtWidgets.QFrame()
#     #     frame_task_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
#     #     frame_task_line.setFrameShadow(QtWidgets.QFrame.Raised)
#     #     frame_task_line.setStyleSheet("""
#     #     QFrame {
#     #         border: 1px solid black;
#     #             }
#     #          """)
#     #     frame_task_line.setFixedHeight(40)
#     #     # Создаем layout для элементов внутри строки
#     #     frame_layout = QtWidgets.QHBoxLayout(frame_task_line)
#     #     frame_layout.setContentsMargins(5, 5, 5, 5)
#     #     frame_layout.setSpacing(5)
#     #     #
#     #     # Лейбл с порядковым номером изделия
#     #     product_num = self.ui.layoutTask.count()  # Учитываем добавление заполнителя
#     #     label_product_num = QtWidgets.QLabel(str(product_num))
#     #     font = QtGui.QFont()
#     #     font.setPointSize(12)
#     #     label_product_num.setFont(font)
#     #     label_product_num.setStyleSheet("QLabel { border: none; }")
#     #     frame_layout.addWidget(label_product_num)
#         #
#         #     # Поле ввода названия изделия
#         #     lineEditProductName = QtWidgets.QLineEdit()
#         #     lineEditProductName.setFont(QtGui.QFont("Arial", 12))
#         #     lineEditProductName.setPlaceholderText("Введите название изделия")
#         #
#         #     # Настраиваем QCompleter для нового поля
#         #     product_names = self.get_words_from_database("products_product", "name")
#         #     completer = QtWidgets.QCompleter(product_names, self)
#         #     completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
#         #     lineEditProductName.setCompleter(completer)
#         #
#         #     frame_layout.addWidget(lineEditProductName)
#         #
#         #     # Поле ввода количества
#         #     spin_box_quantity = QtWidgets.QSpinBox()
#         #     spin_box_quantity.setFixedSize(80, 24)
#         #     spin_box_quantity.setStyleSheet("QSpinBox { font-size: 14px; }")
#         #     spin_box_quantity.setMaximum(999999)
#         #     spin_box_quantity.setSingleStep(10)
#         #     frame_layout.addWidget(spin_box_quantity)
#         #
#         #     # Кнопка удаления строки
#         #     btn_delete = QtWidgets.QPushButton()
#         #     btn_delete.setFixedSize(26, 26)
#         #     icon = QtGui.QIcon()
#         #     icon.addPixmap(QtGui.QPixmap(":/utils/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         #     btn_delete.setIcon(icon)
#         #     btn_delete.setIconSize(QtCore.QSize(16, 16))
#         #     frame_layout.addWidget(btn_delete)
#         #
#         #     # Привязка кнопки удаления к функции
#         #     btn_delete.clicked.connect(lambda: self.delete_product_line(frame_product_line))
#         #
#         #     # Добавляем созданный фрейм перед заполнителем
#         #     self.ui.layoutProducts.insertWidget(self.ui.layoutProducts.count() - 1, frame_product_line)
#         #
#         # except Exception as e:
#         #     print(f"Ошибка в add_product_line: {e}")
#         #
#         #
#         #
#     def get_words_from_database(self, table_name, column_name):
#         """
#         Получение данных из базы данных SQLite для указанной таблицы и столбца.
#         :param table_name: Название таблицы.
#         :param column_name: Название столбца.
#         :return: Список строк из указанного столбца.
#         """
#         try:
#             import os
#
#             # Путь к базе данных
#             BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#             db_path = os.path.join(BASE_DIR, "db.sqlite3")
#             conn = sqlite3.connect(db_path)
#
#             cursor = conn.cursor()
#
#             # Динамический SQL-запрос
#             query = f"SELECT DISTINCT {column_name} FROM {table_name}"
#             cursor.execute(query)
#             result = cursor.fetchall()
#
#             # Преобразуем результат в список строк
#             words = [row[0] for row in result]
#
#             conn.close()
#             return words
#
#         except sqlite3.Error as e:
#             print(f"Ошибка доступа к базе данных: {e}")
#             return []
#
#     def back_main_manager_window(self):
#         # Возврат к главному окну менеджера
#         from windows.main_manager_window import MainWindowManager
#         self.main_manager_window = MainWindowManager()
#         self.main_manager_window.show()
#         self.close()
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     TasksList = QtWidgets.QMainWindow()
#     ui = Ui_TasksList()
#     ui.setupUi(TasksList)
#     TasksList.show()
#     sys.exit(app.exec_())

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QDate
# from PyQt5.QtWidgets import QMessageBox
# from datetime import datetime
# import sqlite3
# import requests

# class Ui_TasksList(object):
#     def setupUi(self, TasksList):
#         TasksList.setObjectName("TasksList")
#         TasksList.resize(1132, 798)
#         self.centralwidget = QtWidgets.QWidget(TasksList)
#         self.centralwidget.setObjectName("centralwidget")
#
#         # Упрощение: остальной код интерфейса остается без изменений.
#
#         self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
#         self.scrollArea.setGeometry(QtCore.QRect(10, 110, 1111, 601))
#         self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
#         self.scrollArea.setWidgetResizable(True)
#         self.scrollArea.setObjectName("scrollArea")
#         self.scrollAreaWidgetContents = QtWidgets.QWidget()
#         self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
#         self.layoutTask = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
#         self.layoutTask.setContentsMargins(5, 5, 5, 5)
#         self.layoutTask.setSpacing(5)
#         self.scrollAreaWidgetContents.setLayout(self.layoutTask)
#         self.scrollArea.setWidget(self.scrollAreaWidgetContents)
#
#         self.lineEditSearchCustomer = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEditSearchCustomer.setGeometry(QtCore.QRect(20, 29, 321, 31))
#         self.lineEditSearchCustomer.setObjectName("lineEditSearchCustomer")
#
#         self.BtnSearchCustomer = QtWidgets.QPushButton(self.centralwidget)
#         self.BtnSearchCustomer.setGeometry(QtCore.QRect(350, 30, 31, 31))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap("../utils/icons/search.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
#         self.BtnSearchCustomer.setIcon(icon)
#         self.BtnSearchCustomer.setObjectName("BtnSearchCustomer")
#
#         TasksList.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(TasksList)
#         QtCore.QMetaObject.connectSlotsByName(TasksList)

        # def retranslateUi(self, TasksList):
        #     _translate = QtCore.QCoreApplication.translate
        #     TasksList.setWindowTitle(_translate("TasksList", "Список заданий"))
        #     self.lineEditSearchCustomer.setPlaceholderText(_translate("TasksList", "Введите название заказчика"))
        #     self.BtnSearchCustomer.setToolTip(_translate("TasksList", "Искать задания по названию заказчика"))

class TasksList(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TasksList()
        self.ui.setupUi(self)

        # Обработчики для кнопок
        self.ui.BtnSearchCustomer.clicked.connect(self.search_tasks_by_customer)


        self.ui.BtnBack.clicked.connect(self.back_main_manager_window)

        # Получаем данные из базы данных для названий организаций-заказчиков
        customer = self.get_words_from_database("orders_customer", "organization_name")
        # Настраиваем QCompleter для поля lineEditSearchCustomer
        completer = QtWidgets.QCompleter(customer, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lineEditSearchCustomer.setCompleter(completer)

        # Получаем данные из базы данных для наименований изделий
        product_names = self.get_words_from_database("products_product", "name")
        # Настраиваем QCompleter для поля lineEditSearchProductName
        completer = QtWidgets.QCompleter(product_names, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lineEditSearchProductName.setCompleter(completer)

        # # Пустой заполнитель
        # self.empty_placeholder = QtWidgets.QWidget()
        # self.empty_placeholder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # self.ui.layoutTask.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout

    def search_tasks_by_customer(self, name):
        customer_name = self.ui.lineEditSearchCustomer.text().strip()
        if not customer_name:
            QMessageBox.warning(self, "Ошибка", "Введите название заказчика.")
            return

        try:
            response = requests.get("http://127.0.0.1:8000/orders/customer_data/", params={"name": customer_name})
            if response.status_code == 200:
                data = response.json()
                self.update_task_list(data)
            else:
                QMessageBox.warning(self, "Ошибка", f"Ошибка сервера: {response.text}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось подключиться к серверу: {e}")

    def update_task_list(self, tasks):
        """
        Обновление списка заданий в прокручиваемой области.
        :param tasks: Список заданий, полученных с сервера.
        """
        # Очистка текущего списка
        for i in reversed(range(self.ui.layoutTask.count())):
            widget = self.ui.layoutTask.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Добавление новых заданий
        for task in tasks:
            # Создаем горизонтальный фрейм для каждого задания
            task_frame = QtWidgets.QFrame()
            task_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            task_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            task_frame.setStyleSheet("border: 1px solid black; margin: 2px;")
            task_frame.setGeometry(QtCore.QRect(10, 10, 1071, 100))

            # Горизонтальный layout для размещения текста в одну строку
            task_layout = QtWidgets.QHBoxLayout(task_frame)

            # Элементы задачи (счет, дата, заказчик)
            task_info = QtWidgets.QLabel(
                f"{task['invoice_number']} | {task['order_date']} | {task['customer_name']}"
            )
            task_info.setStyleSheet("font-weight: bold; font-size: 12px; margin: 5px;")
            task_layout.addWidget(task_info)

            # Создание комбобокса для продуктов
            product_combobox = QtWidgets.QComboBox()

            # Добавление продуктов в комбобокс
            for product in task["products"]:
                product_combobox.addItem(f"{product['name']} - {product['quantity']} шт.")

            # Добавление комбобокса в горизонтальный layout
            task_layout.addWidget(product_combobox)

            # Добавляем фрейм с заказом в layout основного окна
            self.ui.layoutTask.addWidget(task_frame)

    def get_words_from_database(self, table_name, column_name):

        """
        Получение данных из базы данных SQLite для указанной таблицы и столбца.
        :param table_name: Название таблицы.
        :param column_name: Название столбца.
        :return: Список строк из указанного столбца.
        """
        try:
            import os

            # Путь к базе данных
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(BASE_DIR, "db.sqlite3")
            conn = sqlite3.connect(db_path)

            cursor = conn.cursor()

            # Динамический SQL-запрос
            query = f"SELECT DISTINCT {column_name} FROM {table_name}"
            cursor.execute(query)
            result = cursor.fetchall()

            # Преобразуем результат в список строк
            words = [row[0] for row in result]

            conn.close()
            return words

        except sqlite3.Error as e:
            print(f"Ошибка доступа к базе данных: {e}")
            return []

    def back_main_manager_window(self):
        # Возврат к главному окну менеджера
        from windows.main_manager_window import MainWindowManager
        self.main_manager_window = MainWindowManager()
        self.main_manager_window.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TasksList()
    window.show()
    sys.exit(app.exec_())
