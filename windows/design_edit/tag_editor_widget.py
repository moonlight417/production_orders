from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout

from products.models import Tag


class TagEditorWidget(QWidget):
    def __init__(self, document):
        super().__init__()
        self.document = document
        self.setup_ui()
        self.load_tags()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.tag_container = QWidget()
        self.tag_layout = QVBoxLayout(self.tag_container)

        self.btn_add = QPushButton("Добавить тег")
        self.btn_add.clicked.connect(self.add_tag_field)

        self.layout.addWidget(self.tag_container)
        self.layout.addWidget(self.btn_add)

    def add_tag_field(self, text=""):
        row = QWidget()
        layout = QHBoxLayout(row)

        edit = QLineEdit(text)
        btn_remove = QPushButton("×")
        btn_remove.clicked.connect(lambda: self.remove_tag(row))

        layout.addWidget(edit)
        layout.addWidget(btn_remove)
        self.tag_layout.addWidget(row)

    def remove_tag(self, row):
        row.deleteLater()

    def load_tags(self):
        for tag in self.document.tags.all():
            self.add_tag_field(tag.name)

    def save_tags(self):
        new_tags = []
        for i in range(self.tag_layout.count()):
            row = self.tag_layout.itemAt(i).widget()
            text = row.findChild(QLineEdit).text().strip()
            if text:
                tag, _ = Tag.objects.get_or_create(name=text)
                new_tags.append(tag)

        self.document.tags.set(new_tags)