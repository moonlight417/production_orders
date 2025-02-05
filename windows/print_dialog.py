import os
from PyQt5.QtWidgets import QDialog, QMessageBox, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import Qt


class PrintDialog(QDialog):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Печать чертежа")

        # Проверяем, существует ли файл
        if not os.path.exists(image_path):
            QMessageBox.warning(self, "Ошибка", "Файл не найден для печати.")
            self.reject()  # Закрыть диалог

        self.image_path = image_path
        self.pixmap = QPixmap(self.image_path)

        # Убедитесь, что изображение загружено корректно
        if self.pixmap.isNull():
            QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение для печати.")
            self.reject()

        # Создаём элемент для отображения изображения
        image_label = QLabel(self)
        image_label.setPixmap(self.pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        # Добавляем кнопку для печати
        print_button = QPushButton("Печать", self)
        print_button.clicked.connect(self.print_image)

        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget(print_button)
        self.setLayout(layout)

    def print_image(self):
        """Функция для печати изображения."""
        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)

        # Создаём QPainter для печати
        painter = QPainter(printer)

        if not painter.begin(printer):
            QMessageBox.warning(self, "Ошибка", "Не удалось подключиться к принтеру.")
            return

        # Масштабируем изображение по размеру страницы
        painter.drawPixmap(0, 0, self.pixmap.scaled(printer.pageRect().width(), printer.pageRect().height(),
                                                    Qt.KeepAspectRatio))
        painter.end()

        QMessageBox.information(self, "Печать", "Чертёж отправлен на печать!")
        self.accept()  # Закрыть диалог после печати



