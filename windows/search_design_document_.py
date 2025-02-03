import os
import django

# Устанавливаем переменную окружения для Django настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

# Инициализируем Django
django.setup()

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QStackedWidget, QFrame, QMessageBox, QScrollArea, QSizePolicy, QLabel, QLineEdit
)
from products.models import MainDocument, Drawing
from windows.document_manager import DocumentViewer


class SearchDesignDoc(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Поиск документа")
        self.resize(1132, 698)

        # Создаём QStackedWidget
        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        # Первая страница: Поиск документа
        self.page_search = QWidget()
        self.setup_search_ui(self.page_search)

        # Вторая страница: Иерархия + чертёж
        self.document_viewer = DocumentViewer()  # Заменили DocumentEditor на DocumentViewer

        # Добавляем обе страницы в стек
        self.stack.addWidget(self.page_search)  # Индекс 0
        self.stack.addWidget(self.document_viewer)  # Индекс 1

        # Переключаемся на страницу поиска при запуске
        self.stack.setCurrentIndex(0)

    def setup_search_ui(self, parent_widget):
        """Настраивает UI поиска документа (первая страница)."""
        main_layout = QVBoxLayout(parent_widget)

        # Верхняя панель навигации
        header_frame = QFrame()
        header_frame.setFrameShape(QFrame.StyledPanel)
        header_frame.setMinimumHeight(50)

        header_layout = QHBoxLayout(header_frame)
        header_layout.setContentsMargins(10, 10, 10, 10)

        # Кнопка "Назад"
        self.btn_back = QPushButton("← Назад")
        self.btn_back.setFixedSize(80, 40)
        self.btn_back.clicked.connect(self.go_back_to_search_screen)
        self.btn_back.setVisible(False)  # На первой странице кнопка назад скрыта

        # Кнопка "Вперёд"
        self.btn_forward = QPushButton("Вперёд →")
        self.btn_forward.setFixedSize(80, 40)
        self.btn_forward.setVisible(False)  # На первой странице кнопка "Вперёд" скрыта

        header_layout.addWidget(self.btn_back)
        header_layout.addStretch()
        header_layout.addWidget(self.btn_forward)

        main_layout.addWidget(header_frame)

        # Прокручиваемая область для списка документов
        self.scrollArea = QScrollArea()
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.layoutTask = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutTask.setContentsMargins(5, 5, 5, 5)
        self.layoutTask.setSpacing(5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Добавляем scrollArea в главный layout
        main_layout.addWidget(self.scrollArea)

        # Поля для ввода поиска
        self.lineEditSearchByName = QLineEdit()
        self.lineEditSearchByName.setPlaceholderText("Поиск по названию")
        self.lineEditSearchByTag = QLineEdit()
        self.lineEditSearchByTag.setPlaceholderText("Поиск по тегам")

        self.search_by_name_button = QPushButton("Поиск по названию")
        self.search_by_tag_button = QPushButton("Поиск по тегам")

        self.search_by_name_button.clicked.connect(self.search_design_document_by_main_name)
        self.search_by_tag_button.clicked.connect(self.search_design_document_by_tag)

        # Добавляем поля для ввода и кнопки поиска
        main_layout.addWidget(self.lineEditSearchByName)
        main_layout.addWidget(self.search_by_name_button)
        main_layout.addWidget(self.lineEditSearchByTag)
        main_layout.addWidget(self.search_by_tag_button)

        # Прокручиваемая область для списка документов
        self.scrollArea = QScrollArea()
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
                self.btn_forward.setVisible(True)  # Показываем кнопку "Вперёд" после успешного поиска
            else:
                QMessageBox.information(self, "Результат", "Документ не найден.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка поиска: {e}")

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
                self.btn_forward.setVisible(True)  # Показываем кнопку "Вперёд" после успешного поиска
            else:
                QMessageBox.information(self, "Результат", "Документы с таким тегом не найдены.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка поиска: {e}")

    def update_document_list(self, documents):
        """Обновляет список найденных документов."""
        # Очистка старого списка
        for i in reversed(range(self.layoutTask.count())):
            widget = self.layoutTask.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Добавление новых документов в список
        for document in documents:
            document_frame = QFrame()
            document_layout = QVBoxLayout(document_frame)
            document_info = QLabel(f"Документ: {document['name']} / Комментарий: {document['comment']}")
            document_layout.addWidget(document_info)

            edit_button = QPushButton("Открыть")
            edit_button.clicked.connect(lambda checked, doc_id=document['id']: self.open_document_hierarchy(doc_id))
            document_layout.addWidget(edit_button)

            self.layoutTask.addWidget(document_frame)

        self.empty_placeholder = QWidget()
        self.empty_placeholder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutTask.addWidget(self.empty_placeholder)

    def open_document_hierarchy(self, doc_id):
        """Открывает иерархию документов в `QStackedWidget`."""
        print(f"📂 Открываем иерархию документов для ID: {doc_id}")

        try:
            # Получаем объект документа по ID
            document = MainDocument.objects.get(id=doc_id)  # Это основной документ

            # Если необходимо, также можно загрузить связанные чертежи
            drawings = Drawing.objects.filter(main_document=document)

            # Загружаем иерархию в `DocumentViewer`
            self.document_viewer.hierarchy_screen.load_hierarchy(document)

            # Переключаемся на экран с иерархией
            self.stack.setCurrentIndex(1)  # Переход на второй экран (иерархия)

            # Обновляем навигационные кнопки
            self.update_navigation_buttons()

        except MainDocument.DoesNotExist:
            print(f"Документ с ID {doc_id} не найден.")
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {doc_id} не найден.")
        except Exception as e:
            print(f"Ошибка при загрузке иерархии: {e}")
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить иерархию документа: {e}")

        # Обновляем навигационные кнопки
        self.update_navigation_buttons()

    def go_back_to_search_screen(self):
        """Переход на экран поиска."""
        self.stack.setCurrentIndex(0)
        self.update_navigation_buttons()

    def go_forward_to_next_screen(self):
        """Переход на следующую страницу (например, иерархия или чертёж)."""
        current_index = self.stack.currentIndex()
        if current_index < self.stack.count() - 1:
            self.stack.setCurrentIndex(current_index + 1)
        self.update_navigation_buttons()

    def update_navigation_buttons(self):
        """Обновляет видимость кнопок в зависимости от текущей страницы."""
        current_index = self.stack.currentIndex()
        total_pages = self.stack.count()

        # На первой странице кнопка "Назад" скрыта
        self.btn_back.setVisible(current_index != 0)

        # На последней странице кнопка "Вперёд" скрыта
        self.btn_forward.setVisible(current_index != total_pages - 1)
