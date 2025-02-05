import sys, os

from PyQt5.QtWidgets import QStackedWidget, QMessageBox

from .main_tab_widget import MainTabWidget
from ..document_viewer import DocumentViewer
from .gui.ui_design_document_edit_form import Ui_DesignDocumentEditForm
from PyQt5 import QtWidgets
import resources_rc

class DesignDocumentEditForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_DesignDocumentEditForm()
        self.ui.setupUi(self)

        # Передаем self.ui в MainTabWidget
        self.main_tab_widget = MainTabWidget(self.ui)
        self.ui.gridLayout.addWidget(self.main_tab_widget, 0, 0, 1, 1)

        # Подключаем кнопку сохранения
        self.ui.BtnSave.clicked.connect(self.main_tab_widget.save_to_db)
        # self.comment = self.ui.textEditComments.toPlainText()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignDocumentEditForm()
    window.show()
    sys.exit(app.exec_())


