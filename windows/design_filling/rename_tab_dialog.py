from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class RenameTabDialog(QDialog):
    def __init__(self, current_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Изменение названия вкладки")
        self.current_name = current_name
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        label = QLabel(f"Текущее название: {self.current_name}")
        layout.addWidget(label)

        self.new_name_input = QLineEdit(self)
        self.new_name_input.setText(self.current_name)
        layout.addWidget(self.new_name_input)

        button_ok = QPushButton("Изменить")
        button_ok.clicked.connect(self.accept)  # Закрывает диалог с кодом QDialog.Accepted
        layout.addWidget(button_ok)

    def get_new_name(self):
        """Возвращает новое название, введённое пользователем."""
        return self.new_name_input.text()
