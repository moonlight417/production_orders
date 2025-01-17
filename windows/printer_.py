
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter, QPixmap

import sys

class PrintDialog(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.init_ui()

    def init_ui(self):
        """Инициализация окна печати."""
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)

        if print_dialog.exec_() == QPrintDialog.Accepted:
            self.print_image(printer)

    def print_image(self, printer):
        """Печать изображения на выбранном принтере."""
        pixmap = QPixmap(self.image_path)

        if pixmap.isNull():
            print("Ошибка: невозможно загрузить изображение")
            return

        painter = QPainter(printer)
        try:
            # Масштабируем изображение под размер страницы
            rect = printer.pageRect()
            scaled_pixmap = pixmap.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            painter.drawPixmap(rect, scaled_pixmap)
        finally:
            painter.end()  # Обязательно завершаем работу с painter
            self.close()



# Пример вызова (замените 'path/to/image.png' на путь к вашему изображению)
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     image_path = "path/to/image.png"  # Укажите путь к изображению
#     print_dialog = PrintDialog(image_path)
#     sys.exit(app.exec_())
