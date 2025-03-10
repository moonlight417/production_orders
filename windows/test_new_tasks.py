from PyQt5 import QtWidgets, QtCore
import requests
from task_detail import TaskDetail  # Импортируем класс для дочернего окна


class NewTasks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        print("Инициализация NewTasks...")  # Отладочное сообщение
        self.setWindowTitle("Новые задания")
        self.setGeometry(100, 100, 600, 400)

        # Создаем центральный виджет
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Создаем QScrollArea
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Позволяет виджету изменять размер
        self.layout.addWidget(self.scroll_area)

        # Создаем контейнер для заданий
        self.task_container = QtWidgets.QVBoxLayout()
        self.task_widget = QtWidgets.QWidget()  # Создаем виджет для контейнера
        self.task_widget.setLayout(self.task_container)  # Устанавливаем layout для виджета

        self.scroll_area.setWidget(self.task_widget)  # Устанавливаем виджет в QScrollArea

        # # Загружаем новые задания
        # self.load_new_tasks()

        # Атрибут для хранения выбранного ID задания
        self.selected_task_id = None



    def load_new_tasks(self):
        """Метод для загрузки и отображения новых заданий"""
        try:
            base_url = 'http://127.0.0.1:8000/'
            api_path = 'orders/new_tasks/'  # Предполагаем, что у вас есть этот маршрут
            full_url = f'{base_url}{api_path}'

            response = requests.get(full_url)
            if response.status_code == 200:
                new_tasks = response.json()  # Предполагаем, что сервер возвращает список новых заданий
                print(f"Полученные задания: {new_tasks}")  # Отладочное сообщение
                self.populate_task_list(new_tasks)  # Заполняем список заданий
            else:
                self.task_container.addWidget(QtWidgets.QLabel("Не удалось загрузить новые задания."))
        except Exception as e:
            print(f"Ошибка при загрузке новых заданий: {e}")  # Отладочное сообщение
            self.task_container.addWidget(QtWidgets.QLabel(f"Произошла ошибка: {str(e)}"))

    def populate_task_list(self, tasks):
        """Метод для заполнения списка заданий в контейнере"""
        # Очищаем предыдущие элементы в контейнере
        for i in reversed(range(self.task_container.count())):
            item = self.task_container.itemAt(i)
            if item.widget():  # Удаляем виджеты
                item.widget().deleteLater()
            elif item.spacerItem():  # Удаляем QSpacerItem
                self.task_container.removeItem(item)

        # Добавляем новые задания в контейнер
        for task in tasks:
            task_widget = QtWidgets.QWidget()
            task_layout = QtWidgets.QHBoxLayout(task_widget)

            # Формируем текст для задания
            task_text = (
                f"Задание: {task.get('invoice_number', 'Неизвестно')} - "
                f"Дата: {task.get('order_invoice_date', 'Неизвестно')} - "
                f"Заказчик: {task.get('customer_name', 'Неизвестно')}"
            )

            task_label = QtWidgets.QLabel(task_text)
            open_button = QtWidgets.QPushButton("Открыть")
            open_button.setFixedWidth(80)
            open_button.clicked.connect(
                lambda checked, task_data=task: self.open_task(task_data))  # Передаем данные задания в метод

            task_layout.addWidget(open_button)
            task_layout.addWidget(task_label)
            self.task_container.addWidget(task_widget)

        # Добавляем пустой заполнитель в конец контейнера
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.task_container.addSpacerItem(spacer)


    def open_task(self, task_data):
        """Метод для открытия задания"""
        task_id = task_data.get('id')  # Предполагаем, что у вас есть ID задания в данных
        if task_id is None:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "ID задания не найден.")
            return

        base_url = 'http://127.0.0.1:8000/'
        api_path = f'orders/update_task_status/{task_id}/'  # Путь к API для обновления статуса
        full_url = f'{base_url}{api_path}'

        response = requests.post(full_url)  # Отправляем POST-запрос на сервер
        print(f"Статус ответа: {response.status_code}, Ответ: {response.text}")  # Отладочное сообщение
        if response.status_code == 200:
            # Если статус успешно обновлен, открываем окно с деталями задания
            self.task_detail_window = TaskDetail(task_data)
            self.task_detail_window.exec_()  # Используем exec_() для модального окна
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось обновить статус задания.")

    def get_selected_task_id(self):
        """Возвращает ID выбранного задания"""
        return self.selected_task_id


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = NewTasks()
    window.show()
    app.exec_()
