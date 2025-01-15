import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from main_tab_widget import MainTabWidget
# from custom_tab_widget import CustomTabWidget
from PyQt5 import QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm

import resources_rc

class DesignDocumentFillingForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DesignDocumentFillingForm()
        self.ui.setupUi(self)

        # Создаем основной виджет с двумя уровнями вкладок и добавляем его в gridLayout
        self.main_tab_widget = MainTabWidget()
        self.ui.gridLayout.addWidget(self.main_tab_widget, 0, 0, 1, 1)

        # Подключаем кнопки
        # self.ui.BtnEditTabName.clicked.connect(self.rename_current_tab)
        # self.ui.BtnAddDetail.clicked.connect(self.add_detail_tab)
        # self.ui.BtnAddAssemblyUnit.clicked.connect(self.add_assembly_unit_tab)
        # self.ui.BtnDelCurrentTab.clicked.connect(self.close_current_tab)

    def rename_current_tab(self):
        """Метод для вызова окна изменения названия текущей вкладки."""
        self.new.main_tab_widget.rename_tab()

    def add_detail_tab(self):
        """Метод для вызова окна добавления вкладки 'Деталь'."""
        self.new.main_tab_widget.add_detail_tab()

    def add_assembly_unit_tab(self):
        """Метод для вызова окна добавления вкладки 'Сборочная единица'."""
        self.new.main_tab_widget.add_assembly_unit_tab()

    def close_current_tab(self):
        """Метод для закрытия текущей вкладки."""
        self.new.main_tab_widget.main_tab_widget.close_current_tab()  # Здесь вызываем метод у вложенного CustomTabWidget


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignDocumentFillingForm()
    window.show()
    sys.exit(app.exec_())


