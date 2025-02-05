from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFrame, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt

class TagsTabContent(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout(self)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        scroll_area.setWidget(self.scroll_content)

        add_tag_button = QPushButton("Добавить новый тег")
        add_tag_button.clicked.connect(self.add_tag_input)

        main_layout.addWidget(scroll_area)
        main_layout.addWidget(add_tag_button)
        self.setLayout(main_layout)

        # Список для хранения всех введённых тегов
        self.tag_list = []

    def add_tag_input(self):
        tag_layout = QHBoxLayout()
        tag_input = QLineEdit()
        tag_input.setPlaceholderText("Введите содержание тега")
        tag_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(lambda: self.remove_tag_input(tag_layout, tag_input))

        tag_layout.addWidget(tag_input)
        tag_layout.addWidget(delete_button)
        self.scroll_layout.addLayout(tag_layout)
        tag_input.setFocus()

        # Сохраняем в список каждый добавленный тег (пока пустой)
        self.tag_list.append(tag_input)

        # Добавление тега - выводим список тегов сразу для отладки
        print(self.get_tag_list())

    def remove_tag_input(self, tag_layout, tag_input):
        while tag_layout.count():
            child = tag_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.scroll_layout.removeItem(tag_layout)

        # Удаляем тег из списка
        if tag_input in self.tag_list:
            self.tag_list.remove(tag_input)

    def get_tag_list(self):
        # Возвращаем список значений введённых тегов
        return [tag_input.text() for tag_input in self.tag_list if tag_input.text()]





