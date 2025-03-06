from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox, \
    QCheckBox, QLineEdit, QTabWidget, QSpacerItem, QSizePolicy, QSlider, QScrollArea
from PyQt5.QtGui import QPixmap, QTransform, QCursor
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from unidecode import unidecode
import os
import shutil


# def apply_button_style(button):
#     button.setStyleSheet("""
#             QPushButton {
#                 font-size: 20px;
#                 font-weight: bold;
#                 background-color: #999999;
#                 color: white;
#                 border: none;
#                 border-radius: 10px;
#                 padding: 10px 20px;
#             }
#             QPushButton:hover {
#                 background-color: #9FC5E8;
#             }
#         """)


class UnifiedDrawingTabWidget(QWidget):
    tabCloseRequested = pyqtSignal()  # Сигнал для удаления вкладки

    def __init__(self):
        super().__init__()

        # Главное хранилище вкладок
        self.inner_tab_widget = QTabWidget()
        self.inner_tab_widget.setTabsClosable(False)
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
        tab2 = QWidget()
        tab1_layout = QHBoxLayout(tab)
        tab2_layout = QVBoxLayout(tab2)  # Изменяем на QVBoxLayout для вертикального расположения

        # Область прокрутки для чертежа
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.image_widget = QWidget()
        self.image_layout = QVBoxLayout(self.image_widget)
        self.image_layout.setAlignment(Qt.AlignCenter)

        # Поле для отображения чертежа
        drawing_widget = QLabel("📂 Чертёж отсутствует")
        drawing_widget.setAlignment(Qt.AlignCenter)
        drawing_widget.setMouseTracking(True)  # Разрешаем отслеживание движения мыши
        drawing_widget.setCursor(QCursor(Qt.PointingHandCursor))  # Меняем курсор на лупу
        self.image_layout.addWidget(drawing_widget)
        self.scroll_area.setWidget(self.image_widget)

        # Кнопки управления
        buttons = QWidget()
        button_layout = QVBoxLayout(buttons)

        load_button = QPushButton("📂")
        # apply_button_style(load_button)
        load_button.setFixedWidth(80)
        load_button.clicked.connect(lambda: self.open_file(drawing_widget, scale_slider))

        self.rotate_left_button = QPushButton("↺")
        # apply_button_style(self.rotate_left_button)
        self.rotate_left_button.setEnabled(False)
        self.rotate_left_button.setFixedWidth(80)
        self.rotate_left_button.clicked.connect(lambda: self.rotate_image(drawing_widget, -90))

        # rotate_right_button = QPushButton("↻")
        # apply_button_style(rotate_right_button)
        # rotate_right_button.setFixedWidth(80)
        # rotate_right_button.clicked.connect(lambda: self.rotate_image(drawing_widget, 90))

        # Слайдер для масштабирования
        scale_slider = QSlider(Qt.Vertical)
        scale_slider.setMinimum(50)  # 50% масштаб
        scale_slider.setMaximum(200)  # 200% масштаб
        scale_slider.setValue(100)  # Начальное значение 100%
        scale_slider.setEnabled(False)  # Делаем слайдер неактивным по умолчанию
        scale_slider.valueChanged.connect(lambda value: self.scale_image(drawing_widget, value))

        # Поле массы и чекбокс актуальности
        mass_input = QLineEdit()
        mass_input.setPlaceholderText("Масса, кг")
        mass_input.setVisible(False)
        mass_input.setFixedWidth(80)
        mass_input.setFixedHeight(30)  # Установите фиксированную высоту
        mass_input.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Политика размера

        check_box_is_actual = QCheckBox("Актуальность")
        check_box_is_actual.stateChanged.connect(lambda state: mass_input.setVisible(state == Qt.Checked))

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # Добавляем в разметку
        button_layout.addWidget(load_button)
        button_layout.addWidget(self.rotate_left_button)
        # button_layout.addWidget(rotate_right_button)
        # button_layout.addWidget(QLabel("Масштаб:"))

        button_layout.addWidget(check_box_is_actual)
        button_layout.addWidget(mass_input)
        button_layout.addItem(spacer)

        # Кнопка закрытия текущего листа
        close_button = QPushButton("Удалить")
        close_button.setFixedWidth(80)
        # apply_button_style(close_button)
        close_button.clicked.connect(lambda: self.delete_current_inner_tab())
        button_layout.addWidget(close_button)  # Добавляем кнопку закрытия в button_layout

        tab1_layout.addWidget(buttons)

        # Добавляем кнопки и слайдер в разметку
        tab1_layout.addWidget(self.scroll_area)
        # Добавляем tab2 в tab1
        tab1_layout.addWidget(tab2)
        tab1_layout.addWidget(scale_slider)

        tab.setLayout(tab1_layout)

        # Добавляем в `inner_tab_widget`
        sheet_number = self.inner_tab_widget.count() + 1
        self.inner_tab_widget.addTab(tab, f"Лист {sheet_number}")

        self.current_pixmap = None  # Инициализация атрибута для хранения текущего изображения

    def scale_image(self, drawing_widget, scale_value):
        """Масштабирует изображение в зависимости от значения слайдера."""
        if self.current_pixmap:  # Используем текущее изображение
            scaled_pixmap = self.current_pixmap.scaled(self.current_pixmap.size() * (scale_value / 100), Qt.KeepAspectRatio)
            drawing_widget.setPixmap(scaled_pixmap)

    def delete_current_inner_tab(self):
        """Удаляет текущий чертёж (лист)."""
        current_index = self.inner_tab_widget.currentIndex()
        if current_index != -1:
            self.inner_tab_widget.removeTab(current_index)
            QMessageBox.information(self, "Удаление", "Текущий лист был удалён.")

    def open_file(self, drawing_widget, scale_slider):
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
        file_name_lat = file_name_lat.replace(" ", "_")  # Заменяем пробелы на подчеркивания

        # Архивация
        archive_folder = os.path.join(os.path.dirname(__file__), 'archived_images')
        os.makedirs(archive_folder, exist_ok=True)
        destination_path = os.path.join(archive_folder, file_name_lat)

        try:
            shutil.copy(file_path, destination_path)
            drawing_widget.pixmap = QPixmap(destination_path)
            drawing_widget.current_image_path = destination_path
            drawing_widget.current_angle = 0  # Инициализация угла поворота
            self.current_pixmap = drawing_widget.pixmap  # Сохраняем текущее изображение
            drawing_widget.setPixmap(self.current_pixmap.scaled(QSize(500, 500), Qt.KeepAspectRatio))
            scale_slider.setEnabled(True)  # Активируем слайдер после загрузки изображения
            scale_slider.setVisible(True)  # Показываем слайдер
            self.rotate_left_button.setEnabled(True) 
            print(f"✅ Чертёж загружен: {destination_path}")
        except Exception as e:
            print(f"❌ Ошибка загрузки чертежа: {e}")

    def rotate_image(self, drawing_widget, angle):
        """Поворачивает изображение на заданный угол."""
        if hasattr(drawing_widget, 'pixmap') and not drawing_widget.pixmap.isNull():
            # Убедимся, что у нас есть валидное изображение
            drawing_widget.current_angle = (drawing_widget.current_angle + angle) % 360
            transform = QTransform().rotate(drawing_widget.current_angle)
            self.current_pixmap = drawing_widget.pixmap.transformed(transform, Qt.SmoothTransformation)  # Обновляем текущее изображение
            drawing_widget.setPixmap(self.current_pixmap.scaled(QSize(500, 500), Qt.KeepAspectRatio))
        else:
            QMessageBox.warning(self, "Ошибка",
                                "Изображение не загружено. Пожалуйста, загрузите изображение перед поворотом.")

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