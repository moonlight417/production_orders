from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel, QMessageBox, QDialog
from custom_tab_widget import CustomTabWidget
from structure_tab_content import StructureTabContent
from tags_tab_content import TagsTabContent
from inner_tab_widget import InnerTabWidget
from rename_tab_dialog import RenameTabDialog

class MainTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.main_tab_widget = CustomTabWidget()
        layout.addWidget(self.main_tab_widget)
        self.scroll_areas = {}
        self.add_protected_tabs()

    def add_protected_tabs(self):
        # # Вкладка "Структура"
        # structure_tab = StructureTabContent()
        # self.main_tab_widget.addTab(structure_tab, "Структура")

        # Вкладка "Теги"
        tags_tab = TagsTabContent()
        self.main_tab_widget.addTab(tags_tab, "Теги")

        # Добавляем защищенные вкладки
        self.main_tab_widget.protected_tabs = 0  # Индексы вкладок "Структура" и "Теги"

    def add_detail_tab(self):
        tab = InnerTabWidget()
        self.main_tab_widget.addTab(tab, "Деталь")
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

    def add_assembly_unit_tab(self):
        tab = InnerTabWidget()
        tab_name = f"Сборочная единица {self.main_tab_widget.count() + 1}"
        self.main_tab_widget.addTab(tab, tab_name)
        new_index = self.main_tab_widget.count() - 1
        self.main_tab_widget.setCurrentIndex(new_index)

    def rename_tab(self):
        current_index = self.main_tab_widget.currentIndex()
        if current_index == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите вкладку для изменения названия.")
            return

        if current_index == 0:
            QMessageBox.warning(self, "Предупреждение", "Нельзя изменить название защищенной вкладки.")
            return

        current_name = self.main_tab_widget.tabText(current_index)
        dialog = RenameTabDialog(current_name, self)

        if dialog.exec_() == QDialog.Accepted:
            new_name = dialog.get_new_name()
            if new_name:
                self.main_tab_widget.setTabText(current_index, new_name)
            else:
                QMessageBox.warning(self, "Предупреждение", "Название не может быть пустым.")
