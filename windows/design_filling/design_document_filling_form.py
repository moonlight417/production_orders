import sys, os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "e:/Programming/production_orders/")))
# # from windows.design_filling.tags_tab_content import TagsTabContent
from .main_tab_widget import MainTabWidget
from .gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

# from custom_tab_widget import CustomTabWidget
from PyQt5 import QtWidgets


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
        self.ui.BtnSave.clicked.connect(self.main_tab_widget.save_all_tabs_to_database)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignDocumentFillingForm()
    window.show()
    sys.exit(app.exec_())


