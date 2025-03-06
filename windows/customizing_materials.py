
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
from materials.models import Material
import webbrowser

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
        font = self.label_title.font()
        font.setPointSize(18)
        self.label_title.setFont(font)
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

        # Загрузка существующих материалов при инициализации
        self.load_materials()

        # Подключаем кнопки
        self.ui.BtnAddMaterial.clicked.connect(self.add_material_line)
        self.ui.BtnSaveChangesMaterial.clicked.connect(self.save_changes)

        # Заполнитель снизу
        self.bottom_spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum,
                                                   QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_3.addItem(self.bottom_spacer)

    def load_materials(self):
        """Загрузка материалов из базы данных в интерфейс"""
        materials = Material.objects.all()
        for material in materials:
            self.add_material_line(material)

    def add_material_line(self, material=None):
        """Добавление строки с материалом (новая или существующая запись)"""
        try:
            widget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
            widget.setObjectName("material_widget")
            layout = QtWidgets.QHBoxLayout(widget)

            # Поля для ввода
            name_edit = QtWidgets.QLineEdit(widget)
            name_edit.setPlaceholderText("Материал")
            name_edit.setFixedWidth(200)  # Устанавливаем фиксированную ширину 200 пикселей

            gost_edit = QtWidgets.QLineEdit(widget)
            gost_edit.setPlaceholderText("ГОСТ")
            gost_edit.setFixedWidth(200)  # Устанавливаем фиксированную ширину 200 пикселей

            density_edit = QtWidgets.QLineEdit(widget)
            density_edit.setPlaceholderText("кг/м³")
            density_edit.setFixedWidth(70)  # Устанавливаем фиксированную ширину 100 пикселей

            link_edit = QtWidgets.QLineEdit(widget)
            link_edit.setPlaceholderText("Ссылка")
            # link_edit.setFixedWidth(300)  # Устанавливаем фиксированную ширину 300 пикселей

            # Если передан существующий материал - заполняем поля
            if material:
                name_edit.setText(material.name)
                gost_edit.setText(material.standard)
                density_edit.setText(str(material.density))
                link_edit.setText(material.website_link)
                widget.material = material  # Сохраняем ссылку на объект

            # Сохраняем ссылки на поля в виджете
            widget.line_edits = (name_edit, gost_edit, density_edit, link_edit)

            # Кнопка открытия сайта
            btn_open_link = QtWidgets.QPushButton()
            btn_open_link.setText("website")
            # btn_open_link.setIcon(QtGui.QIcon(":/utils/icons/site.svg"))
            btn_open_link.setFixedWidth(70)
            btn_open_link.clicked.connect(lambda: self.open_link(link_edit.text()))

            # Кнопка удаления
            btn_delete = QtWidgets.QPushButton()
            btn_delete.setIcon(QtGui.QIcon(":/utils/icons/x-square.svg"))
            btn_delete.setFixedWidth(40)
            btn_delete.clicked.connect(lambda: self.confirm_delete_material(widget))
            # btn_delete.clicked.connect(lambda: self.delete_material_line(widget))

            # Добавляем элементы в layout
            layout.addWidget(name_edit)
            layout.addWidget(gost_edit)
            layout.addWidget(density_edit)
            layout.addWidget(link_edit)
            layout.addWidget(btn_open_link)
            layout.addWidget(btn_delete)

            # Вставляем перед заполнителем
            self.ui.verticalLayout_3.insertWidget(
                self.ui.verticalLayout_3.count() - 1,
                widget
            )

        except Exception as e:
            print(f"Ошибка при добавлении строки: {e}")

    def open_link(self, url):
        """Открывает ссылку в браузере"""
        if url:  # Проверяем, что URL не пустой
            webbrowser.open(url)  # Открываем URL в браузере
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Ссылка не указана!")

    def confirm_delete_material(self, widget):
        """Подтверждение удаления материала"""
        reply = QtWidgets.QMessageBox.question(
            self,
            "Подтверждение удаления",
            "Вы действительно хотите удалить материал?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            self.delete_material_line(widget)  # Удаляем материал, если пользователь подтвердил

    def save_changes(self):
        """Сохранение всех изменений в базе данных"""
        try:
            existing_materials = set(Material.objects.all())
            used_materials = set()

            # Обрабатываем все строки
            for i in range(self.ui.verticalLayout_3.count()):
                item = self.ui.verticalLayout_3.itemAt(i)
                if item.widget() and hasattr(item.widget(), 'line_edits'):
                    widget = item.widget()
                    name, gost, density, link = [field.text() for field in widget.line_edits]

                    # Валидация плотности
                    try:
                        density_value = float(density) if density else 0.0
                    except ValueError:
                        QtWidgets.QMessageBox.warning(
                            self,
                            "Ошибка",
                            "Некорректное значение плотности!"
                        )
                        return

                    # Обновление или создание материала
                    if hasattr(widget, 'material'):
                        material = widget.material
                        material.name = name
                        material.standard = gost
                        material.density = density_value
                        material.website_link = link
                        used_materials.add(material)
                    else:
                        material = Material.objects.create(
                            name=name,
                            standard=gost,
                            density=density_value,
                            website_link=link
                        )
                        used_materials.add(material)

            # Удаление отсутствующих материалов
            for material in existing_materials - used_materials:
                material.delete()

            QtWidgets.QMessageBox.information(
                self,
                "Успех",
                "Все изменения успешно сохранены!"
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                f"Ошибка при сохранении: {str(e)}"
            )

    def delete_material_line(self, widget):
        """Удаление строки материала из интерфейса"""
        self.ui.verticalLayout_3.removeWidget(widget)
        widget.deleteLater()
        self.ui.scrollAreaWidgetContents.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Materials()  # Создаём экземпляр вашего класса Materials
    window.show()         # Показываем окно
    sys.exit(app.exec_())