from PyQt5 import QtWidgets, QtCore, QtGui
import os
import shutil


class UnifiedDrawingTabWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.inner_tab_widget = QtWidgets.QTabWidget()
        self.add_button = QtWidgets.QPushButton("Добавить лист")

        layout.addWidget(self.add_button)
        layout.addWidget(self.inner_tab_widget)

        self.add_button.clicked.connect(self.add_inner_tab)

    def add_inner_tab(self):
        tab = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(tab)

        self.inner_tab_widget.addTab(tab, f"Лист {self.inner_tab_widget.count() + 1}")

    def get_inner_tabs_data(self):
        data = []
        for i in range(self.inner_tab_widget.count()):
            tab = self.inner_tab_widget.widget(i)
            # Здесь можно добавить логику для сбора данных с каждой вкладки
            data.append({})
        return data

