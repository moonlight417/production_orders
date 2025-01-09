from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
import sys

class DesignDocumentFillingForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DesignDocumentFillingForm()
        self.ui.setupUi(self)

        # Список защищённых вкладок по индексам
        self.protected_tabs = [self.ui.tabWidget.indexOf(self.ui.tab_struct),
                               self.ui.tabWidget.indexOf(self.ui.tab_tags)]

        # Подключаем кнопки
        self.ui.BtnOpenDesignFile_2.clicked.connect(self.open_file)
        self.ui.BtnAddDetail.clicked.connect(self.add_tab)  # Добавление вкладки "Деталь"
        self.ui.BtnAddAssemblyUnit.clicked.connect(self.add_assembly_unit)  # Добавление вкладки "Сборочная единица"
        self.ui.BtnSaveTabName.clicked.connect(self.save_tab_name)

    def open_file(self):
        """Метод открытия файла"""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "../utils/drawings/",
                                                             "Изображения (*.png *.jpg *.bmp *.gif)")

        if file_path:
            pixmap = QtGui.QPixmap(file_path)

            # Получаем размеры области (label), в которую вставляется изображение
            label_size = self.ui.label_image.size()

            # Если область слишком маленькая, можно принудительно установить минимальные размеры
            if label_size.width() == 0 or label_size.height() == 0:
                label_size = self.ui.label_image.minimumSize()  # Можно установить другие значения

            # Масштабируем изображение с сохранением пропорций
            scaled_pixmap = pixmap.scaled(label_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

            # Устанавливаем масштабированное изображение
            self.ui.label_image.setPixmap(scaled_pixmap)

            print(f"Выбранное изображение: {file_path}")

    def add_tab(self):
        """Метод добавления вкладки с кнопкой удаления (тип: Деталь)"""
        self.add_custom_tab("Деталь")

    def add_assembly_unit(self):
        """Метод добавления вкладки с кнопкой удаления (тип: Сборочная единица)"""
        self.add_custom_tab("Сборочная единица")

    def add_custom_tab(self, tab_name):
        """Общий метод добавления новой вкладки с кастомным заголовком"""
        tab_name = self.ui.lineEditItemName.text().strip() or tab_name

        new_tab = QtWidgets.QWidget()  # Создаём новый виджет для вкладки
        new_tab_layout = QtWidgets.QVBoxLayout(new_tab)
        label = QtWidgets.QLabel(f"Это вкладка с названием: {tab_name}")
        new_tab_layout.addWidget(label)

        index = self.ui.tabWidget.addTab(new_tab, "")  # Добавляем вкладку без названия
        self.add_close_button(index, tab_name)  # Устанавливаем кастомный заголовок

        self.ui.lineEditItemName.clear()

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


