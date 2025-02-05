from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox, \
    QCheckBox, QLineEdit, QTabWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from unidecode import unidecode
import os
import shutil


def apply_button_style(button):
    button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-weight: bold;
                background-color: #999999;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #9FC5E8;
            }
        """)


class UnifiedDrawingTabWidget(QWidget):
    tabCloseRequested = pyqtSignal()  # Сигнал для удаления вкладки

    def __init__(self):
        super().__init__()

        # Главное хранилище вкладок
        self.inner_tab_widget = QTabWidget()
        self.inner_tab_widget.setTabsClosable(True)
        self.inner_tab_widget.tabCloseRequested.connect(self.delete_current_inner_tab)

        # Интерфейс для добавления нового листа
        self.add_button = QPushButton("Добавить лист")
        self.add_button.clicked.connect(self.add_inner_tab)

        # Разметка
        layout = QVBoxLayout(self)
        layout.addWidget(self.add_button)
        layout.addWidget(self.inner_tab_widget)
        self.setLayout(layout)



    def add_inner_tab(self):
        """Добавляет новый лист-чертёж как вкладку."""
        tab = QWidget()
        tab_layout = QHBoxLayout(tab)

        buttons = QWidget()
        button_layout = QVBoxLayout(buttons)

        # Чертёжные элементы
        drawing_widget = QLabel()
        drawing_widget.setAlignment(Qt.AlignCenter)
        drawing_widget.pixmap = QPixmap()
        drawing_widget.current_angle = 0
        drawing_widget.current_image_path = None

        # Кнопки управления
        load_button = QPushButton("📂")
        apply_button_style(load_button)
        load_button.setFixedWidth(80)
        load_button.clicked.connect(lambda: self.open_file(drawing_widget))

        rotate_left_button = QPushButton("↺")
        # Устанавливаем стиль для кнопки

        # Принудительно настроим минимальную ширину, чтобы текст и стиль подгонялись
        rotate_left_button.setFixedWidth(80)
        apply_button_style(rotate_left_button)
        rotate_left_button.clicked.connect(lambda: self.rotate_image(drawing_widget, -90))

        rotate_right_button = QPushButton("↻")
        apply_button_style(rotate_right_button)
        rotate_right_button.setFixedWidth(80)
        rotate_right_button.clicked.connect(lambda: self.rotate_image(drawing_widget, 90))

        # delete_button = QPushButton("Удалить текущий лист")
        # delete_button.clicked.connect(self.delete_current_inner_tab)

        # Поле массы и чекбокс актуальности
        mass_input = QLineEdit()
        mass_input.setPlaceholderText("Масса, кг")
        mass_input.setVisible(False)
        mass_input.setFixedWidth(80)

        check_box_is_actual = QCheckBox("Актуальность")
        check_box_is_actual.stateChanged.connect(lambda state: mass_input.setVisible(state == Qt.Checked))

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Добавляем в разметку
        tab_layout.addWidget(buttons)
        button_layout.addWidget(load_button)
        button_layout.addWidget(rotate_left_button)
        button_layout.addWidget(rotate_right_button)
        # tab_layout.addWidget(load_button)
        # tab_layout.addWidget(rotate_left_button)
        # tab_layout.addWidget(rotate_right_button)
        # tab_layout.addWidget(delete_button)
        button_layout.addWidget(check_box_is_actual)
        button_layout.addWidget(mass_input)
        button_layout.addItem(spacer)
        tab_layout.addWidget(drawing_widget)
        tab.setLayout(tab_layout)

        # Добавляем в `inner_tab_widget`
        sheet_number = self.inner_tab_widget.count() + 1
        self.inner_tab_widget.addTab(tab, f"Лист {sheet_number}")



    def delete_current_inner_tab(self):
        """Удаляет текущий чертёж (лист)."""
        current_index = self.inner_tab_widget.currentIndex()
        if current_index != -1:
            self.inner_tab_widget.removeTab(current_index)
            QMessageBox.information(self, "Удаление", "Текущий лист был удалён.")

    def open_file(self, drawing_widget):
        """Загружает изображение, копирует в архив и отображает."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл чертежа", "", "Изображения (*.png *.jpg *.bmp *.gif);;Все файлы (*)"
        )

        if not file_path:
            print("⚠️ Файл не выбран.")
            return

        # Преобразуем имя файла в латиницу
        file_name = os.path.basename(file_path)
        file_name_lat = unidecode(file_name)  # Преобразуем в латиницу
        file_name_lat = file_name_lat.replace(" ", "_")  # Дополнительно заменяем пробелы на подчеркивания

        # Архивация
        archive_folder = os.path.join(os.path.dirname(__file__), 'archived_images')
        os.makedirs(archive_folder, exist_ok=True)
        destination_path = os.path.join(archive_folder, file_name_lat)

        try:
            shutil.copy(file_path, destination_path)
            drawing_widget.pixmap = QPixmap(destination_path)
            drawing_widget.current_image_path = destination_path
            drawing_widget.setPixmap(drawing_widget.pixmap.scaled(QSize(500, 500), Qt.KeepAspectRatio))
            print(f"✅ Чертёж загружен: {destination_path}")
        except Exception as e:
            print(f"❌ Ошибка загрузки чертежа: {e}")

    def rotate_image(self, drawing_widget, angle):
        """Поворачивает изображение на заданный угол."""
        if not drawing_widget.pixmap.isNull():
            drawing_widget.current_angle = (drawing_widget.current_angle + angle) % 360
            transform = QTransform().rotate(drawing_widget.current_angle)
            rotated_pixmap = drawing_widget.pixmap.transformed(transform, Qt.SmoothTransformation)
            drawing_widget.setPixmap(rotated_pixmap.scaled(QSize(500, 500), Qt.KeepAspectRatio))

    def get_inner_tabs_data(self):
        """Собирает информацию о чертежах."""
        inner_tabs_data = []

        for i in range(self.inner_tab_widget.count()):
            inner_tab = self.inner_tab_widget.widget(i)
            drawing_widget = inner_tab.findChild(QLabel)

            if drawing_widget and hasattr(drawing_widget, "current_image_path"):
                file_path = drawing_widget.current_image_path
                is_actual_checkbox = inner_tab.findChild(QCheckBox)
                is_actual = is_actual_checkbox.isChecked() if is_actual_checkbox else False

                # 🔹 Теперь ищем `QLineEdit` внутри конкретного листа!
                mass_input = inner_tab.findChild(QLineEdit)
                mass = float(mass_input.text()) if mass_input and mass_input.text().strip() else None

                inner_tabs_data.append({
                    "file": file_path,
                    "is_actual": is_actual,
                    "mass": mass,
                })
                print(f"📄 Собран чертёж: {file_path} (Актуальность: {is_actual}), масса: {mass}")

        return inner_tabs_data

