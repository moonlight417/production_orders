from PyQt5 import QtCore, QtGui, QtWidgets

class TaskFilling(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример размещения фреймов в ScrollArea")

        # Основной виджет
        main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(main_widget)

        # Контейнер для фреймов
        container = QtWidgets.QWidget()

        # Верт. layout для размещения фреймов
        layout = QtWidgets.QVBoxLayout(container)
        layout.setSpacing(5)  # Нет промежутков между фреймами
        layout.setContentsMargins(5, 5, 5, 5)  # Отсутствие отступов

        # Добавляем 5 фреймов размером 500x20
        for _ in range(20):
            frame = QtWidgets.QFrame(container)
            frame.setFixedSize(300, 20)
            frame.setStyleSheet("background-color: #425f8f;")  # Пример цвета фона

            # Устанавливаем политику размера фрейма, чтобы он не растягивался
            frame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

            layout.addWidget(frame)

        # Добавляем пустой элемент, который займет оставшееся пространство
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer_item)

        # Создаем QScrollArea
        scroll_area = QtWidgets.QScrollArea(main_widget)
        scroll_area.setWidgetResizable(True)  # Делает контейнер ресайзируемым
        scroll_area.setWidget(container)  # Устанавливаем наш контейнер в ScrollArea

        # Устанавливаем ScrollArea в основной layout
        main_layout = QtWidgets.QVBoxLayout(main_widget)
        main_layout.addWidget(scroll_area)

        self.show()

# Запуск приложения
app = QtWidgets.QApplication([])
window = TaskFilling()
app.exec_()
