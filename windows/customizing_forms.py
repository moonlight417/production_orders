
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

class Ui_Forms(object):
    def setupUi(self, Forms):
        Forms.setObjectName("Forms")
        Forms.resize(1102, 660)

        self.centralwidget = QtWidgets.QWidget(Forms)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1047, 548))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        # self.widget_4.setObjectName("widget_4")
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # self.lineEditNameMaterial = QtWidgets.QLineEdit(self.widget_4)
        # self.lineEditNameMaterial.setMaximumSize(QtCore.QSize(16777215, 16777215))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.lineEditNameMaterial.setFont(font)
        # self.lineEditNameMaterial.setText("")
        # self.lineEditNameMaterial.setObjectName("lineEditNameMaterial")
        # self.horizontalLayout_3.addWidget(self.lineEditNameMaterial)
        # self.lineEditGostMaterial = QtWidgets.QLineEdit(self.widget_4)
        # self.lineEditGostMaterial.setMaximumSize(QtCore.QSize(180, 16777215))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.lineEditGostMaterial.setFont(font)
        # self.lineEditGostMaterial.setText("")
        # self.lineEditGostMaterial.setObjectName("lineEditGostMaterial")
        # self.horizontalLayout_3.addWidget(self.lineEditGostMaterial)
        # self.checkBoxSelectMaterial = QtWidgets.QCheckBox(self.widget_4)
        # self.checkBoxSelectMaterial.setText("")
        # self.checkBoxSelectMaterial.setIconSize(QtCore.QSize(20, 20))
        # self.checkBoxSelectMaterial.setObjectName("checkBoxSelectMaterial")
        # self.horizontalLayout_3.addWidget(self.checkBoxSelectMaterial)
        # self.verticalLayout_3.addWidget(self.widget_4)
        # spacerItem2 = QtWidgets.QSpacerItem(20, 479, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout_3.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.main_widget)
        self.bottom_panel_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_panel_widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.bottom_panel_widget.setObjectName("bottom_panel_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_panel_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.BtnDeleteSelectedMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.BtnDeleteSelectedMaterial.setFont(font)
        # self.BtnDeleteSelectedMaterial.setObjectName("BtnDeleteSelectedMaterial")
        # self.horizontalLayout_2.addWidget(self.BtnDeleteSelectedMaterial)
        # spacerItem3 = QtWidgets.QSpacerItem(322, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem3)
        self.BtnAddForm = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnAddForm.setFont(font)
        self.BtnAddForm.setObjectName("BtnAddMaterial")
        self.horizontalLayout_2.addWidget(self.BtnAddForm)
        spacerItem4 = QtWidgets.QSpacerItem(321, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.BtnSaveChangesMaterial = QtWidgets.QPushButton(self.bottom_panel_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnSaveChangesMaterial.setFont(font)
        self.BtnSaveChangesMaterial.setObjectName("BtnSaveChangesMaterial")
        self.horizontalLayout_2.addWidget(self.BtnSaveChangesMaterial)
        self.verticalLayout.addWidget(self.bottom_panel_widget)
        Forms.setCentralWidget(self.centralwidget)

        self.retranslateUi(Forms)
        QtCore.QMetaObject.connectSlotsByName(Forms)

    def retranslateUi(self, Forms):
        _translate = QtCore.QCoreApplication.translate
        Forms.setWindowTitle(_translate("Forms", "Формы"))
        self.label.setText(_translate("Forms", "Применяемые формы:"))

        # self.BtnDeleteSelectedMaterial.setText(_translate("Forms", "Удалить выбранную запись"))
        self.BtnAddForm.setText(_translate("Forms", "Добавить запись"))
        self.BtnSaveChangesMaterial.setText(_translate("Forms", "Сохранить изменения"))

class Forms(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Forms()
        self.ui.setupUi(self)

        # Кнопки
        self.ui.BtnAddForm.clicked.connect(self.add_form_line)

        # Пустой заполнитель снизу
        self.bottom_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                   QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_3.addItem(self.bottom_spacer)

    def add_form_line(self):
        print("Метод add_material_line вызван")
        try:
            # Создаём новый виджет для строки материала
            widget_4 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            widget_4.setObjectName("widget_4")

            horizontalLayout_3 = QtWidgets.QHBoxLayout(widget_4)
            horizontalLayout_3.setObjectName("horizontalLayout_3")

            # Поля для ввода

            lineEditNameForm = QtWidgets.QLineEdit(widget_4)
            lineEditNameForm.setMaximumSize(QtCore.QSize(16777215, 16777215))
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditNameForm.setFont(font)
            lineEditNameForm.setText("")
            lineEditNameForm.setObjectName("lineEditNameMaterial")
            lineEditNameForm.setPlaceholderText("Форма")
            horizontalLayout_3.addWidget(lineEditNameForm)

            lineEditGostForm = QtWidgets.QLineEdit(widget_4)
            lineEditGostForm.setMaximumSize(QtCore.QSize(180, 16777215))
            font = QtGui.QFont()
            font.setPointSize(11)
            lineEditGostForm.setFont(font)
            lineEditGostForm.setText("")
            lineEditGostForm.setObjectName("lineEditGostMaterial")
            lineEditGostForm.setPlaceholderText("ГОСТ ...")
            horizontalLayout_3.addWidget(lineEditGostForm)

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

    def delete_form_line(self, widget_4):
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
    window = Forms()  # Создаём экземпляр вашего класса Materials
    window.show()         # Показываем окно
    sys.exit(app.exec_())
