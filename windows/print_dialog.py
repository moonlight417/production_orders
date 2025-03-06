# print_dialog.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QScrollArea, QMessageBox, QSlider
from PyQt5.QtGui import QPixmap, QPainter, QTransform
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import Qt, QRectF

class PrintDialog(QDialog):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Печать чертежа")
        self.pixmap = pixmap  # Исходное изображение

        # Основной layout
        main_layout = QVBoxLayout(self)

        # Кнопки управления печатью
        control_layout = QHBoxLayout()

        # Кнопка поворота влево
        self.rotate_left_button = QPushButton("↺ Повернуть влево")
        self.rotate_left_button.clicked.connect(self.rotate_left)
        control_layout.addWidget(self.rotate_left_button)

        # Кнопка поворота вправо
        self.rotate_right_button = QPushButton("↻ Повернуть вправо")
        self.rotate_right_button.clicked.connect(self.rotate_right)
        control_layout.addWidget(self.rotate_right_button)

        # Слайдер для масштабирования
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(50)  # 50% масштаб
        self.scale_slider.setMaximum(200)  # 200% масштаб
        self.scale_slider.setValue(100)  # Начальное значение 100%
        self.scale_slider.valueChanged.connect(self.scale_image)
        control_layout.addWidget(QLabel("Масштаб:"))
        control_layout.addWidget(self.scale_slider)

        main_layout.addLayout(control_layout)

        # Кнопка печати
        self.print_button = QPushButton("🖨 Печать")
        self.print_button.clicked.connect(self.print_image)
        main_layout.addWidget(self.print_button)

        self.setLayout(main_layout)

    def rotate_left(self):
        """Поворачивает изображение на 90 градусов влево."""
        self.current_angle -= 90
        self.update_image()

    def rotate_right(self):
        """Поворачивает изображение на 90 градусов вправо."""
        self.current_angle += 90
        self.update_image()

    def scale_image(self):
        """Масштабирует изображение."""
        self.scale_factor = self.scale_slider.value() / 100.0
        self.update_image()

    def update_image(self):
        """Обновляет изображение с учетом поворота и масштабирования."""
        transform = QTransform().rotate(self.current_angle)
        scaled_pixmap = self.pixmap.scaled(
            self.pixmap.size() * self.scale_factor,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.rotated_pixmap = scaled_pixmap.transformed(transform, Qt.SmoothTransformation)
        self.image_label.setPixmap(self.rotated_pixmap)

    def print_image(self):
        """Печатает изображение с выбором принтера."""
        printer = QPrinter(QPrinter.HighResolution)
        print_dialog = QPrintDialog(printer, self)

        if print_dialog.exec_() == QPrintDialog.Accepted:
            try:
                painter = QPainter(printer)
                if not painter.begin(printer):
                    QMessageBox.warning(self, "Ошибка", "Не удалось подключиться к принтеру.")
                    return

                # Масштабируем изображение под размер страницы
                page_rect = printer.pageRect(QPrinter.DevicePixel)
                image_rect = QRectF(self.rotated_pixmap.rect())

                # Рисуем изображение на принтере
                painter.drawPixmap(page_rect, self.rotated_pixmap, image_rect)
                painter.end()

                QMessageBox.information(self, "Успех", "Чертёж отправлен на печать!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при печати: {str(e)}")