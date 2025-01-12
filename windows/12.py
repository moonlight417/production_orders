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


class DrawingWidget(QWidget):
    """Виджет для работы с изображением (загрузка, поворот, печать)."""

    def __init__(self):
        super().__init__()
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap()
        self.current_angle = 0

        layout = QVBoxLayout(self)
        self.load_button = QPushButton("Load Image")
        self.load_button.clicked.connect(self.open_file)
        self.print_button = QPushButton("Print Image")
        self.print_button.clicked.connect(self.open_printer_window)

        layout.addWidget(self.load_button)
        layout.addWidget(self.print_button)
        layout.addWidget(self.image_label)

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
            label_size = self.image_label.size()
            scaled_pixmap = rotated_pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

    def open_printer_window(self):
        if not hasattr(self, 'current_image_path') or not self.current_image_path:
            QMessageBox.warning(self, "Ошибка", "Нет изображения для печати")
            return
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.show()


class InnerTabWidget(QWidget):
    """Виджет с вложенным QTabWidget для каждой верхней вкладки."""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.inner_tab_widget = QTabWidget()
        self.add_tab_button = QPushButton("Add Inner Tab")
        self.add_tab_button.clicked.connect(self.add_inner_tab)

        layout.addWidget(self.inner_tab_widget)
        layout.addWidget(self.add_tab_button)

        self.add_inner_tab()

    def add_inner_tab(self):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        drawing_widget = DrawingWidget()
        rotate_left_btn = QPushButton("Rotate Left")
        rotate_right_btn = QPushButton("Rotate Right")

        rotate_left_btn.clicked.connect(drawing_widget.rotate_left)
        rotate_right_btn.clicked.connect(drawing_widget.rotate_right)

        tab_layout.addWidget(drawing_widget)
        tab_layout.addWidget(rotate_left_btn)
        tab_layout.addWidget(rotate_right_btn)

        tab_name = f"Inner Tab {self.inner_tab_widget.count() + 1}"
        self.inner_tab_widget.addTab(tab, tab_name)


class MainTabWidget(QMainWindow):
    """Главное окно с верхним уровнем вкладок."""

    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.main_tab_widget = QTabWidget()

        self.add_detail_button = QPushButton("Add Detail Tab")
        self.add_detail_button.clicked.connect(self.add_detail_tab)

        self.add_assembly_unit_button = QPushButton("Add Assembly Unit Tab")
        self.add_assembly_unit_button.clicked.connect(self.add_assembly_unit_tab)

        layout.addWidget(self.main_tab_widget)
        layout.addWidget(self.add_detail_button)
        layout.addWidget(self.add_assembly_unit_button)
        self.setCentralWidget(central_widget)

    def add_detail_tab(self):
        tab = InnerTabWidget()
        self.main_tab_widget.addTab(tab, "Деталь")

    def add_assembly_unit_tab(self):
        tab = InnerTabWidget()
        self.main_tab_widget.addTab(tab, "Сборочная единица")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainTabWidget()
    main_window.show()
    sys.exit(app.exec_())
