from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox, QDialog, QTabBar, QScrollArea, QVBoxLayout, QFrame, QCheckBox, QPushButton
from PyQt5.QtCore import Qt
from .custom_tab_widget import CustomTabWidget
from .drawing_widget import DrawingWidget
from .rename_tab_dialog import RenameTabDialog

class InnerTabWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.inner_tab_widget = CustomTabWidget()

        # checkbox = QCheckBox("Принадлежность к СБ")
        # scroll_area = QScrollArea()
        # scroll_content = QWidget()
        # scroll_layout = QVBoxLayout(scroll_content)
        # scroll_area.setWidget(scroll_content)

        add_button = QPushButton("Добавить лист")
        add_button.clicked.connect(self.add_inner_tab)

        # layout.addWidget(checkbox)
        # layout.addWidget(scroll_area)
        layout.addWidget(add_button)
        layout.addWidget(self.inner_tab_widget)
        self.setLayout(layout)

    def add_inner_tab(self):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        drawing_widget = DrawingWidget()
        tab_layout.addWidget(drawing_widget)

        self.sheet_number = self.inner_tab_widget.count() + 1

        tab_name = f"Лист {self.sheet_number}"
        self.inner_tab_widget.addTab(tab, tab_name)
