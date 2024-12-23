
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from windows.start_window import StartWindow


class Ui_MainWindowProduction(object):
    def setupUi(self, MainWindowProduction):
        MainWindowProduction.setObjectName("MainWindowProduction")
        MainWindowProduction.resize(378, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindowProduction)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnOrderBase = QtWidgets.QPushButton(self.centralwidget)
        self.BtnOrderBase.setGeometry(QtCore.QRect(20, 60, 131, 31))
        self.BtnOrderBase.setObjectName("BtnOrderBase")
        self.BtnDrowingArchive = QtWidgets.QPushButton(self.centralwidget)
        self.BtnDrowingArchive.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.BtnDrowingArchive.setObjectName("BtnDrowingArchive")
        self.BtnRoleSelection = QtWidgets.QPushButton(self.centralwidget)
        self.BtnRoleSelection.setGeometry(QtCore.QRect(260, 100, 101, 31))
        self.BtnRoleSelection.setObjectName("BtnRoleSelection")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 27, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(310, 27, 31, 21))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.LbNewOrders = QtWidgets.QLabel(self.frame)
        self.LbNewOrders.setGeometry(QtCore.QRect(6, 2, 20, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LbNewOrders.setFont(font)
        self.LbNewOrders.setAlignment(QtCore.Qt.AlignCenter)
        self.LbNewOrders.setObjectName("LbNewOrders")
        self.BtnNewOrders = QtWidgets.QPushButton(self.centralwidget)
        self.BtnNewOrders.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.BtnNewOrders.setObjectName("BtnNewOrders")
        MainWindowProduction.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowProduction)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        MainWindowProduction.setMenuBar(self.menubar)

        self.retranslateUi(MainWindowProduction)
        QtCore.QMetaObject.connectSlotsByName(MainWindowProduction)

    def retranslateUi(self, MainWindowProduction):
        _translate = QtCore.QCoreApplication.translate
        MainWindowProduction.setWindowTitle(_translate("MainWindowProduction", "Главное окно производство"))
        self.BtnOrderBase.setText(_translate("MainWindowProduction", "База заказов"))
        self.BtnDrowingArchive.setText(_translate("MainWindowProduction", "Архив КД"))
        self.BtnRoleSelection.setText(_translate("MainWindowProduction", "К выбору роли"))
        self.label.setText(_translate("MainWindowProduction", "Новых заказов:"))
        self.LbNewOrders.setText(_translate("MainWindowProduction", "12"))
        self.BtnNewOrders.setText(_translate("MainWindowProduction", "Новые заказы"))

class MainWindowProduction(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindowProduction()
        self.ui.setupUi(self)

        self.ui.BtnRoleSelection.clicked.connect(self.back_role_selection)

    def back_role_selection(self):
        try:
            self.role_selection_window = StartWindow()  # Создаем экземпляр окна для выбора роли
            self.role_selection_window.show()  # Показываем окно
            self.close()  # Закрываем текущее окно
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно выбора роли: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowProduction = QtWidgets.QMainWindow()
    ui = Ui_MainWindowProduction()
    ui.setupUi(MainWindowProduction)
    MainWindowProduction.show()
    sys.exit(app.exec_())
