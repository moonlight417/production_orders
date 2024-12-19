
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskFilling(object):
    def setupUi(self, TaskFilling):
        TaskFilling.setObjectName("TaskFilling")
        TaskFilling.resize(641, 785)
        self.centralwidget = QtWidgets.QWidget(TaskFilling)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 80, 621, 21))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.labelProduct = QtWidgets.QLabel(self.frame_3)
        self.labelProduct.setGeometry(QtCore.QRect(230, 0, 51, 16))
        self.labelProduct.setObjectName("labelProduct")
        self.labelQuantity = QtWidgets.QLabel(self.frame_3)
        self.labelQuantity.setGeometry(QtCore.QRect(475, 0, 61, 16))
        self.labelQuantity.setObjectName("labelQuantity")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 621, 551))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 602, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 581, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frameProductLine = QtWidgets.QFrame(self.frame_4)
        self.frameProductLine.setGeometry(QtCore.QRect(0, 0, 581, 41))
        self.frameProductLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.frameProductLine.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameProductLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameProductLine.setLineWidth(2)
        self.frameProductLine.setMidLineWidth(1)
        self.frameProductLine.setObjectName("frameProductLine")
        self.line_8 = QtWidgets.QFrame(self.frameProductLine)
        self.line_8.setGeometry(QtCore.QRect(530, 1, 18, 39))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.spinBoxQuantity = QtWidgets.QSpinBox(self.frameProductLine)
        self.spinBoxQuantity.setGeometry(QtCore.QRect(460, 10, 71, 22))
        self.spinBoxQuantity.setMaximum(1000000)
        self.spinBoxQuantity.setSingleStep(10)
        self.spinBoxQuantity.setObjectName("spinBoxQuantity")
        self.LbNumber = QtWidgets.QLabel(self.frameProductLine)
        self.LbNumber.setGeometry(QtCore.QRect(10, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LbNumber.setFont(font)
        self.LbNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.LbNumber.setObjectName("LbNumber")
        self.lineEditNameOfProduct = QtWidgets.QLineEdit(self.frameProductLine)
        self.lineEditNameOfProduct.setGeometry(QtCore.QRect(40, 10, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditNameOfProduct.setFont(font)
        self.lineEditNameOfProduct.setObjectName("lineEditNameOfProduct")
        self.BtnDeleteLine = QtWidgets.QPushButton(self.frame_4)
        self.BtnDeleteLine.setGeometry(QtCore.QRect(545, 5, 31, 31))
        self.BtnDeleteLine.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../utils/icons/x-square.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("x-square.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.BtnDeleteLine.setIcon(icon)
        self.BtnDeleteLine.setObjectName("BtnDeleteLine")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.BtnForDeveloping = QtWidgets.QPushButton(self.centralwidget)
        self.BtnForDeveloping.setGeometry(QtCore.QRect(520, 720, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnForDeveloping.setFont(font)
        self.BtnForDeveloping.setObjectName("BtnForDeveloping")
        self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
        self.BtnBack.setGeometry(QtCore.QRect(10, 720, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnBack.setFont(font)
        self.BtnBack.setObjectName("BtnBack")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 30, 621, 51))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frameCustomer = QtWidgets.QFrame(self.frame_5)
        self.frameCustomer.setGeometry(QtCore.QRect(0, 0, 621, 41))
        self.frameCustomer.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.frameCustomer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCustomer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameCustomer.setLineWidth(2)
        self.frameCustomer.setMidLineWidth(1)
        self.frameCustomer.setObjectName("frameCustomer")
        self.LbCheckNumber = QtWidgets.QLabel(self.frameCustomer)
        self.LbCheckNumber.setGeometry(QtCore.QRect(10, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LbCheckNumber.setFont(font)
        self.LbCheckNumber.setObjectName("LbCheckNumber")
        self.dateEditDate = QtWidgets.QDateEdit(self.frameCustomer)
        self.dateEditDate.setGeometry(QtCore.QRect(55, 10, 81, 22))
        self.dateEditDate.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditDate.setCalendarPopup(True)
        self.dateEditDate.setObjectName("dateEditDate")
        self.lineEditCustomer = QtWidgets.QLineEdit(self.frameCustomer)
        self.lineEditCustomer.setGeometry(QtCore.QRect(150, 10, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCustomer.setFont(font)
        self.lineEditCustomer.setObjectName("lineEditCustomer")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 561, 21))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.labelCheckNumber = QtWidgets.QLabel(self.frame_6)
        self.labelCheckNumber.setGeometry(QtCore.QRect(0, 0, 51, 16))
        self.labelCheckNumber.setObjectName("labelCheckNumber")
        self.labelDate = QtWidgets.QLabel(self.frame_6)
        self.labelDate.setGeometry(QtCore.QRect(80, 0, 31, 16))
        self.labelDate.setObjectName("labelDate")
        self.labelCustomer = QtWidgets.QLabel(self.frame_6)
        self.labelCustomer.setGeometry(QtCore.QRect(260, 0, 171, 16))
        self.labelCustomer.setObjectName("labelCustomer")
        self.BtnAddNewProduct = QtWidgets.QPushButton(self.centralwidget)
        self.BtnAddNewProduct.setGeometry(QtCore.QRect(20, 660, 41, 41))
        self.BtnAddNewProduct.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../utils/icons/plus-square-dotted.svg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("plus-square-dotted.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.BtnAddNewProduct.setIcon(icon1)
        self.BtnAddNewProduct.setIconSize(QtCore.QSize(23, 23))
        self.BtnAddNewProduct.setObjectName("BtnAddNewProduct")
        self.labelAddNewProduct = QtWidgets.QLabel(self.centralwidget)
        self.labelAddNewProduct.setGeometry(QtCore.QRect(80, 670, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAddNewProduct.setFont(font)
        self.labelAddNewProduct.setObjectName("labelAddNewProduct")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 700, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        TaskFilling.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaskFilling)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 21))
        self.menubar.setObjectName("menubar")
        TaskFilling.setMenuBar(self.menubar)

        self.retranslateUi(TaskFilling)
        QtCore.QMetaObject.connectSlotsByName(TaskFilling)

    def retranslateUi(self, TaskFilling):
        _translate = QtCore.QCoreApplication.translate
        TaskFilling.setWindowTitle(_translate("TaskFilling", "Оформление задания"))
        self.labelProduct.setText(_translate("TaskFilling", "Изделие"))
        self.labelQuantity.setText(_translate("TaskFilling", "Количество"))
        self.LbNumber.setText(_translate("TaskFilling", "1"))
        self.lineEditNameOfProduct.setText(_translate("TaskFilling", "Нож КСША 40.00.004"))
        self.BtnForDeveloping.setText(_translate("TaskFilling", "На разработку"))
        self.BtnBack.setText(_translate("TaskFilling", "Назад"))
        self.LbCheckNumber.setText(_translate("TaskFilling", "142"))
        self.lineEditCustomer.setText(_translate("TaskFilling", "ООО \"Белагро Бел\""))
        self.labelCheckNumber.setText(_translate("TaskFilling", "№ счёта"))
        self.labelDate.setText(_translate("TaskFilling", "Дата"))
        self.labelCustomer.setText(_translate("TaskFilling", "Название организации заказчика"))
        self.labelAddNewProduct.setText(_translate("TaskFilling", "Добавить новое изделие в задание"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskFilling = QtWidgets.QMainWindow()
    ui = Ui_TaskFilling()
    ui.setupUi(TaskFilling)
    TaskFilling.show()
    sys.exit(app.exec_())
