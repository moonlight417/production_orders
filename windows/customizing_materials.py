
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

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
        self.BtnAddMaterial.setText(_translate("Materials", "Добавить запись"))
        self.BtnSaveChangesMaterial.setText(_translate("Materials", "Сохранить изменения"))

class Materials(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Materials()
        self.ui.setupUi(self)

        # Кнопки
        self.ui.BtnAddMaterial.clicked.connect(self.add_material_line)

        # # Пустой заполнитель
        # spacerItem2 = QtWidgets.QSpacerItem(20, 423, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.ui.verticalLayout_3.addItem(spacerItem2)

        # Пустой заполнитель снизу
        self.bottom_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                   QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_3.addItem(self.bottom_spacer)

    def add_material_line(self):
        print("Метод add_material_line вызван")
        try:
            # Создаём новый виджет для строки материала
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
            lineEditNameMaterial.setPlaceholderText("Материал")
            horizontalLayout_3.addWidget(lineEditNameMaterial)

            lineEditGostMaterial = QtWidgets.QLineEdit(widget_4)
            lineEditGostMaterial.setMaximumSize(QtCore.QSize(180, 16777215))
            lineEditGostMaterial.setFont(font)
            lineEditGostMaterial.setText("")
            lineEditGostMaterial.setObjectName("lineEditGostMaterial")
            lineEditGostMaterial.setPlaceholderText("ГОСТ ...")
            horizontalLayout_3.addWidget(lineEditGostMaterial)

            lineEditDensity = QtWidgets.QLineEdit(widget_4)
            lineEditDensity.setMaximumSize(QtCore.QSize(50, 16777215))
            lineEditDensity.setFont(font)
            lineEditDensity.setText("")
            lineEditDensity.setObjectName("lineEditDensity")
            lineEditDensity.setPlaceholderText("кг/м³")
            horizontalLayout_3.addWidget(lineEditDensity)

            lineEditLinkToSite = QtWidgets.QLineEdit(widget_4)
            lineEditLinkToSite.setFont(font)
            lineEditLinkToSite.setText("")
            lineEditLinkToSite.setObjectName("lineEditLinkToSite")
            lineEditLinkToSite.setPlaceholderText("Ссылка на сайт")
            horizontalLayout_3.addWidget(lineEditLinkToSite)

            # Кнопка удаления строки
            btn_delete = QtWidgets.QPushButton()
            btn_delete.setFixedSize(26, 26)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/utils/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn_delete.setIcon(icon)
            btn_delete.setIconSize(QtCore.QSize(16, 16))
            horizontalLayout_3.addWidget(btn_delete)

            # Привязка кнопки удаления к функции
            btn_delete.clicked.connect(lambda: self.delete_material_line(widget_4))

            # Добавляем новый виджет перед заполнителем
            self.ui.verticalLayout_3.insertWidget(self.ui.verticalLayout_3.count() - 1, widget_4)
            print("Строка добавлена успешно.")

            # Обновляем размер scrollArea
            self.ui.scrollAreaWidgetContents.adjustSize()

        except Exception as e:
            print(f"Ошибка в add_material_line: {e}")

    def delete_material_line(self, widget_4):
        """Удаление строки материала и обновление интерфейса"""
        try:
            layout = self.ui.verticalLayout_3

            # Проверяем, есть ли виджет в Layout
            if layout.indexOf(widget_4) != -1:
                layout.removeWidget(widget_4)
                widget_4.setParent(None)

                # Отложенное удаление виджета
                QtCore.QTimer.singleShot(0, widget_4.deleteLater)
                print("Строка успешно удалена.")

            # Обновляем размер scrollArea
            self.ui.scrollAreaWidgetContents.adjustSize()
        except Exception as e:
            print(f"Ошибка в delete_material_line: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Materials()  # Создаём экземпляр вашего класса Materials
    window.show()         # Показываем окно
    sys.exit(app.exec_())