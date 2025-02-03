from PyQt5.QtWidgets import QDialog, QMessageBox, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import Qt


class PrintDialog(QDialog):
    """Диалоговое окно печати с выводом результата."""

    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.setWindowTitle("Печать чертежа")

        # ✅ Вызываем печать сразу
        self.init_ui()
        self.print_image()

    def init_ui(self):
        """Создаёт интерфейс."""
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Идёт печать...")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def print_image(self):
        """Открывает диалог печати и отображает результат."""
        printer = QPrinter()
        print_dialog = QPrintDialog(printer, self)

        if print_dialog.exec_() == QPrintDialog.Accepted:
            pixmap = QPixmap(self.image_path)
            if pixmap.isNull():
                self.label.setText("❌ Ошибка: Невозможно загрузить изображение!")
                return

            painter = QPainter(printer)
            rect = printer.pageRect()
            scaled_pixmap = pixmap.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            x_offset = (rect.width() - scaled_pixmap.width()) // 2
            y_offset = (rect.height() - scaled_pixmap.height()) // 2

            painter.drawPixmap(x_offset, y_offset, scaled_pixmap)
            painter.end()

            self.label.setText("✅ Чертёж успешно отправлен на печать!")  # ✅ Меняем текст в окне
        else:
            self.label.setText("❌ Печать отменена.")  # ❌ Показываем, что пользователь отменил печать


