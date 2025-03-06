import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc


# Функция для настройки Django
def setup_django():
    import django
    from pathlib import Path

    # Добавляем путь к проекту в sys.path
    BASE_DIR = Path(__file__).resolve().parent.parent
    sys.path.append(str(BASE_DIR))

    # Устанавливаем переменную окружения
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')  # Убедитесь что путь правильный!

    # Настраиваем Django
    django.setup()


# Вызываем функцию настройки Django
setup_django()

# Импортируем модели ПОСЛЕ настройки Django
from materials.models import SheetForm, RodForm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btnOpenRod = QtWidgets.QPushButton("Открыть Пруток", self.centralwidget)
        self.verticalLayout.addWidget(self.btnOpenRod)

        self.btnOpenSheet = QtWidgets.QPushButton("Открыть Лист", self.centralwidget)
        self.verticalLayout.addWidget(self.btnOpenSheet)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))


class Ui_TableWindow(QtWidgets.QMainWindow):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.setupUi()
        self.loadData()

    def setupUi(self):
        self.setObjectName("TableWindow")
        self.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.verticalLayout.addWidget(self.tableView)

        self.btnAddRow = QtWidgets.QPushButton("Добавить запись", self.centralwidget)
        self.verticalLayout.addWidget(self.btnAddRow)

        self.btnSaveChanges = QtWidgets.QPushButton("Сохранить изменения", self.centralwidget)
        self.verticalLayout.addWidget(self.btnSaveChanges)

        self.model = QSqlTableModel(self)
        self.model.setTable(self.table_name)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.tableView.setModel(self.model)

        self.btnAddRow.clicked.connect(self.addRow)
        self.btnSaveChanges.clicked.connect(self.saveChanges)

    def loadData(self):
        self.model.select()

    def addRow(self):
        self.model.insertRow(self.model.rowCount())

    def saveChanges(self):
        if self.model.submitAll():
            self.model.database().commit()
        else:
            self.model.database().rollback()


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnOpenRod.clicked.connect(lambda: self.openTable("rod_form"))
        self.ui.btnOpenSheet.clicked.connect(lambda: self.openTable("sheet_form"))

        self.initDatabase()

    def initDatabase(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("materials.db")
        if not self.db.open():
            QtWidgets.QMessageBox.critical(None, "Ошибка", "Не удалось подключиться к базе данных")
            return

    def openTable(self, table_name):
        self.tableWindow = Ui_TableWindow(table_name)
        self.tableWindow.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())