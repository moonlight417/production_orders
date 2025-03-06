# document_viewer.py
import os

from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QMessageBox, QDialog,
    QScrollArea, QFrame, QSlider, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QCursor, QPainter, QTransform
from PyQt5.QtCore import Qt, QRectF
from products.models import DrawingSheet, MainDocument, Drawing, Tag
from print_dialog import PrintDialog  # Импортируем класс PrintDialog из другого файла
# from windows.design_edit.design_document_edit_form import DesignDocumentEditForm

class DocumentViewer(QWidget):
    """Редактирование конструкторского документа с функциями поворота, масштабирования и печати чертежа."""

    def __init__(self, doc_id, parent=None):
        super().__init__(parent)
        self.doc_id = doc_id
        self.parent = parent  # Сохраняем родительский `QStackedWidget`
        self.setWindowTitle(f"Просмотр документа (ID: {self.doc_id})")

        # 📄 Загружаем документ из базы
        try:
            self.document = MainDocument.objects.get(id=self.doc_id)
        except MainDocument.DoesNotExist:
            QMessageBox.critical(self, "Ошибка", f"Документ с ID {self.doc_id} не найден!")
            self.close()  # Закрываем виджет, если документ не найден
            return

        # 🏗️ Основной layout
        main_layout = QHBoxLayout(self)

        # 📂 Левая часть (Чертёж)
        self.left_layout = QVBoxLayout()

        # Область прокрутки для чертежа
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.image_widget = QWidget()
        self.image_layout = QVBoxLayout(self.image_widget)
        self.image_layout.setAlignment(Qt.AlignCenter)

        # Поле для отображения чертежа
        self.drawing_label = QLabel("📂 Чертёж отсутствует")
        self.drawing_label.setMouseTracking(True)  # Разрешаем отслеживание движения мыши
        self.drawing_label.setCursor(QCursor(Qt.PointingHandCursor))  # Меняем курсор на лупу
        self.image_layout.addWidget(self.drawing_label)
        self.scroll_area.setWidget(self.image_widget)
        self.left_layout.addWidget(self.scroll_area)

        # Элементы управления
        control_layout = QHBoxLayout()

        # Кнопка "↺ Повернуть влево"
        self.rotate_left_button = QPushButton("↺")
        self.rotate_left_button.clicked.connect(self.rotate_left)
        control_layout.addWidget(self.rotate_left_button)

        # Кнопка "↻ Повернуть вправо"
        self.rotate_right_button = QPushButton("↻")
        self.rotate_right_button.clicked.connect(self.rotate_right)
        control_layout.addWidget(self.rotate_right_button)

        # Слайдер для масштабирования
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(50)  # 50% масштаб
        self.scale_slider.setMaximum(200)  # 200% масштаб
        self.scale_slider.setValue(100)  # Начальное значение 100%
        self.scale_slider.valueChanged.connect(self.scale_image)
        control_layout.addWidget(QLabel("Масштаб:"))
        control_layout.addWidget(self.scale_slider)

        # # Кнопка "Редактировать"
        # self.edit_button = QPushButton("Редактировать")
        # self.edit_button.clicked.connect(self.open_edit_window)
        # control_layout.addWidget(self.edit_button)

        # Кнопка печати
        self.print_button = QPushButton("🖨 Печать")
        self.print_button.clicked.connect(self.print_image)
        control_layout.addWidget(self.print_button)

        # Кнопка удаления
        self.delete_button = QPushButton("Удалить")
        self.delete_button.clicked.connect(self.delete_document)
        control_layout.addWidget(self.delete_button)

        # Кнопка возврата
        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.go_back)
        control_layout.addWidget(self.back_button)

        self.left_layout.addLayout(control_layout)
        main_layout.addLayout(self.left_layout, stretch=2)  # Левая часть занимает 2/3 экрана

        # 📜 Правая часть (Данные документа)
        self.right_layout = QVBoxLayout()

        self.scroll_area_info = QScrollArea()
        self.scroll_area_info.setWidgetResizable(True)
        self.scroll_content_info = QWidget()
        self.scroll_layout_info = QVBoxLayout(self.scroll_content_info)

        # Загружаем данные документа
        self.load_document_data()

        self.scroll_area_info.setWidget(self.scroll_content_info)
        self.right_layout.addWidget(self.scroll_area_info)

        main_layout.addLayout(self.right_layout, stretch=1)  # Правая часть занимает 1/3 экрана

        self.setLayout(main_layout)

        # Инициализация переменных для управления изображением
        self.current_image_path = self.load_drawing_image()
        self.pixmap = QPixmap(self.current_image_path) if self.current_image_path else QPixmap()
        self.angle = 0
        self.scale_factor = 1.0

        # Обновляем изображение
        self.update_image()

    def load_drawing_image(self):
        """Загружает чертёж из базы и возвращает путь к файлу."""
        try:
            # Получаем корневую директорию проекта
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # Загружаем актуальный чертёж
            drawing_sheet = DrawingSheet.objects.filter(
                drawing__main_document=self.document,
                is_actual=True
            ).first()

            if drawing_sheet and drawing_sheet.file:
                # Формируем абсолютный путь к файлу
                file_path = os.path.join(base_dir, drawing_sheet.file.name)
                print(f"🔄 Проверка пути к файлу: {file_path}")

                if os.path.exists(file_path):
                    print("✅ Изображение успешно загружено")
                    return file_path
                else:
                    print(f"❌ Файл не найден: {file_path}")
            else:
                print("❌ Нет актуального чертежа")
        except Exception as e:
            print(f"❌ Ошибка при загрузке: {str(e)}")
        return None

    def load_document_data(self):
        """Загружает и отображает данные документа в правой части (QScrollArea)."""
        self.scroll_layout_info.setAlignment(Qt.AlignTop)

        # 📌 Основная информация
        self.scroll_layout_info.addWidget(QLabel("<b>Информация о документе:</b>"))
        self.scroll_layout_info.addWidget(QLabel(f"📄 Название: {self.document.main_name}"))
        self.scroll_layout_info.addWidget(QLabel(f"🗒 Комментарий: {self.document.comment or '—'}"))

        # 🔖 Теги
        tags = self.document.tags.all()
        tag_names = ", ".join(tag.name for tag in tags) if tags else "—"
        self.scroll_layout_info.addWidget(QLabel(f"🏷️ Теги: {tag_names}"))

        # 📜 Загружаем иерархию родитель-потомок
        self.load_hierarchy()

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.scroll_layout_info.addItem(spacer)

    def zoom_image(self):
        """Увеличивает изображение на 10%."""
        self.scale_factor += 0.1
        self.update_image()

    def rotate_left(self):
        """Поворачивает изображение на 90 градусов влево."""
        self.angle -= 90
        self.update_image()

    def rotate_right(self):
        """Поворачивает изображение на 90 градусов вправо."""
        self.angle += 90
        self.update_image()

    def scale_image(self, value):
        """Масштабирует изображение в соответствии со значением слайдера."""
        self.scale_factor = value / 100.0
        self.update_image()

    def update_image(self):
        """Обновляет изображение с учетом поворота и масштабирования."""
        if not self.pixmap.isNull():
            transform = QTransform().rotate(self.angle)
            scaled_pixmap = self.pixmap.scaled(
                self.pixmap.size() * self.scale_factor,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            rotated_pixmap = scaled_pixmap.transformed(transform, Qt.SmoothTransformation)
            self.drawing_label.setPixmap(rotated_pixmap)

    def print_image(self):
        """Печатает изображение с выбором принтера."""
        if not self.pixmap.isNull():
            printer = QPrinter(QPrinter.HighResolution)
            print_dialog = QPrintDialog(printer, self)

            if print_dialog.exec_() == QPrintDialog.Accepted:
                try:
                    painter = QPainter(printer)
                    if not painter.isActive():
                        QMessageBox.warning(self, "Ошибка", "Не удалось подключиться к принтеру.")
                        return

                    # Масштабируем изображение под размер страницы
                    page_rect = printer.pageRect(QPrinter.DevicePixel)
                    image_rect = QRectF(self.pixmap.rect())

                    # Рисуем изображение на принтере
                    painter.drawPixmap(page_rect, self.pixmap, image_rect)
                    painter.end()

                    QMessageBox.information(self, "Успех", "Чертёж отправлен на печать!")
                except Exception as e:
                    QMessageBox.critical(self, "Ошибка", f"Ошибка при печати: {str(e)}")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет изображения для печати.")

    def load_hierarchy(self):
        """Загружает иерархию документов, добавляя кнопки с отступами для родительских и дочерних чертежей."""
        self.scroll_layout_info.addWidget(QLabel("<b>Иерархия чертежей:</b>"))

        # 🔍 Получаем ВСЕ корневые чертежи (без родителя)
        root_drawings = Drawing.objects.filter(main_document=self.document, parent=None)

        for drawing in root_drawings:
            self.add_drawing_button(drawing, 0)  # Родители идут с уровнем 0

    def add_drawing_button(self, drawing, level):
        """Создаёт кнопку чертежа в иерархии с отступами для дочерних элементов."""

        # 🔍 Определяем цвет кнопки
        sheet = DrawingSheet.objects.filter(drawing=drawing, is_actual=True).first()
        if sheet and sheet.mass is not None:
            color = "green"  # ✅ Актуальный с массой
            mass_text = f" ⚖️ {sheet.mass} кг"
        elif sheet:
            color = "yellow"  # ⚠️ Актуальный, но без массы
            mass_text = " ❌ Без массы"
        else:
            color = "red"  # ⛔ Неактуальный
            mass_text = " ⛔ Неактуальный"

        # 🔹 Создаём кнопку
        button = QPushButton(f"{' ' * (level * 4)}📄 {drawing.doc_name}{mass_text}")
        button.clicked.connect(lambda: self.load_new_drawing(drawing))

        # 🎨 Применяем цвет кнопки
        if color == "green":
            button.setStyleSheet(f"background-color: #DFFFD6; color: black; padding-left: {level * 20}px;")
        elif color == "yellow":
            button.setStyleSheet(f"background-color: #FFFFCC; color: black; padding-left: {level * 20}px;")
        elif color == "red":
            button.setStyleSheet(f"background-color: #FFC0CB; color: black; padding-left: {level * 20}px;")

        self.scroll_layout_info.addWidget(button)

        # 🔽 Добавляем дочерние чертежи с увеличенным уровнем отступа
        child_drawings = Drawing.objects.filter(parent=drawing)
        for child in child_drawings:
            self.add_drawing_button(child, level + 1)  # Увеличиваем уровень вложенности

    def load_new_drawing(self, drawing):
        """Загружает новый чертёж в левую часть экрана."""
        drawing_sheet = DrawingSheet.objects.filter(drawing=drawing, is_actual=True).first()
        if drawing_sheet and drawing_sheet.file:
            # Получаем корневую директорию проекта
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_dir, drawing_sheet.file.name)
            if os.path.exists(file_path):
                self.pixmap = QPixmap(file_path)
                if not self.pixmap.isNull():
                    self.update_image()  # Обновляем изображение с новым pixmap
                else:
                    self.drawing_label.setText("⚠️ Ошибка загрузки изображения")
            else:
                self.drawing_label.setText("❌ Файл не найден")
        else:
            self.drawing_label.setText("📂 Чертёж отсутствует")

    # def open_edit_window(self):
    #     self.edit_window = EditDocumentWindow(self.doc_id, self)
    #     self.edit_window.show()

    def update_document_data(self):
        """Перезагружает данные документа после редактирования"""
        self.document.refresh_from_db()
        self.current_image_path = self.load_drawing_image()
        self.pixmap = QPixmap(self.current_image_path) if self.current_image_path else QPixmap()
        self.update_image()

        # Очищаем и перезагружаем информацию
        while self.scroll_layout_info.count():
            item = self.scroll_layout_info.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.load_document_data()

    def save_document(self):
        """Сохраняет изменения в документе."""
        try:
            self.document.comment = self.comment_edit.toPlainText()
            self.document.save()
            QMessageBox.information(self, "Успех", "Комментарий обновлён!")
            self.go_back()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить документ: {e}")

    def delete_document(self):
        """Удаляет текущий документ из базы данных."""
        reply = QMessageBox.question(self, "Подтверждение", "Вы уверены, что хотите удалить этот документ?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.document.delete()
                QMessageBox.information(self, "Успех", "Документ успешно удален!")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при удалении документа: {str(e)}")

    def go_back(self):
        """🏳 Переключает `QStackedWidget` обратно на поиск документов."""
        self.parent.go_back_to_search()