from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTabWidget, QHBoxLayout, QDialog, QMessageBox
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt

class PrintDialog(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.print_image(printer)

    def print_image(self, printer):
        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            QMessageBox.critical(self, "Ошибка", "Невозможно загрузить изображение")
            return
        painter = QPainter(printer)
        try:
            rect = printer.pageRect()
            scaled_pixmap = pixmap.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.drawPixmap(rect, scaled_pixmap)
        finally:
            painter.end()
