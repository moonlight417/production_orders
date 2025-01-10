from functools import partial
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
import sys
import resources_rc

class DesignDocumentFillingForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DesignDocumentFillingForm()
        self.ui.setupUi(self)

        self.rotation_angle = 0  # Угол поворота изображения

        # Список защищённых вкладок по индексам
        self.protected_tabs = [self.ui.tabWidget.indexOf(self.ui.tab_struct),
                               self.ui.tabWidget.indexOf(self.ui.tab_tags)]

        # Подключаем кнопки

        self.ui.BtnAddDetail.clicked.connect(self.add_tab)  # Добавление вкладки "Деталь"
        self.ui.BtnAddAssemblyUnit.clicked.connect(self.add_assembly_unit)  # Добавление вкладки "Сборочная единица"
        self.ui.BtnSaveTabName.clicked.connect(self.save_tab_name)

    def open_file(self):
        """Метод открытия файла"""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл", "../utils/drawings/",
            "Изображения (*.png *.jpg *.bmp *.gif)"
        )

        if file_path:
            self.current_image_path = file_path
            self.rotation_angle = 0  # Сбрасываем угол поворота
            self.update_image()
            print(f"Выбранное изображение: {file_path}")
        else:
            print("Файл не выбран")

    def update_image(self):
        """Метод обновления изображения с учетом поворота"""
        pixmap = QtGui.QPixmap(self.current_image_path)

        # Поворачиваем изображение, если угол поворота не равен нулю
        if self.rotation_angle != 0:
            transform = QtGui.QTransform()
            transform.rotate(self.rotation_angle)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)

        label_size = self.label_image.size()
        scaled_pixmap = pixmap.scaled(label_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_image.setPixmap(scaled_pixmap)

    def rotate_left(self):
        """Метод для поворота изображения влево"""
        self.rotation_angle -= 90  # Уменьшаем угол на 90 градусов
        self.rotation_angle %= 360  # Ограничиваем угол в пределах 0-359
        self.update_image()  # Обновляем изображение

    def rotate_right(self):
        """Метод для поворота изображения вправо"""
        self.rotation_angle += 90  # Увеличиваем угол на 90 градусов
        self.rotation_angle %= 360  # Ограничиваем угол в пределах 0-359
        self.update_image()  # Обновляем изображение

    # def resizeEvent(self, event):
    #     if self.current_image_path:  # Проверяем, если изображение уже загружено
    #         pixmap = QtGui.QPixmap(self.current_image_path)
    #         label_size = self.label_image.size()
    #         scaled_pixmap = pixmap.scaled(label_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    #         self.label_image.setPixmap(scaled_pixmap)

    def add_tab(self):
        """Метод добавления вкладки с кнопкой удаления (тип: Деталь)"""
        self.add_custom_tab("Деталь")

    def add_assembly_unit(self):
        """Метод добавления вкладки с кнопкой удаления (тип: Сборочная единица)"""
        self.add_custom_tab("Сборочная единица")

    def add_custom_tab(self, tab_name):
        """Общий метод добавления новой вкладки с кастомным заголовком"""
        tab_name = self.ui.lineEditItemName.text().strip() or tab_name

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/utils/icons/plus-square-dotted.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        tab_detail = QtWidgets.QWidget()

        tab_detail.setObjectName("tab_detail")
        gridLayout_7 = QtWidgets.QGridLayout(tab_detail)
        gridLayout_7.setContentsMargins(0, 15, 10, 0)  # Отступы слева, сверху, справа и снизу
        gridLayout_7.setSpacing(0)  # Расстояние между виджетами внутри макета
        gridLayout_7.setObjectName("gridLayout_7")
        gridLayout_6 = QtWidgets.QGridLayout()
        gridLayout_6.setObjectName("gridLayout_6")
        checkBoxBelongingToAnAssemblyUnit = QtWidgets.QCheckBox("Принадлежность к сборочной единице:", tab_detail)
        checkBoxBelongingToAnAssemblyUnit.setObjectName("checkBoxBelongingToAnAssemblyUnit")
        gridLayout_6.addWidget(checkBoxBelongingToAnAssemblyUnit, 1, 0, 1, 1)

        checkBoxBelongingToAnAssemblyUnit.setObjectName("checkBoxBelongingToAnAssemblyUnit")
        # self.gridLayout_6.addWidget(self.labelBelongingToAnAssemblyUnit_2, 1, 0, 1, 1)
        radioButtonUnit_1_2 = QtWidgets.QRadioButton(tab_detail)
        font = QtGui.QFont()
        font.setPointSize(12)
        radioButtonUnit_1_2.setFont(font)
        radioButtonUnit_1_2.setObjectName("radioButtonUnit_1_2")
        gridLayout_6.addWidget(radioButtonUnit_1_2, 3, 0, 1, 1)

        radioButtonUnit_2_2 = QtWidgets.QRadioButton(tab_detail)
        font = QtGui.QFont()
        font.setPointSize(12)
        radioButtonUnit_2_2.setFont(font)
        radioButtonUnit_2_2.setObjectName("radioButtonUnit_2_2")
        gridLayout_6.addWidget(radioButtonUnit_2_2, 2, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        gridLayout_6.addItem(spacerItem, 4, 0, 1, 1)

        BtnAddSheet_2 = QtWidgets.QPushButton(tab_detail)
        BtnAddSheet_2.setIcon(icon2)
        BtnAddSheet_2.setObjectName("BtnAddSheet_2")
        BtnAddSheet_2.setFixedWidth(120)
        gridLayout_6.addWidget(BtnAddSheet_2, 1, 3, 1, 1)

        tabWidget_2 = QtWidgets.QTabWidget(tab_detail)
        tabWidget_2.setObjectName("tabWidget_2")
        tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(tab.sizePolicy().hasHeightForWidth())
        tab.setSizePolicy(sizePolicy)
        tab.setObjectName("tab")
        gridLayout_11 = QtWidgets.QGridLayout(tab)
        gridLayout_11.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        gridLayout_11.setContentsMargins(9, -1, -1, -1)
        gridLayout_11.setObjectName("gridLayout_11")

        BtnPrintDesignFile = QtWidgets.QPushButton(tab)
        BtnPrintDesignFile.setToolTipDuration(3000)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/utils/icons/folder2-open.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        # self.BtnPrintDesignFile.setIcon(icon1)
        # self.BtnPrintDesignFile.setIconSize(QtCore.QSize(20, 20))
        BtnPrintDesignFile.setText("Печать")
        gridLayout_11.addWidget(BtnPrintDesignFile, 3, 5, 1, 1)

        BtnOpenDesignFile_2 = QtWidgets.QPushButton(tab)
        BtnOpenDesignFile_2.setToolTipDuration(3000)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/utils/icons/folder2-open.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        BtnOpenDesignFile_2.setIcon(icon1)
        BtnOpenDesignFile_2.setIconSize(QtCore.QSize(20, 20))
        BtnOpenDesignFile_2.setObjectName("BtnOpenDesignFile_2")
        gridLayout_11.addWidget(BtnOpenDesignFile_2, 3, 6, 1, 1)

        labelMass_2 = QtWidgets.QLabel(tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        labelMass_2.setFont(font)
        labelMass_2.setToolTipDuration(3000)
        labelMass_2.setObjectName("labelMass_2")
        labelMass_2.setText("Масса детали, кг")
        gridLayout_11.addWidget(labelMass_2, 3, 0, 1, 1)

        BtnRotateLeft = QtWidgets.QPushButton(tab)
        BtnRotateLeft.setToolTipDuration(3000)
        BtnRotateLeft.setAutoFillBackground(False)
        BtnRotateLeft.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/utils/icons/icons8_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BtnRotateLeft.setIcon(icon3)
        BtnRotateLeft.setIconSize(QtCore.QSize(25, 25))
        BtnRotateLeft.setObjectName("BtnRotateLeft_2")
        gridLayout_11.addWidget(BtnRotateLeft, 3, 3, 1, 1)

        BtnRotateRight = QtWidgets.QPushButton(tab)
        BtnRotateRight.setToolTipDuration(3000)
        BtnRotateRight.setAutoFillBackground(False)
        BtnRotateRight.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/utils/icons/icons8_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BtnRotateRight.setIcon(icon4)
        BtnRotateRight.setIconSize(QtCore.QSize(25, 25))
        BtnRotateRight.setObjectName("pushButton_9")
        gridLayout_11.addWidget(BtnRotateRight, 3, 4, 1, 1)

        lineEditMass_3 = QtWidgets.QLineEdit(tab)
        lineEditMass_3.setText("")
        lineEditMass_3.setObjectName("lineEditMass_3")
        gridLayout_11.addWidget(lineEditMass_3, 3, 1, 1, 1)
        BtnDeleteSheet_2 = QtWidgets.QPushButton(tab)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/utils/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BtnDeleteSheet_2.setIcon(icon5)
        BtnDeleteSheet_2.setObjectName("BtnDeleteSheet_2")
        gridLayout_11.addWidget(BtnDeleteSheet_2, 3, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        gridLayout_11.addItem(spacerItem1, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        gridLayout_11.addItem(spacerItem2, 3, 5, 1, 1)

        self.label_image = QtWidgets.QLabel(tab)
        self.label_image.setText("")
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        gridLayout_11.addWidget(self.label_image, 0, 0, 1, 8)

        tabWidget_2.addTab(tab, "")
        gridLayout_6.addWidget(tabWidget_2, 2, 2, 3, 2)
        gridLayout_7.addLayout(gridLayout_6, 0, 0, 1, 1)
        # tabWidget.addTab(tab_detail, "")

        BtnOpenDesignFile_2.clicked.connect(self.open_file)
        BtnPrintDesignFile.clicked.connect(self.open_printer_window)
        BtnRotateLeft.clicked.connect(self.rotate_left)
        BtnRotateRight.clicked.connect(self.rotate_right)

        # Лейбл для имени вкладки
        self.label_title = QtWidgets.QLabel(tab_name)
        # font = QtGui.QFont()
        # font.setPointSize(18)  # Устанавливаем размер шрифта 12 pt
        # self.label_title.setFont(font)  # Применяем шрифт к лейблу
        self.label_title.setStyleSheet("font-size: 18pt;")
        gridLayout_6.addWidget(self.label_title, 1, 2, 1, 1)


        # Добавляем вкладку в TabWidget
        index = self.ui.tabWidget.addTab(tab_detail, "")  # Добавляем вкладку без названия
        self.add_close_button(index, tab_name)  # Устанавливаем кастомный заголовок

        # Устанавливаем только что добавленную вкладку активной
        self.ui.tabWidget.setCurrentIndex(index)

        self.ui.lineEditItemName.clear()  # Очищаем поле ввода для следующей вкладки

    def on_button_click(self):
        """Обработчик для кнопки"""
        print("Кнопка была нажата!")

    def add_close_button(self, index, tab_name):
        """Добавляет кастомный заголовок с текстом и кнопкой удаления"""
        tab_header = QtWidgets.QWidget()
        tab_header_layout = QtWidgets.QHBoxLayout(tab_header)
        tab_header_layout.setContentsMargins(0, 0, 0, 0)

        # Добавляем текст заголовка
        label = QtWidgets.QLabel(tab_name)
        tab_header_layout.addWidget(label)

        # Добавляем кнопку удаления
        if index not in self.protected_tabs:  # Только для незашищённых вкладок
            close_button = QtWidgets.QPushButton("×")
            close_button.setFixedSize(20, 20)  # Устанавливаем размер кнопки
            close_button.setStyleSheet("""
                QPushButton {
                    border: none;
                    color: red;
                    font-weight: bold;
                    font-size: 14px;
                    width: 20px;
                    height: 20px;
                    text-align: center;
                    padding: 0;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            close_button.clicked.connect(self.handle_remove_tab)
            tab_header_layout.addWidget(close_button)

        self.ui.tabWidget.tabBar().setTabButton(index, QtWidgets.QTabBar.RightSide, tab_header)

    def handle_remove_tab(self):
        sender = self.sender()  # Определяем, какая кнопка вызвала сигнал
        self.remove_tab_by_widget(sender)

    def save_tab_name(self):
        """Метод изменения названия текущей вкладки"""
        current_index = self.ui.tabWidget.currentIndex()
        if current_index in self.protected_tabs:
            print(f"Вкладка с индексом {current_index} защищена от изменения названия")
            return

        new_name = self.ui.lineEditItemName.text().strip()
        if new_name:
            # Обновляем текст в кастомном заголовке
            tab_header = self.ui.tabWidget.tabBar().tabButton(current_index, QtWidgets.QTabBar.RightSide)
            label = tab_header.findChild(QtWidgets.QLabel)
            if label:
                label.setText(new_name)
                self.label_title.setText(new_name)
            print(f"Название вкладки с индексом {current_index} изменено на '{new_name}'")
        else:
            print("Название не может быть пустым")

    def remove_tab_by_widget(self, close_button):
        """Удаляет вкладку по нажатию на кнопку удаления"""
        tab_header = close_button.parentWidget()  # Получаем виджет заголовка вкладки
        index = self.ui.tabWidget.tabBar().tabAt(tab_header.pos())  # Определяем индекс вкладки

        if index != -1:  # Проверяем, что индекс корректный
            self.ui.tabWidget.removeTab(index)  # Удаляем вкладку
            tab_header.deleteLater()  # Удаляем заголовок вкладки
            print(f"Вкладка с индексом {index} удалена")

    def open_printer_window(self):
        """Метод для открытия окна печати с выбранным изображением"""
        if not hasattr(self, 'current_image_path') or not self.current_image_path:
            print("Нет изображения для печати")
            return

        from printer import PrintDialog  # Импортируем внутри метода для избежания циклического импорта
        self.printer_window = PrintDialog(self.current_image_path)  # Передаём путь к файлу
        self.printer_window.finished.connect(self.on_print_finished)

        print("Окно печати открыто")
        self.printer_window.show()

    def on_print_finished(self):
        """Метод, вызываемый после завершения печати"""
        try:
            print("Печать завершена, закрываю окно...")
            self.printer_window.close()
            QtWidgets.QMessageBox.information(self, "Успех", "Документ успешно отправлен на печать.")
        except Exception as e:
            print(f"Ошибка при закрытии окна печати: {e}")
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {e}")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignDocumentFillingForm()
    window.show()
    sys.exit(app.exec_())








# def open_file(self):
#     # Открываем диалог для выбора файла
#     file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*.*)")
#
#     if file_path:  # Если файл выбран
#         print(f"Выбранный файл: {file_path}")
#         os.startfile(file_path)  # Открываем файл с помощью системного приложения (Windows)


