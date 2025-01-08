
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Materials(object):
    def setupUi(self, Materials):
        Materials.setObjectName("Materials")
        Materials.resize(948, 604)

        self.centralwidget = QtWidgets.QWidget(Materials)
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

        self.label_title = QtWidgets.QLabel(self.header_widget)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_title.setObjectName("label")
        self.horizontalLayout.addWidget(self.label_title)

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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 893, 492))
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

        self.BtnDeleteSelectedMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnDeleteSelectedMaterial.setFont(font)
        self.BtnDeleteSelectedMaterial.setObjectName("BtnDeleteSelectedMaterial")
        self.horizontalLayout_2.addWidget(self.BtnDeleteSelectedMaterial)

        spacerItem3 = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        # self.BtnAddMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        # self.BtnAddMaterial.setObjectName("BtnAddMaterial")
        self.BtnAddMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnAddMaterial.setFont(font)
        self.BtnAddMaterial.setObjectName("BtnAddMaterial")
        self.horizontalLayout_2.addWidget(self.BtnAddMaterial)


        spacerItem4 = QtWidgets.QSpacerItem(257, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.BtnSaveChangesMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnSaveChangesMaterial.setFont(font)
        self.BtnSaveChangesMaterial.setObjectName("BtnSaveChangesMaterial")
        self.horizontalLayout_2.addWidget(self.BtnSaveChangesMaterial)

        self.verticalLayout.addWidget(self.bottom_panel_widget)
        Materials.setCentralWidget(self.centralwidget)

        self.retranslateUi(Materials)
        QtCore.QMetaObject.connectSlotsByName(Materials)

    def retranslateUi(self, Materials):
        _translate = QtCore.QCoreApplication.translate
        Materials.setWindowTitle(_translate("Materials", "Материалы"))
        self.label_title.setText(_translate("Materials", "Применяемые материалы:"))
        # self.lineEditNameMaterial.setPlaceholderText(_translate("Materials", "Материал"))
        # self.lineEditGostMaterial.setPlaceholderText(_translate("Materials", "ГОСТ ..."))
        # self.lineEditDensity.setPlaceholderText(_translate("Materials", "кг/м³"))
        # self.lineEditLinkToSite.setPlaceholderText(_translate("Materials", "Ссылка на сайт"))
        self.BtnDeleteSelectedMaterial.setText(_translate("Materials", "Удалить выбранную запись"))
        self.BtnAddMaterial.setText(_translate("Materials", "Добавить запись"))
        self.BtnSaveChangesMaterial.setText(_translate("Materials", "Сохранить изменения"))

class Materials(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Materials()
        self.ui.setupUi(self)

        self.ui.BtnAddMaterial.clicked.connect(self.add_material_line)  # Убираем скобки
        # self.ui.BtnAddMaterial.setText("Проверка кнопки")
        # self.ui.BtnAddMaterial.clicked.connect(lambda: print("Кнопка нажата"))
        # self.BtnDeleteSelectedMaterial.connect(self.delete_material_line)


    def add_material_line(self):
        print("Метод add_material_line вызван")
        try:
            print("Добавление строки материала...")  # Отладочный вывод

            # Создаем новый виджет для строки материала
            widget_4 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            widget_4.setObjectName("widget_4")

            horizontalLayout_3 = QtWidgets.QHBoxLayout(widget_4)
            horizontalLayout_3.setObjectName("horizontalLayout_3")

            # Поля для ввода
            lineEditNameMaterial = QtWidgets.QLineEdit(widget_4)
            lineEditNameMaterial.setMaximumSize(QtCore.QSize(150, 16777215))
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditNameMaterial.setFont(font)
            lineEditNameMaterial.setText("")
            lineEditNameMaterial.setObjectName("lineEditNameMaterial")
            horizontalLayout_3.addWidget(lineEditNameMaterial)

            lineEditGostMaterial = QtWidgets.QLineEdit(widget_4)
            lineEditGostMaterial.setMaximumSize(QtCore.QSize(180, 16777215))
            lineEditGostMaterial.setFont(font)
            lineEditGostMaterial.setText("")
            lineEditGostMaterial.setObjectName("lineEditGostMaterial")
            horizontalLayout_3.addWidget(lineEditGostMaterial)

            lineEditDensity = QtWidgets.QLineEdit(widget_4)
            lineEditDensity.setMaximumSize(QtCore.QSize(50, 16777215))
            lineEditDensity.setFont(font)
            lineEditDensity.setText("")
            lineEditDensity.setObjectName("lineEditDensity")
            horizontalLayout_3.addWidget(lineEditDensity)

            lineEditLinkToSite = QtWidgets.QLineEdit(widget_4)
            lineEditLinkToSite.setFont(font)
            lineEditLinkToSite.setText("")
            lineEditLinkToSite.setObjectName("lineEditLinkToSite")
            horizontalLayout_3.addWidget(lineEditLinkToSite)

            checkBoxSelectMaterial = QtWidgets.QCheckBox(widget_4)
            checkBoxSelectMaterial.setText("")
            checkBoxSelectMaterial.setIconSize(QtCore.QSize(20, 20))
            checkBoxSelectMaterial.setObjectName("checkBoxSelectMaterial")
            horizontalLayout_3.addWidget(checkBoxSelectMaterial)

            # Добавляем новый виджет в layout
            self.ui.verticalLayout_3.addWidget(widget_4)
            print("Строка добавлена успешно.")

            # Обновляем размер scrollArea
            self.ui.scrollAreaWidgetContents.adjustSize()

        except Exception as e:
            print(f"Ошибка в add_material_line: {e}")

    def delete_material_line(self, widget_4):
        """Удаление строки и обновление нумерации"""
        try:
            # Удаление фрейма из layout
            self.ui.scrollAreaWidgetContents.removeWidget(widget_4)
            widget_4.deleteLater()


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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Materials()  # Создаём экземпляр вашего класса Materials
    window.show()         # Показываем окно
    sys.exit(app.exec_())
