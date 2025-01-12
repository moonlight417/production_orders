from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
from image_handler import ImageHandler
from tab_manager import TabManager
from printer import PrintDialog
import sys

class DesignDocumentFillingForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DesignDocumentFillingForm()
        self.ui.setupUi(self)

        # Обработчик изображений
        self.image_handler = ImageHandler(self.ui)

        # Управление вкладками
        self.tab_manager = TabManager(self.ui.tabWidget)

        # Подключение кнопок
        self.ui.BtnAddDetail.clicked.connect(self.tab_manager.add_tab_detail)
        self.ui.BtnAddAssemblyUnit.clicked.connect(self.tab_manager.add_tab_assembly_unit)
        self.ui.BtnEditTabName.clicked.connect(self.tab_manager.save_tab_name)
        # self.ui.BtnOpenFile.clicked.connect(self.image_handler.open_file)
        # self.ui.BtnRotateLeft.clicked.connect(self.image_handler.rotate_left)
        # self.ui.BtnRotateRight.clicked.connect(self.image_handler.rotate_right)

    def open_printer_window(self):
        """Открытие окна печати"""
        if not self.image_handler.current_image_path:
            QtWidgets.QMessageBox.warning(self, "Внимание", "Изображение не выбрано!")
            return
        printer_window = PrintDialog(self.image_handler.current_image_path)
        printer_window.finished.connect(self.on_print_finished)
        printer_window.show()

    def on_print_finished(self):
        """Завершение печати"""
        QtWidgets.QMessageBox.information(self, "Успех", "Документ успешно отправлен на печать.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignDocumentFillingForm()
    window.show()
    sys.exit(app.exec_())