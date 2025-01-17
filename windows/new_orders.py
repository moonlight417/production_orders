
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewOrders(object):
    def setupUi(self, NewOrders):
        NewOrders.setObjectName("NewOrders")
        NewOrders.resize(1075, 660)
        self.centralwidget = QtWidgets.QWidget(NewOrders)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.widget)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1055, 603))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.empty_task = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.empty_task.setMinimumSize(QtCore.QSize(0, 60))
        self.empty_task.setAutoFillBackground(False)
        self.empty_task.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.empty_task.setObjectName("empty_task")
        self.verticalLayout_2.addWidget(self.empty_task)
        spacerItem = QtWidgets.QSpacerItem(20, 506, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        NewOrders.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewOrders)
        QtCore.QMetaObject.connectSlotsByName(NewOrders)

    def retranslateUi(self, NewOrders):
        _translate = QtCore.QCoreApplication.translate
        NewOrders.setWindowTitle(_translate("NewOrders", "Новые заказы"))
        self.label_3.setText(_translate("NewOrders", "Новые заказы"))

class NewOrders(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_NewOrders()
        self.ui.setupUi(self)
        self.parent = parent  # Сохраняем ссылку на родительское окно

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewOrders = QtWidgets.QMainWindow()
    ui = Ui_NewOrders()
    ui.setupUi(NewOrders)
    NewOrders.show()
    sys.exit(app.exec_())
