from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox, QCheckBox, QLineEdit
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from . import inner_tab_widget
from .print_dialog import PrintDialog
import shutil
import os

from PyQt5.QtCore import pyqtSignal

class DrawingWidget(QWidget):
    tabCloseRequested = pyqtSignal()  # Сигнал для запроса удаления вкладки

    def __init__(self):
        super().__init__()
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap()
        self.current_angle = 0
        self.current_image_path = None  # Хранение пути к текущему изображению
        self.inner_tab_widget = inner_tab_widget  # Экземпляр InnerTabWidget
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

        delete_button = QPushButton("Удалить текущий лист")
        delete_button.setFixedWidth(180)
        delete_button.clicked.connect(self.delete_current_inner_tab)

        self.lineEditMass = QLineEdit()
        self.lineEditMass.setFixedWidth(150)
        self.lineEditMass.setPlaceholderText("Масса, кг")
        self.lineEditMass.setVisible(False)  # Изначально скрываем поле массы

        self.check_box_is_actual = QCheckBox("Актуальность документа", self)
        self.check_box_is_actual.stateChanged.connect(self.toggle_mass_field)

        # Добавляем виджеты в вертикальный лэйаут
        button_panel.addWidget(load_button)
        button_panel.addWidget(print_button)
        button_panel.addWidget(rotate_left_button)
        button_panel.addWidget(rotate_right_button)
        button_panel.addWidget(delete_button)
        button_panel.addStretch()
        button_panel.addWidget(self.check_box_is_actual)
        button_panel.addWidget(self.lineEditMass)

        # Добавляем лэйауты и элементы в основной горизонтальный лэйаут
        layout.addLayout(button_panel)
        layout.addWidget(self.image_label)

        # Устанавливаем лэйаут для окна
        self.setLayout(layout)

    def toggle_mass_field(self, state):
        """
        Показать или скрыть поле ввода массы в зависимости от состояния чекбокса.
        """
        self.lineEditMass.setVisible(state == Qt.Checked)

    import os
    import shutil
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5.QtGui import QPixmap

    def open_file(self):
        """Открывает файл изображения из любого места, копирует его в `archived_images` и сохраняет путь."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл чертежа",
            "",  # ✅ Теперь можно выбирать из любой папки
            "Изображения (*.png *.jpg *.bmp *.gif);;Все файлы (*)"
        )

        if not file_path:
            print("⚠️ Файл не выбран. Операция отменена.")
            return

        print(f"📄 Выбран файл: {file_path}")

        # Создаем папку архива, если её нет
        archive_folder = os.path.join(os.path.dirname(__file__), 'archived_images')
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)
            print(f"📂 Папка '{archive_folder}' была создана.")

        # Получаем имя файла
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(archive_folder, file_name)

        print(f"📂 Копируем файл в: {destination_path}")

        try:
            if not os.path.exists(file_path):
                print(f"❌ Файл {file_path} не найден!")
                return

            shutil.copy(file_path, destination_path)
            print(f"✅ Файл успешно скопирован: {destination_path}")

            # Загружаем изображение
            self.pixmap = QPixmap(destination_path)
            self.current_angle = 0

            if self.pixmap.isNull():
                print(f"❌ Ошибка загрузки изображения: {destination_path}")
                return

            self.update_image()
            self.current_image_path = destination_path  # ✅ Теперь путь всегда сохраняется
            print(f"✅ Путь к файлу сохранен в `current_image_path`: {self.current_image_path}")

        except Exception as e:
            print(f"❌ Ошибка при обработке файла: {e}")

    def rotate_right(self):
        if not self.pixmap.isNull():
            self.current_angle = (self.current_angle + 90) % 360
            self.update_image()
            self.save_rotated_image()  # Сохраняем изображение после поворота

    def rotate_left(self):
        if not self.pixmap.isNull():
            self.current_angle = (self.current_angle - 90) % 360
            self.update_image()
            self.save_rotated_image()  # Сохраняем изображение после поворота

    def update_image(self):
        if not self.pixmap.isNull():
            transform = QTransform().rotate(self.current_angle)
            rotated_pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
            fixed_size = QSize(500, 500)
            scaled_pixmap = rotated_pixmap.scaled(fixed_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

    def open_printer_window(self):
        if not self.current_image_path:
            QMessageBox.warning(self, "Предупреждение", "Нет изображения для печати.")
            return
        self.printer_window = PrintDialog(self.current_image_path)
        self.printer_window.show()

    def delete_current_inner_tab(self):
        """
        Отправить сигнал на удаление текущей вкладки.
        """
        reply = QMessageBox.question(
            self, "Подтверждение удаления",
            "Вы уверены, что хотите удалить текущий лист?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.tabCloseRequested.emit()  # Отправляем сигнал

    def save_rotated_image(self):
        """
        Сохраняет текущее изображение с учётом угла поворота в архив.
        """
        if not self.pixmap.isNull() and self.current_image_path:
            # Применяем текущий угол поворота
            transform = QTransform().rotate(self.current_angle)
            rotated_pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)

            # Сохраняем изображение в том же месте, где находится исходный файл
            rotated_pixmap.save(self.current_image_path)
            print(f"Изображение сохранено с новым поворотом: {self.current_image_path}")


