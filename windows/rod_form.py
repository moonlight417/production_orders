from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3  # Используем SQLite для примера, замените на свою БД

class Ui_Forms(object):
    def setupUi(self, Forms):
        Forms.setObjectName("Forms")
        Forms.resize(1102, 660)

        self.centralwidget = QtWidgets.QWidget(Forms)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Метка
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("Применяемые формы:")
        self.verticalLayout.addWidget(self.label)

        # Область прокрутки
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        # Кнопки
        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setObjectName("button_widget")
        self.button_Layout = QtWidgets.QHBoxLayout(self.button_widget)
        self.button_Layout.setContentsMargins(0, 0, 0, 0)  # Убираем внешние отступы
        self.button_Layout.setSpacing(10)  # Устанавливаем отступы между кнопками

        self.BtnAddForm = QtWidgets.QPushButton()
        self.BtnAddForm.setObjectName("BtnAddForm")
        self.BtnAddForm.setText("Добавить запись")
        self.button_Layout.addWidget(self.BtnAddForm)

        self.BtnSaveChangesMaterial = QtWidgets.QPushButton()
        self.BtnSaveChangesMaterial.setObjectName("BtnSaveChangesMaterial")
        self.BtnSaveChangesMaterial.setText("Сохранить изменения")
        self.button_Layout.addWidget(self.BtnSaveChangesMaterial)

        self.verticalLayout.addWidget(self.button_widget)

        Forms.setCentralWidget(self.centralwidget)
        self.retranslateUi(Forms)
        QtCore.QMetaObject.connectSlotsByName(Forms)

    def retranslateUi(self, Forms):
        _translate = QtCore.QCoreApplication.translate
        Forms.setWindowTitle(_translate("Forms", "Формы"))
        self.label.setText(_translate("Forms", "Применяемые формы:"))
        self.BtnAddForm.setText(_translate("Forms", "Добавить запись"))
        self.BtnSaveChangesMaterial.setText(_translate("Forms", "Сохранить изменения"))


class Forms(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Forms()
        self.ui.setupUi(self)

        self.conn = sqlite3.connect("database.db")  # Подключение к БД
        self.cursor = self.conn.cursor()

        self.ui.BtnAddForm.clicked.connect(self.add_form_line)
        self.ui.BtnSaveChangesMaterial.clicked.connect(self.save_changes)

        # Добавляем подпружинивание
        self.bottom_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_3.addItem(self.bottom_spacer)

        self.load_data()  # Загружаем данные при старте

    def load_data(self):
        """Загружает данные из базы и отображает их в UI"""
        try:
            self.cursor.execute("SELECT id, material, section_shape, section_size1, section_size2, bar_length, standard FROM RodForm")
            rows = self.cursor.fetchall()
            for row in rows:
                self.add_form_line(row)
        except Exception as e:
            print(f"Ошибка при загрузке данных: {e}")

    def add_form_line(self, data=None):
        """Добавляет строку в форму. Если переданы данные, заполняет их."""
        widget_4 = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
        horizontalLayout_3 = QtWidgets.QHBoxLayout(widget_4)

        # Комбобокс для формы сечения
        comboBoxShape = QtWidgets.QComboBox(widget_4)
        comboBoxShape.addItems(["Круг", "Шестигранник", "Квадрат", "Труба"])

        if data and data[2] in ["Круг", "Шестигранник", "Квадрат", "Труба"]:
            comboBoxShape.setCurrentText(data[2])

        horizontalLayout_3.addWidget(comboBoxShape)

        lineEditSize1 = QtWidgets.QLineEdit(widget_4)
        lineEditSize1.setPlaceholderText("Размер 1, мм")
        lineEditSize1.setText(str(data[3]) if data else "")
        horizontalLayout_3.addWidget(lineEditSize1)

        lineEditSize2 = QtWidgets.QLineEdit(widget_4)
        lineEditSize2.setPlaceholderText("Размер 2, мм (если есть)")
        lineEditSize2.setText(str(data[4]) if data else "")
        horizontalLayout_3.addWidget(lineEditSize2)

        lineEditLength = QtWidgets.QLineEdit(widget_4)
        lineEditLength.setPlaceholderText("Длина, мм")
        lineEditLength.setText(str(data[5]) if data else "")
        horizontalLayout_3.addWidget(lineEditLength)

        lineEditStandard = QtWidgets.QLineEdit(widget_4)
        lineEditStandard.setPlaceholderText("ГОСТ")
        lineEditStandard.setText(str(data[6]) if data else "")
        horizontalLayout_3.addWidget(lineEditStandard)

        btn_delete = QtWidgets.QPushButton(widget_4)
        btn_delete.setText("X")
        btn_delete.clicked.connect(lambda: self.delete_form_line(widget_4))
        horizontalLayout_3.addWidget(btn_delete)

        # Вставляем перед нижним пустым пространством
        self.ui.verticalLayout_3.insertWidget(self.ui.verticalLayout_3.count() - 1, widget_4)

    def delete_form_line(self, widget):
        """Удаляет строку формы"""
        self.ui.verticalLayout_3.removeWidget(widget)
        widget.setParent(None)

    def save_changes(self):
        """Сохраняет изменения в БД"""
        try:
            self.cursor.execute("DELETE FROM RodForm")  # Очистка таблицы перед сохранением

            for i in range(self.ui.verticalLayout_3.count()):
                widget = self.ui.verticalLayout_3.itemAt(i).widget()
                if widget and isinstance(widget, QtWidgets.QWidget):
                    lineEdits = widget.findChildren(QtWidgets.QLineEdit)
                    if len(lineEdits) == 6:  # Убеждаемся, что у нас 6 полей
                        material = lineEdits[0].text()
                        shape = lineEdits[1].text()
                        size1 = lineEdits[2].text()
                        size2 = lineEdits[3].text() or "NULL"
                        length = lineEdits[4].text()
                        standard = lineEdits[5].text()

                        self.cursor.execute(
                            "INSERT INTO RodForm (material, section_shape, section_size1, section_size2, bar_length, standard) VALUES (?, ?, ?, ?, ?, ?)",
                            (material, shape, size1, size2, length, standard)
                        )

            self.conn.commit()
            print("Изменения сохранены.")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Forms()
    window.show()
    sys.exit(app.exec_())
