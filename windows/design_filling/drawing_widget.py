from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize
from .print_dialog import PrintDialog

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap()
        self.current_angle = 0
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)
        button_panel = QVBoxLayout()
        load_button = QPushButton("Загрузить изображение")
        load_button.clicked.connect(self.open_file)
        print_button = QPushButton("Печать изображения")
        print_button.clicked.connect(self.open_printer_window)
        rotate_left_button = QPushButton("Повернуть влево")
        rotate_left_button.clicked.connect(self.rotate_left)
        rotate_right_button = QPushButton("Повернуть вправо")
        rotate_right_button.clicked.connect(self.rotate_right)

        button_panel.addWidget(load_button)
        button_panel.addWidget(print_button)
        button_panel.addWidget(rotate_left_button)
        button_panel.addWidget(rotate_right_button)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_panel.addSpacerItem(spacer)

        layout.addLayout(button_panel)
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "../utils/drawings/", "Изображения (*.png *.jpg *.bmp *.gif)")
        if file_path:
            self.pixmap = QPixmap(file_path)
            self.current_angle = 0
            self.update_image()
            self.current_image_path = file_path

    def rotate_right(self):
        if not self.pixmap.isNull():
            self.current_angle = (self.current_angle + 90) % 360
            self.update_image()

    def rotate_left(self):
        if not self.pixmap.isNull():
            self.current_angle = (self.current_angle - 90) % 360
            self.update_image()

    def update_image(self):
        if not self.pixmap.isNull():
            transform = QTransform().rotate(self.current_angle)
            rotated_pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
            fixed_size = QSize(500, 500)
            scaled_pixmap = rotated_pixmap.scaled(fixed_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

    def open_printer_window(self):
        if not hasattr(self, 'current_image_path') or not self.current_image_path:
            QMessageBox.warning(self, "Предупреждение", "Нет изображения для печати.")
            return
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.show()
