
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm

class DesignDocumentFillingForm(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_DesignDocumentFillingForm()
        self.ui.setupUi(self)
        self.parent = parent  # Сохраняем ссылку на родительское окно

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DesignDocumentFillingForm = QtWidgets.QMainWindow()
    ui = Ui_DesignDocumentFillingForm()
    ui.setupUi(DesignDocumentFillingForm)
    DesignDocumentFillingForm.show()
    sys.exit(app.exec_())
