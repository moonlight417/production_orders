
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

class Ui_Employees(object):
    def setupUi(self, Employees):
        Employees.setObjectName("Employees")
        Employees.resize(1051, 575)
        self.centralwidget = QtWidgets.QWidget(Employees)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_widget = QtWidgets.QWidget(self.centralwidget)
        self.header_widget.setMaximumSize(QtCore.QSize(16777215, 20))
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.header_widget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.header_widget)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.main_widget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 996, 463))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.main_widget)
        self.bottom_panel_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_panel_widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.bottom_panel_widget.setObjectName("bottom_panel_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_panel_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BtnAddEmployee = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnAddEmployee.setFont(font)
        self.BtnAddEmployee.setObjectName("BtnAddMaterial")
        self.horizontalLayout_2.addWidget(self.BtnAddEmployee)
        spacerItem4 = QtWidgets.QSpacerItem(301, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.BtnSaveChangesMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnSaveChangesMaterial.setFont(font)
        self.BtnSaveChangesMaterial.setObjectName("BtnSaveChangesMaterial")
        self.horizontalLayout_2.addWidget(self.BtnSaveChangesMaterial)
        self.verticalLayout.addWidget(self.bottom_panel_widget)
        Employees.setCentralWidget(self.centralwidget)

        self.retranslateUi(Employees)
        QtCore.QMetaObject.connectSlotsByName(Employees)

    def retranslateUi(self, Employees):
        _translate = QtCore.QCoreApplication.translate
        Employees.setWindowTitle(_translate("Employees", "Сотрудники"))
        self.BtnAddEmployee.setText(_translate("Employees", "Добавить запись"))
        self.BtnSaveChangesMaterial.setText(_translate("Employees", "Сохранить изменения"))

class Employees(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Employees()
        self.ui.setupUi(self)

        # Кнопки
        self.ui.BtnAddEmployee.clicked.connect(self.add_form_line)

        # Пустой заполнитель снизу
        self.bottom_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                   QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_3.addItem(self.bottom_spacer)

    def add_form_line(self):
        print("Метод add_material_line вызван")
        try:
            # Создаём новый виджет для строки сотрудника
            widget_4 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            widget_4.setObjectName("widget_4")

            horizontalLayout_3 = QtWidgets.QHBoxLayout(widget_4)
            horizontalLayout_3.setObjectName("horizontalLayout_3")

            employee_num = self.ui.verticalLayout_3.count()  # Учитываем добавление заполнителя
            LbNumberEmployee = QtWidgets.QLabel(str(employee_num))
            font = QtGui.QFont()
            font.setPointSize(12)
            LbNumberEmployee.setFont(font)
            LbNumberEmployee.setObjectName("LbNumberEmployee")
            horizontalLayout_3.addWidget(LbNumberEmployee)

            # Поля для ввода
            lineEditSecondName = QtWidgets.QLineEdit(widget_4)
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditSecondName.setFont(font)
            lineEditSecondName.setText("")
            lineEditSecondName.setObjectName("lineEditSecondName")
            lineEditSecondName.setPlaceholderText( "Фамилия")
            horizontalLayout_3.addWidget(lineEditSecondName)

            lineEditFirstName = QtWidgets.QLineEdit(widget_4)
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditFirstName.setFont(font)
            lineEditFirstName.setText("")
            lineEditFirstName.setObjectName("lineEditFirstName")
            lineEditFirstName.setPlaceholderText("Имя ")
            horizontalLayout_3.addWidget(lineEditFirstName)

            lineEditMiddleName = QtWidgets.QLineEdit(widget_4)
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditMiddleName.setFont(font)
            lineEditMiddleName.setText("")
            lineEditMiddleName.setObjectName("lineEditMiddleName")
            lineEditMiddleName.setPlaceholderText("Отчество")
            horizontalLayout_3.addWidget(lineEditMiddleName)

            lineEditPost = QtWidgets.QLineEdit(widget_4)
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditPost.setFont(font)
            lineEditPost.setText("")
            lineEditPost.setObjectName("lineEditPost")
            lineEditPost.setPlaceholderText("Должность")
            horizontalLayout_3.addWidget(lineEditPost)

            # Меню выбора роли
            comboBoxRole = QtWidgets.QComboBox(widget_4)
            comboBoxRole.setMinimumSize(QtCore.QSize(80, 0))
            comboBoxRole.setCurrentText("")
            comboBoxRole.setObjectName("comboBoxRole")
            comboBoxRole.addItem("")
            comboBoxRole.addItem("Менеджер")
            comboBoxRole.addItem("Инженер")
            comboBoxRole.addItem("Производство")
            horizontalLayout_3.addWidget(comboBoxRole)

            # Кнопка удаления строки
            btn_delete = QtWidgets.QPushButton()
            btn_delete.setFixedSize(26, 26)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/utils/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn_delete.setIcon(icon)
            btn_delete.setIconSize(QtCore.QSize(16, 16))
            horizontalLayout_3.addWidget(btn_delete)

            # Привязка кнопки удаления к функции
            btn_delete.clicked.connect(lambda: self.delete_form_line(widget_4))

            # Добавляем новый виджет перед заполнителем
            self.ui.verticalLayout_3.insertWidget(self.ui.verticalLayout_3.count() - 1, widget_4)
            print("Строка добавлена успешно.")

            # Обновляем размер scrollArea
            self.ui.scrollAreaWidgetContents.adjustSize()

        except Exception as e:
            print(f"Ошибка в add_material_line: {e}")


    def delete_form_line(self, frame_product_line):
        """Удаление строки и обновление нумерации"""
        try:
            # Удаление фрейма из layout
            self.ui.verticalLayout_3.removeWidget(frame_product_line)
            frame_product_line.deleteLater()

            # Обновляем номера всех строк
            self.update_employees_numbers()

        except Exception as e:
            print(f"Ошибка в delete_product_line: {e}")

    def update_employees_numbers(self):
        """Пересчитывает номера всех строк"""
        try:
            # Перебираем все элементы в layout, исключая заполнитель
            for i in range(self.ui.verticalLayout_3.count() - 1):
                item = self.ui.verticalLayout_3.itemAt(i).widget()
                if isinstance(item, QtWidgets.QWidget):  # Проверяем, что это QWidget
                    label = item.findChild(QtWidgets.QLabel,
                                           "LbNumberEmployee")  # Ищем QLabel с именем "LbNumberEmployee"
                    if label:
                        label.setText(str(i + 1))  # Обновляем номер
        except Exception as e:
            print(f"Ошибка в update_employees_numbers: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Employees()  # Создаём экземпляр вашего класса Materials
    window.show()         # Показываем окно
    sys.exit(app.exec_())

