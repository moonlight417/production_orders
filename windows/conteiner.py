from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton, QWidget, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_MainWindowManager(object):
    def setupUi(self, MainWindowManager):
        MainWindowManager.setObjectName("MainWindowManager")
        MainWindowManager.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindowManager)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnNewTasks = QtWidgets.QPushButton(self.centralwidget)
        self.BtnNewTasks.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.BtnNewTasks.setObjectName("BtnNewTasks")
        self.BtnOrderBase = QtWidgets.QPushButton(self.centralwidget)
        self.BtnOrderBase.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.BtnOrderBase.setObjectName("BtnOrderBase")
        self.BtnDrowingArchive = QtWidgets.QPushButton(self.centralwidget)
        self.BtnDrowingArchive.setGeometry(QtCore.QRect(20, 140, 131, 31))
        self.BtnDrowingArchive.setObjectName("BtnDrowingArchive")
        self.BtnRoleSelection = QtWidgets.QPushButton(self.centralwidget)
        self.BtnRoleSelection.setGeometry(QtCore.QRect(270, 150, 91, 23))
        self.BtnRoleSelection.setObjectName("BtnRoleSelection")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 27, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(330, 27, 31, 21))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.LbCheckOrders = QtWidgets.QLabel(self.frame)
        self.LbCheckOrders.setGeometry(QtCore.QRect(6, 2, 20, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LbCheckOrders.setFont(font)
        self.LbCheckOrders.setAlignment(QtCore.Qt.AlignCenter)
        self.LbCheckOrders.setObjectName("LbCheckOrders")
        self.BtnCheck = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCheck.setGeometry(QtCore.QRect(290, 60, 70, 23))
        self.BtnCheck.setObjectName("BtnCheck")
        self.BtnViewTasks = QtWidgets.QPushButton(self.centralwidget)
        self.BtnViewTasks.setGeometry(QtCore.QRect(20, 60, 131, 31))
        self.BtnViewTasks.setObjectName("BtnViewTasks")
        MainWindowManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        MainWindowManager.setMenuBar(self.menubar)

        self.retranslateUi(MainWindowManager)
        QtCore.QMetaObject.connectSlotsByName(MainWindowManager)

    def retranslateUi(self, MainWindowManager):
        _translate = QtCore.QCoreApplication.translate
        MainWindowManager.setWindowTitle(_translate("MainWindowManager", "Главное окно менеджера"))
        self.BtnNewTasks.setText(_translate("MainWindowManager", "Новое задание"))
        self.BtnOrderBase.setText(_translate("MainWindowManager", "База заказов"))
        self.BtnDrowingArchive.setText(_translate("MainWindowManager", "Архив КД"))
        self.BtnRoleSelection.setText(_translate("MainWindowManager", "К выбору роли"))
        self.label.setText(_translate("MainWindowManager", "Заказов на проверку:"))
        self.LbCheckOrders.setText(_translate("MainWindowManager", "12"))
        self.BtnCheck.setText(_translate("MainWindowManager", "Проверить"))
        self.BtnViewTasks.setText(_translate("MainWindowManager", "Задания"))


from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QWidget
)
import sys


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Интерфейс с постоянными элементами")
        self.setGeometry(100, 100, 800, 600)

        # Создаем основной виджет и компоновку
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Постоянные элементы (например, заголовок и кнопки навигации)
        self.header_label = QLabel("Постоянный заголовок")
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        btn_nav_first = QPushButton("Первый экран")
        btn_nav_second = QPushButton("Второй экран")

        btn_nav_first.clicked.connect(self.show_first_screen)
        btn_nav_second.clicked.connect(self.show_second_screen)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(btn_nav_first)
        nav_layout.addWidget(btn_nav_second)

        # Добавляем постоянные элементы в компоновку
        main_layout.addWidget(self.header_label)
        main_layout.addLayout(nav_layout)

        # Создаем QStackedWidget для переключаемых экранов
        self.stacked_widget = QStackedWidget()

        # Создаем экраны и добавляем их в QStackedWidget
        self.first_screen = FirstScreen()
        self.second_screen = SecondScreen()

        self.stacked_widget.addWidget(self.first_screen)
        self.stacked_widget.addWidget(self.second_screen)

        # Добавляем QStackedWidget в основную компоновку
        main_layout.addWidget(self.stacked_widget)

        # Устанавливаем основной виджет с компоновкой
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def show_first_screen(self):
        self.stacked_widget.setCurrentWidget(self.first_screen)

    def show_second_screen(self):
        self.stacked_widget.setCurrentWidget(self.second_screen)


class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Первый экран")
        layout.addWidget(label)
        self.setLayout(layout)


class SecondScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Второй экран")
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
