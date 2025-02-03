from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QMessageBox, QFrame, QVBoxLayout, QLabel, QPushButton, QWidget, QSizePolicy, QStackedWidget
)
from products.models import MainDocument
from windows.document_editor import DocumentEditor  # Импортируем редактор


class SearchDesignDoc(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Поиск документа")
        self.resize(1132, 698)

        #  Создаём QStackedWidget
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        #  Первая страница: Поиск документа
        self.page_search = QWidget()
        self.setup_search_ui(self.page_search)

        #  Вторая страница: Редактор документа
        self.page_editor = QWidget()

        #  Добавляем обе страницы в стек
        self.stack.addWidget(self.page_search)  # Индекс 0
        self.stack.addWidget(self.page_editor)  # Индекс 1

        #  Переключаемся на страницу поиска при запуске
        self.stack.setCurrentIndex(0)

    def setup_search_ui(self, parent_widget):
        """Настраивает UI поиска документа (первая страница)."""
        main_layout = QVBoxLayout(parent_widget)
        main_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.setSpacing(10)

        # ======= Шапка =======
        header_frame = QFrame()
        header_frame.setFrameShape(QFrame.StyledPanel)
        header_frame.setMinimumHeight(80)

        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        # Поле поиска по названию
        self.lineEditSearchByName = QtWidgets.QLineEdit(header_frame)
        self.lineEditSearchByName.setPlaceholderText("Введите название документа")
        self.BtnSearchByName = QPushButton("🔍")
        self.BtnSearchByName.setFixedSize(30, 30)
        self.BtnSearchByName.clicked.connect(self.search_design_document_by_main_name)

        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.lineEditSearchByName)
        search_layout.addWidget(self.BtnSearchByName)

        # Поле поиска по тегу
        self.lineEditSearchByTag = QtWidgets.QLineEdit(header_frame)
        self.lineEditSearchByTag.setPlaceholderText("Введите тег")
        self.BtnSearchByTag = QPushButton("🔍")
        self.BtnSearchByTag.setFixedSize(30, 30)
        self.BtnSearchByTag.clicked.connect(self.search_design_document_by_tag)

        tag_layout = QtWidgets.QHBoxLayout()
        tag_layout.addWidget(self.lineEditSearchByTag)
        tag_layout.addWidget(self.BtnSearchByTag)

        header_layout.addLayout(search_layout)
        header_layout.addLayout(tag_layout)

        # Добавляем шапку в главный layout
        main_layout.addWidget(header_frame)

        # ======= Прокручиваемая область =======
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.layoutTask = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutTask.setContentsMargins(5, 5, 5, 5)
        self.layoutTask.setSpacing(5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Добавляем scrollArea в главный layout
        main_layout.addWidget(self.scrollArea)

        parent_widget.setLayout(main_layout)

    def search_design_document_by_main_name(self):
        """Поиск документа по имени."""
        document_main_name = self.lineEditSearchByName.text().strip()
        if not document_main_name:
            QMessageBox.warning(self, "Ошибка", "Введите название документа.")
            return

        try:
            documents = MainDocument.objects.filter(main_name__icontains=document_main_name)
            if documents.exists():
                data = [{"id": doc.id, "name": doc.main_name, "comment": doc.comment} for doc in documents]
                self.update_document_list(data)
            else:
                QMessageBox.information(self, "Результат", "Документ не найден.")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка поиска: {e}")

    from functools import partial

    def update_document_list(self, documents):
        """Обновляет список найденных документов."""
        for i in reversed(range(self.layoutTask.count())):
            widget = self.layoutTask.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for document in reversed(documents):
            document_frame = QFrame()
            document_layout = QVBoxLayout(document_frame)
            document_info = QLabel(f"Документ: {document['name']} / Комментарий: {document['comment']}")
            document_layout.addWidget(document_info)

            edit_button = QPushButton("Открыть")
            edit_button.clicked.connect(partial(self.open_document_editor, document['id']))  # ✅ Используем partial
            document_layout.addWidget(edit_button)

            self.layoutTask.addWidget(document_frame)

        self.empty_placeholder = QWidget()
        self.empty_placeholder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutTask.addWidget(self.empty_placeholder)

    def open_document_editor(self, doc_id):
        """Открывает редактор документа в QStackedWidget."""
        print(f"📂 Открываем редактор документа с ID: {doc_id}")

        # ✅ Проверяем, есть ли уже `DocumentEditor`
        if hasattr(self, "editor") and self.editor:
            self.editor.deleteLater()  # Удаляем предыдущий редактор
            print("🗑️ Удаляем предыдущий экземпляр DocumentEditor")

        # ✅ Создаём новый экземпляр DocumentEditor
        self.editor = DocumentEditor(doc_id, self)
        if not self.page_editor.layout():
            self.page_editor.setLayout(QVBoxLayout())

        self.page_editor.layout().addWidget(self.editor)

        # ✅ Переключаемся на страницу редактора
        self.stack.setCurrentWidget(self.page_editor)

    def go_back_to_search(self):
        """Возвращает на страницу поиска."""
        self.stack.setCurrentIndex(0)


    def search_design_document_by_tag(self):
        """Поиск документа по тегу."""
        tag_name = self.lineEditSearchByTag.text().strip()
        if not tag_name:
            QMessageBox.warning(self, "Ошибка", "Введите название тега.")
            return

        try:
            documents = MainDocument.objects.filter(tags__name__icontains=tag_name).distinct()
            if documents.exists():
                data = [{"id": doc.id, "name": doc.main_name, "comment": doc.comment} for doc in documents]
                self.update_document_list(data)
            else:
                QMessageBox.information(self, "Результат", "Документы с таким тегом не найдены.")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка поиска: {e}")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = SearchDesignDoc()
    window.show()
    sys.exit(app.exec_())

