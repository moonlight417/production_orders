from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
import sys
import os

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
        self.ui.BtnAddDetail.clicked.connect(self.add_tab)

    def open_file(self):
        """Метод открытия файла"""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "../utils/drawings/",
                                                             "Изображения (*.png *.jpg *.bmp *.gif)")

        if file_path:
            pixmap = QtGui.QPixmap(file_path)
            self.ui.label_image.setPixmap(pixmap)
            print(f"Выбранное изображение: {file_path}")

    def add_tab(self):
        """Метод добавления новой вкладки с возможностью редактирования названия"""
        tab_name = self.ui.lineEditItemName.text().strip()
        if not tab_name:
            tab_name = f"Вкладка {self.ui.tabWidget.count() + 1}"

        new_tab = QtWidgets.QWidget()  # Создаём новый виджет для вкладки
        new_tab_layout = QtWidgets.QVBoxLayout(new_tab)
        label = QtWidgets.QLabel(f"Это вкладка с названием: {tab_name}")
        new_tab_layout.addWidget(label)

        index = self.ui.tabWidget.addTab(new_tab, "")  # Добавляем вкладку с пустым названием
        self.set_tab_header(index, tab_name)

        self.ui.lineEditItemName.clear()

    def set_tab_header(self, index, tab_name):
        """Метод создания кастомного заголовка вкладки с редактируемым названием"""
        tab_header = QtWidgets.QWidget()
        tab_header_layout = QtWidgets.QHBoxLayout(tab_header)
        tab_header_layout.setContentsMargins(0, 0, 0, 0)

        # QLineEdit, которое будет отображать название вкладки
        line_edit = QtWidgets.QLineEdit(tab_name)
        line_edit.setReadOnly(True)  # Устанавливаем QLineEdit как только для чтения
        line_edit.setStyleSheet("border: none; background-color: transparent;")  # Стиль без рамки
        line_edit.setAlignment(QtCore.Qt.AlignCenter)  # Центрируем текст
        tab_header_layout.addWidget(line_edit)

        # Кнопка удаления
        close_button = QtWidgets.QPushButton("×")
        close_button.setFixedSize(16, 16)
        close_button.setStyleSheet("border: none;")
        close_button.clicked.connect(lambda: self.remove_tab_by_widget(close_button))
        tab_header_layout.addWidget(close_button)

        # Устанавливаем кастомный заголовок для вкладки
        self.ui.tabWidget.tabBar().setTabButton(index, QtWidgets.QTabBar.LeftSide, tab_header)

        # Связываем изменение состояния активной вкладки с редактированием названия
        self.ui.tabWidget.currentChanged.connect(lambda: self.update_tab_name(line_edit))

    def update_tab_name(self, line_edit):
        """Метод для переключения состояния QLineEdit на QLabel"""
        current_index = self.ui.tabWidget.currentIndex()

        # Проверяем, активна ли текущая вкладка
        if self.ui.tabWidget.indexOf(line_edit.parent()) == current_index:
            line_edit.setReadOnly(False)  # Если вкладка активна, разрешаем редактирование
        else:
            line_edit.setReadOnly(True)  # Если вкладка не активна, делаем QLineEdit только для чтения

    def remove_tab_by_widget(self, close_button):
        """Метод удаления вкладки по кнопке удаления"""
        tab_header = close_button.parentWidget()
        tab_bar = self.ui.tabWidget.tabBar()
        index = tab_bar.tabAt(tab_header.pos())  # Определяем индекс вкладки по позиции заголовка

        if index != -1 and index not in self.protected_tabs:  # Проверяем, что индекс корректный и вкладка не защищена
            self.ui.tabWidget.removeTab(index)
            print(f"Вкладка с индексом {index} удалена")
        elif index in self.protected_tabs:
            print(f"Вкладка с индексом {index} защищена от удаления")


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


