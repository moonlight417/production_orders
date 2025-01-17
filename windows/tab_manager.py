from PyQt5 import QtWidgets

class TabManager:
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.protected_tabs = []

    def add_tab_detail(self):
        self.add_custom_tab("Деталь")

    def add_tab_assembly_unit(self):
        self.add_custom_tab("Сборочная единица")

    def add_custom_tab(self, tab_name):
        new_tab = QtWidgets.QWidget()
        index = self.tab_widget.addTab(new_tab, tab_name)
        self.tab_widget.setCurrentIndex(index)

    def save_tab_name(self):
        current_index = self.tab_widget.currentIndex()
        if current_index in self.protected_tabs:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Нельзя изменять название этой вкладки!")
            return
        new_name, ok = QtWidgets.QInputDialog.getText(None, "Изменить название", "Новое название:")
        if ok and new_name:
            self.tab_widget.setTabText(current_index, new_name)
