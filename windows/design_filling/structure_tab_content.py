from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea

class StructureTabContent(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        for i in range(50):
            label = QLabel(f"Элемент структуры {i + 1}")
            scroll_layout.addWidget(label)

        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)
        self.setLayout(layout)
