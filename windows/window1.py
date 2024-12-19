import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication
from utils.api_client import ApiClient

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Window 1')
        layout = QVBoxLayout()

        self.label = QLabel('Items will be displayed here')
        layout.addWidget(self.label)

        self.button = QPushButton('Fetch Items')
        self.button.clicked.connect(self.fetch_items)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def fetch_items(self):
        items = ApiClient.fetch_items()
        if items:
            self.label.setText('\n'.join([item['name'] for item in items]))
        else:
            self.label.setText('Failed to fetch items')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window1()
    ex.show()
    sys.exit(app.exec_())