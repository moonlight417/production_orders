from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QFileDialog, QMessageBox, QCheckBox, QLineEdit
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
        # Основной горизонтальный лэйаут
        layout = QHBoxLayout(self)

        # Лэйаут для панели кнопок
        button_panel = QVBoxLayout()

        # Создаем кнопки
        load_button = QPushButton("Загрузить изображение")
        load_button.setFixedWidth(180)
        load_button.clicked.connect(self.open_file)

        print_button = QPushButton("Печать изображения")
        print_button.setFixedWidth(180)
        print_button.clicked.connect(self.open_printer_window)

        rotate_left_button = QPushButton("Повернуть влево")
        rotate_left_button.setFixedWidth(180)
        rotate_left_button.clicked.connect(self.rotate_left)

        rotate_right_button = QPushButton("Повернуть вправо")
        rotate_right_button.setFixedWidth(180)
        rotate_right_button.clicked.connect(self.rotate_right)

        self.lineEditMass = QLineEdit()
        self.lineEditMass.setFixedWidth(150)
        self.lineEditMass.setPlaceholderText("Масса, кг")


        check_box = QCheckBox("Актуальность документа", self)

        # Добавляем виджеты в вертикальный лэйаут
        button_panel.addWidget(load_button)
        button_panel.addWidget(print_button)
        button_panel.addWidget(rotate_left_button)
        button_panel.addWidget(rotate_right_button)
        button_panel.addStretch()
        button_panel.addWidget(self.lineEditMass)
        button_panel.addStretch()  # Создаем пространство между кнопками и чекбоксом
        button_panel.addWidget(check_box)

        # Добавляем лэйауты и элементы в основной горизонтальный лэйаут
        layout.addLayout(button_panel)
        layout.addWidget(self.image_label)

        # Устанавливаем лэйаут для окна
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
