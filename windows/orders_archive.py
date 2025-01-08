
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

class Ui_OrdersArchive(object):
    def setupUi(self, OrdersArchive):
        OrdersArchive.setObjectName("OrdersArchive")
        OrdersArchive.resize(1013, 590)
        self.centralwidget = QtWidgets.QWidget(OrdersArchive)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_widget = QtWidgets.QWidget(self.centralwidget)
        self.header_widget.setObjectName("header_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.header_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.header_widget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 2, 1, 1)
        self.BtnSearchByCustomer = QtWidgets.QPushButton(self.header_widget)
        self.BtnSearchByCustomer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/utils/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSearchByCustomer.setIcon(icon)
        self.BtnSearchByCustomer.setObjectName("BtnSearchByCustomer")
        self.gridLayout.addWidget(self.BtnSearchByCustomer, 0, 5, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.header_widget)
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.header_widget)
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.header_widget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEditSearchByCustomer = QtWidgets.QLineEdit(self.header_widget)
        self.lineEditSearchByCustomer.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEditSearchByCustomer.setObjectName("lineEditSearchByCustomer")
        self.gridLayout.addWidget(self.lineEditSearchByCustomer, 0, 0, 1, 5)
        self.label_by = QtWidgets.QLabel(self.header_widget)
        self.label_by.setObjectName("label_by")
        self.gridLayout.addWidget(self.label_by, 0, 11, 1, 1)
        self.dateEditEndPeriod = QtWidgets.QDateEdit(self.header_widget)
        self.dateEditEndPeriod.setCalendarPopup(True)
        self.dateEditEndPeriod.setObjectName("dateEditEndPeriod")
        self.gridLayout.addWidget(self.dateEditEndPeriod, 0, 12, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.header_widget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout.addWidget(self.line_12, 0, 8, 1, 1)
        self.checkBoxPeriod = QtWidgets.QCheckBox(self.header_widget)
        self.checkBoxPeriod.setObjectName("checkBoxPeriod")
        self.gridLayout.addWidget(self.checkBoxPeriod, 0, 9, 1, 1)
        self.dateEditStartPeriod = QtWidgets.QDateEdit(self.header_widget)
        self.dateEditStartPeriod.setCalendarPopup(True)
        self.dateEditStartPeriod.setObjectName("dateEditStartPeriod")
        self.gridLayout.addWidget(self.dateEditStartPeriod, 0, 10, 1, 1)
        self.lineEditSearchByProductName = QtWidgets.QLineEdit(self.header_widget)
        self.lineEditSearchByProductName.setObjectName("lineEditSearchByProductName")
        self.gridLayout.addWidget(self.lineEditSearchByProductName, 0, 6, 1, 1)
        self.BtnSearchByProductName = QtWidgets.QPushButton(self.header_widget)
        self.BtnSearchByProductName.setText("")
        self.BtnSearchByProductName.setIcon(icon)
        self.BtnSearchByProductName.setObjectName("BtnSearchByProductName")
        self.gridLayout.addWidget(self.BtnSearchByProductName, 0, 7, 1, 1)
        self.verticalLayout.addWidget(self.header_widget)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.main_widget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 958, 474))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_order_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.line_order_widget.setAutoFillBackground(False)
        self.line_order_widget.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.line_order_widget.setObjectName("line_order_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.line_order_widget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.BtnOpenOrder = QtWidgets.QPushButton(self.line_order_widget)
        self.BtnOpenOrder.setMaximumSize(QtCore.QSize(60, 60))
        self.BtnOpenOrder.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #808a9c;
                color: black;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #dae5f7;
                border: 1px solid #0a66fa;;
            }
        """)
        self.BtnOpenOrder.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/utils/icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnOpenOrder.setIcon(icon1)
        self.BtnOpenOrder.setIconSize(QtCore.QSize(23, 23))

        self.BtnOpenOrder.setObjectName("BtnOpenOrder")

        self.gridLayout_2.addWidget(self.BtnOpenOrder, 0, 4, 1, 1)
        self.label_customer = QtWidgets.QLabel(self.line_order_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_customer.setFont(font)
        self.label_customer.setObjectName("label_customer")
        self.gridLayout_2.addWidget(self.label_customer, 0, 1, 1, 1)
        self.label_product_1 = QtWidgets.QLabel(self.line_order_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_product_1.setFont(font)
        self.label_product_1.setObjectName("label_product_1")
        self.gridLayout_2.addWidget(self.label_product_1, 1, 1, 1, 1)
        self.label_product_2 = QtWidgets.QLabel(self.line_order_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_product_2.setFont(font)
        self.label_product_2.setObjectName("label_product_2")
        self.gridLayout_2.addWidget(self.label_product_2, 2, 1, 1, 1)
        self.label_product_3 = QtWidgets.QLabel(self.line_order_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_product_3.setFont(font)
        self.label_product_3.setObjectName("label_product_3")
        self.gridLayout_2.addWidget(self.label_product_3, 3, 1, 1, 1)

        self.BtnStatus = QtWidgets.QPushButton(self.line_order_widget)
        self.BtnStatus.setMaximumSize(QtCore.QSize(60, 60))
        self.BtnStatus.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 255, 127);
                border: 1px solid black;
            }
            QPushButton:hover {
                background-color: rgb(255, 220, 100);
            }
        """)
        self.BtnStatus.setText("")
        self.BtnStatus.setObjectName("BtnStatus")

        self.gridLayout_2.addWidget(self.BtnStatus, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.line_order_widget)
        spacerItem = QtWidgets.QSpacerItem(20, 252, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.main_widget)
        OrdersArchive.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrdersArchive)
        QtCore.QMetaObject.connectSlotsByName(OrdersArchive)

    def retranslateUi(self, OrdersArchive):
        _translate = QtCore.QCoreApplication.translate
        OrdersArchive.setWindowTitle(_translate("OrdersArchive", "Заказы"))
        self.lineEdit_4.setPlaceholderText(_translate("OrdersArchive", "№ счёта"))
        self.lineEdit_3.setPlaceholderText(_translate("OrdersArchive", "№ журн."))
        self.lineEditSearchByCustomer.setPlaceholderText(_translate("OrdersArchive", "Название организации заказчика"))
        self.label_by.setText(_translate("OrdersArchive", "по"))
        self.checkBoxPeriod.setText(_translate("OrdersArchive", "В период от"))
        self.lineEditSearchByProductName.setPlaceholderText(_translate("OrdersArchive", "Наименование изделия"))
        self.label_customer.setText(_translate("OrdersArchive", "34-142 / дата: 26.07.2024 / заказчик: ООО \"Белагро Бел\""))
        self.label_product_1.setText(_translate("OrdersArchive", "1. Изделие 1 - 1000 шт."))
        self.label_product_2.setText(_translate("OrdersArchive", "2. Изделие 2 - 1000 шт."))
        self.label_product_3.setText(_translate("OrdersArchive", "3. Изделие 3 - 1000 шт."))

class OrdersArchive(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OrdersArchive()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrdersArchive = QtWidgets.QMainWindow()
    ui = Ui_OrdersArchive()
    ui.setupUi(OrdersArchive)
    OrdersArchive.show()
    sys.exit(app.exec_())
