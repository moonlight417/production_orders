from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import resources_rc


class Ui_TaskFilling(object):
    def setupUi(self, TaskFilling):
        TaskFilling.setObjectName("TaskFilling")
        TaskFilling.resize(641, 785)

        self.centralwidget = QtWidgets.QWidget(TaskFilling)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 80, 621, 21))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.labelProduct = QtWidgets.QLabel(self.frame_3)
        self.labelProduct.setGeometry(QtCore.QRect(230, 0, 51, 16))
        self.labelProduct.setObjectName("labelProduct")

        self.labelQuantity = QtWidgets.QLabel(self.frame_3)
        self.labelQuantity.setGeometry(QtCore.QRect(475, 0, 61, 16))
        self.labelQuantity.setObjectName("labelQuantity")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 621, 551))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 602, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutProducts = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutProducts.setContentsMargins(5, 5, 5, 5)
        self.layoutProducts.setSpacing(5)
        self.scrollAreaWidgetContents.setLayout(self.layoutProducts)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.BtnForDeveloping = QtWidgets.QPushButton(self.centralwidget)
        self.BtnForDeveloping.setGeometry(QtCore.QRect(520, 720, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnForDeveloping.setFont(font)
        self.BtnForDeveloping.setObjectName("BtnForDeveloping")

        self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
        self.BtnBack.setGeometry(QtCore.QRect(10, 720, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnBack.setFont(font)
        self.BtnBack.setObjectName("BtnBack")

        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 30, 621, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.frameCustomer = QtWidgets.QFrame(self.frame_5)
        self.frameCustomer.setGeometry(QtCore.QRect(0, 0, 621, 41))
        self.frameCustomer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-color: rgb(0, 0, 0);")
        self.frameCustomer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCustomer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameCustomer.setLineWidth(2)
        self.frameCustomer.setMidLineWidth(1)
        self.frameCustomer.setObjectName("frameCustomer")

        self.dateEditDate = QtWidgets.QDateEdit(self.frameCustomer)
        self.dateEditDate.setGeometry(QtCore.QRect(58, 10, 81, 22))
        self.dateEditDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditDate.setCalendarPopup(True)
        self.dateEditDate.setDate(QDate.currentDate())
        self.dateEditDate.setObjectName("dateEditDate")

        self.lineEditCustomer = QtWidgets.QLineEdit(self.frameCustomer)
        self.lineEditCustomer.setGeometry(QtCore.QRect(150, 10, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCustomer.setFont(font)
        self.lineEditCustomer.setObjectName("lineEditCustomer")
        self.lineEditCheckNumber = QtWidgets.QLineEdit(self.frameCustomer)
        self.lineEditCheckNumber.setGeometry(QtCore.QRect(10, 10, 37, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCheckNumber.setFont(font)
        self.lineEditCheckNumber.setObjectName("lineEditCheckNumber")

        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 561, 21))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.labelCheckNumber = QtWidgets.QLabel(self.frame_6)
        self.labelCheckNumber.setGeometry(QtCore.QRect(0, 0, 51, 16))
        self.labelCheckNumber.setObjectName("labelCheckNumber")

        self.labelDate = QtWidgets.QLabel(self.frame_6)
        self.labelDate.setGeometry(QtCore.QRect(80, 0, 31, 16))
        self.labelDate.setObjectName("labelDate")

        self.labelCustomer = QtWidgets.QLabel(self.frame_6)
        self.labelCustomer.setGeometry(QtCore.QRect(260, 0, 171, 16))
        self.labelCustomer.setObjectName("labelCustomer")

        self.BtnAddNewProduct = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAddNewProduct.setGeometry(QtCore.QRect(12, 666, 123, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnAddNewProduct.setFont(font)
        icon1 = QtGui.QIcon()
        self.BtnAddNewProduct.setIcon(icon1)
        self.BtnAddNewProduct.setIconSize(QtCore.QSize(23, 23))
        self.BtnAddNewProduct.setObjectName("BtnAddNewProduct")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 700, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.BtnForDeveloping_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BtnForDeveloping_2.setGeometry(QtCore.QRect(396, 720, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnForDeveloping_2.setFont(font)
        self.BtnForDeveloping_2.setObjectName("BtnForDeveloping_2")

        TaskFilling.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskFilling)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menubar.setObjectName("menubar")
        TaskFilling.setMenuBar(self.menubar)

        self.retranslateUi(TaskFilling)
        QtCore.QMetaObject.connectSlotsByName(TaskFilling)

    def retranslateUi(self, TaskFilling):
        _translate = QtCore.QCoreApplication.translate
        TaskFilling.setWindowTitle(_translate("TaskFilling", "Оформление задания"))
        self.labelProduct.setText(_translate("TaskFilling", "Изделие"))
        self.labelQuantity.setText(_translate("TaskFilling", "Количество"))
        self.labelCheckNumber.setText(_translate("TaskFilling", "№ счёта"))
        self.labelDate.setText(_translate("TaskFilling", "Дата"))
        self.labelCustomer.setText(_translate("TaskFilling", "Название организации заказчика"))
        self.BtnAddNewProduct.setText(_translate("TaskFilling", "Добавить изделие"))
        # self.BtnUpdateNumbers.setText(_translate("TaskFilling", "Обновить нумерацию"))
        self.BtnForDeveloping.setText(_translate("TaskFilling", "На разработку"))
        self.BtnBack.setText(_translate("TaskFilling", "Назад"))
        self.BtnForDeveloping_2.setText(_translate("TaskFilling", "Сохранить"))


class TaskFilling(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TaskFilling()
        self.ui.setupUi(self)

        # Обработчики для кнопок
        self.ui.BtnAddNewProduct.clicked.connect(self.add_product_line)
        self.ui.BtnBack.clicked.connect(self.back_main_manager_window)

        # Пустой заполнитель
        self.empty_placeholder = QtWidgets.QWidget()
        self.empty_placeholder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.ui.layoutProducts.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout



    def add_product_line(self):
        try:
            # Создаем новый фрейм для строки изделия
            frame_product_line = QtWidgets.QFrame()
            frame_product_line.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame_product_line.setFrameShadow(QtWidgets.QFrame.Raised)
            frame_product_line.setStyleSheet("""
                QFrame {
                    border: 1px solid black;
                }
            """)
            frame_product_line.setFixedHeight(40)

            # Создаем layout для элементов внутри строки
            frame_layout = QtWidgets.QHBoxLayout(frame_product_line)
            frame_layout.setContentsMargins(5, 5, 5, 5)
            frame_layout.setSpacing(5)

            # Лейбл с порядковым номером изделия
            product_num = self.ui.layoutProducts.count()  # Учитываем добавление заполнителя
            label_product_num = QtWidgets.QLabel(str(product_num))
            font = QtGui.QFont()
            font.setPointSize(12)
            label_product_num.setFont(font)
            label_product_num.setStyleSheet("QLabel { border: none; }")
            frame_layout.addWidget(label_product_num)

            # Поле ввода названия изделия
            lineEditProductName = QtWidgets.QLineEdit()
            lineEditProductName.setFont(QtGui.QFont("Arial", 12))
            lineEditProductName.setPlaceholderText("Введите название изделия")
            frame_layout.addWidget(lineEditProductName)

            # Поле ввода количества
            spin_box_quantity = QtWidgets.QSpinBox()
            spin_box_quantity.setFixedSize(80, 24)
            spin_box_quantity.setStyleSheet("QSpinBox { font-size: 14px; }")
            spin_box_quantity.setMaximum(999999)
            spin_box_quantity.setSingleStep(10)
            frame_layout.addWidget(spin_box_quantity)

            # Кнопка удаления строки
            btn_delete = QtWidgets.QPushButton()
            btn_delete.setFixedSize(26, 26)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/utils/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn_delete.setIcon(icon)
            btn_delete.setIconSize(QtCore.QSize(16, 16))
            frame_layout.addWidget(btn_delete)

            # Привязка кнопки удаления к функции
            btn_delete.clicked.connect(lambda: self.delete_product_line(frame_product_line))

            # Добавляем созданный фрейм перед заполнителем
            self.ui.layoutProducts.insertWidget(self.ui.layoutProducts.count() - 1, frame_product_line)

            # Скрываем заполнитель
            self.update_empty_placeholder()

        except Exception as e:
            print(f"Ошибка в add_product_line: {e}")

    def delete_product_line(self, frame_product_line):
        """Удаление строки и обновление нумерации"""
        try:
            # Удаление фрейма из layout
            self.ui.layoutProducts.removeWidget(frame_product_line)
            frame_product_line.deleteLater()

            # Обновляем номера всех строк
            self.update_product_numbers()

            # Проверяем, нужно ли снова показать заполнитель
            self.update_empty_placeholder()

        except Exception as e:
            print(f"Ошибка в delete_product_line: {e}")

    def update_product_numbers(self):
        """Пересчитывает номера всех строк"""
        try:
            # Находим все фреймы в layoutProducts, исключая заполнитель
            for i in range(self.ui.layoutProducts.count() - 1):
                item = self.ui.layoutProducts.itemAt(i).widget()
                if isinstance(item, QtWidgets.QFrame):
                    label = item.findChild(QtWidgets.QLabel)  # Находим QLabel в фрейме
                    if label:
                        label.setText(str(i + 1))  # Обновляем номер
        except Exception as e:
            print(f"Ошибка в update_product_numbers: {e}")

    def update_empty_placeholder(self):
        """Показывает или скрывает заполнитель в зависимости от наличия строк"""
        if self.ui.layoutProducts.count() > 1:  # Есть хотя бы один элемент, кроме заполнителя
            self.empty_placeholder.hide()
        else:
            self.empty_placeholder.show()

    def back_main_manager_window(self):
        # Логика возврата к главному окну менеджера
        from windows.main_manager_window import MainWindowManager
        self.main_manager_window = MainWindowManager()
        self.main_manager_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = TaskFilling()
    main_window.show()
    sys.exit(app.exec_())

