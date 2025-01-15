from PyQt5.QtWidgets import QTabWidget, QMessageBox

class CustomTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def close_current_tab(self):
        index = self.currentIndex()
        if index != 0:
            self.removeTab(index)
        else:
            QMessageBox.warning(self, "Предупреждение", "Нельзя удалить защищённую вкладку.")
