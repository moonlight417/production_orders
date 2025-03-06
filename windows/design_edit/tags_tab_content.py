from PyQt5 import QtWidgets, QtCore
from products.models import Tag, MainDocument


class TagsTabContent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)

        self.add_tag_button = QtWidgets.QPushButton("Добавить тег")
        self.add_tag_button.clicked.connect(self.add_tag_input)

        layout.addWidget(self.scroll_area)
        layout.addWidget(self.add_tag_button)

        self.tag_inputs = []

    def add_tag_input(self):
        tag_layout = QtWidgets.QHBoxLayout()
        tag_input = QtWidgets.QLineEdit()
        delete_button = QtWidgets.QPushButton("Удалить")

        tag_layout.addWidget(tag_input)
        tag_layout.addWidget(delete_button)
        self.scroll_layout.addLayout(tag_layout)

        delete_button.clicked.connect(lambda: self.remove_tag_input(tag_layout))
        self.tag_inputs.append(tag_input)

    def remove_tag_input(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.scroll_layout.removeItem(layout)

    def load_tags_from_db(self, main_id):
        try:
            document = MainDocument.objects.get(id=main_id)
            for tag in document.tags.all():
                self.add_tag_input()
                self.tag_inputs[-1].setText(tag.name)
        except MainDocument.DoesNotExist:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Документ не найден!")

    def get_tag_list(self):
        return [tag_input.text() for tag_input in self.tag_inputs if tag_input.text()]




