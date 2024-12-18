
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_creatingALabel(object):
    def setupUi(self, creatingALabel):
        creatingALabel.setObjectName("creatingALabel")
        creatingALabel.resize(874, 521)
        self.centralwidget = QtWidgets.QWidget(creatingALabel)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBoxCreateLabel = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxCreateLabel.setGeometry(QtCore.QRect(15, 10, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxCreateLabel.setFont(font)
        self.checkBoxCreateLabel.setObjectName("checkBoxCreateLabel")
        self.frameLabel = QtWidgets.QFrame(self.centralwidget)
        self.frameLabel.setGeometry(QtCore.QRect(180, 20, 681, 371))
        self.frameLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLabel.setObjectName("frameLabel")
        self.labelNameOfProduct = QtWidgets.QLabel(self.frameLabel)
        self.labelNameOfProduct.setGeometry(QtCore.QRect(30, 105, 371, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.labelNameOfProduct.setFont(font)
        self.labelNameOfProduct.setObjectName("labelNameOfProduct")
        self.label_21 = QtWidgets.QLabel(self.frameLabel)
        self.label_21.setGeometry(QtCore.QRect(510, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_drawing_2 = QtWidgets.QLabel(self.frameLabel)
        self.label_drawing_2.setGeometry(QtCore.QRect(465, 40, 176, 176))
        self.label_drawing_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_drawing_2.setText("")
        self.label_drawing_2.setPixmap(QtGui.QPixmap("../utils/pic/our_website.png"))
        self.label_drawing_2.setScaledContents(True)
        self.label_drawing_2.setObjectName("label_drawing_2")
        self.label_35 = QtWidgets.QLabel(self.frameLabel)
        self.label_35.setGeometry(QtCore.QRect(495, 225, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.labelCustomer = QtWidgets.QLabel(self.frameLabel)
        self.labelCustomer.setGeometry(QtCore.QRect(30, 135, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCustomer.setFont(font)
        self.labelCustomer.setObjectName("labelCustomer")
        self.labelNetWeight = QtWidgets.QLabel(self.frameLabel)
        self.labelNetWeight.setGeometry(QtCore.QRect(495, 250, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelNetWeight.setFont(font)
        self.labelNetWeight.setObjectName("labelNetWeight")
        self.label = QtWidgets.QLabel(self.frameLabel)
        self.label.setGeometry(QtCore.QRect(570, 245, 30, 30))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../utils/pic/Antech_ru_020_Ves_Netto_(e).jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frameLabel)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 131, 66))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../utils/pic/Эмблема.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.frameLabel)
        self.frame.setGeometry(QtCore.QRect(25, 80, 226, 16))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelDateOfCheck = QtWidgets.QLabel(self.frame)
        self.labelDateOfCheck.setGeometry(QtCore.QRect(145, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.labelDateOfCheck.setFont(font)
        self.labelDateOfCheck.setObjectName("labelDateOfCheck")
        self.labelNumberOfCheck = QtWidgets.QLabel(self.frame)
        self.labelNumberOfCheck.setGeometry(QtCore.QRect(75, 0, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.labelNumberOfCheck.setFont(font)
        self.labelNumberOfCheck.setObjectName("labelNumberOfCheck")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(5, 0, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(115, 0, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_22 = QtWidgets.QLabel(self.frameLabel)
        self.label_22.setGeometry(QtCore.QRect(135, 15, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frameLabel)
        self.label_23.setGeometry(QtCore.QRect(140, 40, 231, 19))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_39 = QtWidgets.QLabel(self.frameLabel)
        self.label_39.setGeometry(QtCore.QRect(30, 160, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.frameLabel)
        self.label_41.setGeometry(QtCore.QRect(30, 185, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frameLabel)
        self.label_42.setGeometry(QtCore.QRect(30, 210, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frameLabel)
        self.label_43.setGeometry(QtCore.QRect(30, 235, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.labelDate = QtWidgets.QLabel(self.frameLabel)
        self.labelDate.setGeometry(QtCore.QRect(30, 260, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelDate.setFont(font)
        self.labelDate.setObjectName("labelDate")
        self.labelUmbrella = QtWidgets.QLabel(self.frameLabel)
        self.labelUmbrella.setGeometry(QtCore.QRect(420, 290, 71, 66))
        self.labelUmbrella.setText("")
        self.labelUmbrella.setPixmap(QtGui.QPixmap("../utils/pic/Berech_ot_vlagi.jpg"))
        self.labelUmbrella.setScaledContents(True)
        self.labelUmbrella.setObjectName("labelUmbrella")
        self.labelEnptyBorder = QtWidgets.QLabel(self.frameLabel)
        self.labelEnptyBorder.setEnabled(True)
        self.labelEnptyBorder.setGeometry(QtCore.QRect(30, 290, 341, 66))
        self.labelEnptyBorder.setFrameShape(QtWidgets.QFrame.Box)
        self.labelEnptyBorder.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelEnptyBorder.setLineWidth(2)
        self.labelEnptyBorder.setMidLineWidth(3)
        self.labelEnptyBorder.setText("")
        self.labelEnptyBorder.setScaledContents(False)
        self.labelEnptyBorder.setObjectName("labelEnptyBorder")
        self.labelDelicate = QtWidgets.QLabel(self.frameLabel)
        self.labelDelicate.setGeometry(QtCore.QRect(500, 290, 71, 66))
        self.labelDelicate.setText("")
        self.labelDelicate.setPixmap(QtGui.QPixmap("../utils/pic/Antech_ru_040_Ostorozhno_hrupkoe.jpg"))
        self.labelDelicate.setScaledContents(True)
        self.labelDelicate.setObjectName("labelDelicate")
        self.labelHandleWithCare = QtWidgets.QLabel(self.frameLabel)
        self.labelHandleWithCare.setGeometry(QtCore.QRect(580, 290, 71, 66))
        self.labelHandleWithCare.setText("")
        self.labelHandleWithCare.setPixmap(QtGui.QPixmap("../utils/pic/Antech_ru_025_Verkh_(This side up).jpg"))
        self.labelHandleWithCare.setScaledContents(True)
        self.labelHandleWithCare.setObjectName("labelHandleWithCare")
        self.label_21.raise_()
        self.label_drawing_2.raise_()
        self.label_35.raise_()
        self.labelCustomer.raise_()
        self.labelNameOfProduct.raise_()
        self.labelNetWeight.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.frame.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_39.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.labelDate.raise_()
        self.labelUmbrella.raise_()
        self.labelEnptyBorder.raise_()
        self.labelDelicate.raise_()
        self.labelHandleWithCare.raise_()
        self.BtnEndOfDesigning = QtWidgets.QPushButton(self.centralwidget)
        self.BtnEndOfDesigning.setGeometry(QtCore.QRect(635, 450, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BtnEndOfDesigning.setFont(font)
        self.BtnEndOfDesigning.setObjectName("BtnEndOfDesigning")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(25, 450, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnUmbrella = QtWidgets.QPushButton(self.centralwidget)
        self.btnUmbrella.setGeometry(QtCore.QRect(40, 145, 81, 76))
        self.btnUmbrella.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../utils/pic/Berech_ot_vlagi.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUmbrella.setIcon(icon)
        self.btnUmbrella.setIconSize(QtCore.QSize(50, 50))
        self.btnUmbrella.setCheckable(True)
        self.btnUmbrella.setObjectName("btnUmbrella")
        self.btnDelicate = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelicate.setGeometry(QtCore.QRect(40, 230, 81, 76))
        self.btnDelicate.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../utils/pic/Antech_ru_040_Ostorozhno_hrupkoe.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelicate.setIcon(icon1)
        self.btnDelicate.setIconSize(QtCore.QSize(50, 50))
        self.btnDelicate.setCheckable(True)
        self.btnDelicate.setObjectName("btnDelicate")
        self.btnHandleWithCare = QtWidgets.QPushButton(self.centralwidget)
        self.btnHandleWithCare.setGeometry(QtCore.QRect(40, 315, 81, 76))
        self.btnHandleWithCare.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../utils/pic/Antech_ru_025_Verkh_(This side up).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHandleWithCare.setIcon(icon2)
        self.btnHandleWithCare.setIconSize(QtCore.QSize(50, 50))
        self.btnHandleWithCare.setCheckable(True)
        self.btnHandleWithCare.setObjectName("btnHandleWithCare")
        self.btnEnptyBorder = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnptyBorder.setGeometry(QtCore.QRect(40, 60, 81, 76))
        self.btnEnptyBorder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../utils/pic/Border.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnptyBorder.setIcon(icon3)
        self.btnEnptyBorder.setIconSize(QtCore.QSize(50, 50))
        self.btnEnptyBorder.setCheckable(True)
        self.btnEnptyBorder.setObjectName("btnEnptyBorder")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 35, 141, 16))
        self.label_5.setObjectName("label_5")
        creatingALabel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(creatingALabel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menubar.setObjectName("menubar")
        creatingALabel.setMenuBar(self.menubar)

        self.retranslateUi(creatingALabel)
        QtCore.QMetaObject.connectSlotsByName(creatingALabel)

    def retranslateUi(self, creatingALabel):
        _translate = QtCore.QCoreApplication.translate
        creatingALabel.setWindowTitle(_translate("creatingALabel", "Формирование этикетки"))
        self.checkBoxCreateLabel.setText(_translate("creatingALabel", "Создать этикетку"))
        self.labelNameOfProduct.setText(_translate("creatingALabel", "Нож КСША 40.00.004                                              "))
        self.label_21.setText(_translate("creatingALabel", "Наш сайт"))
        self.label_35.setText(_translate("creatingALabel", "МАССА НЕТТО:"))
        self.labelCustomer.setText(_translate("creatingALabel", "ООО \"Белагро Бел\""))
        self.labelNetWeight.setText(_translate("creatingALabel", "40 КГ"))
        self.labelDateOfCheck.setText(_translate("creatingALabel", "26.07.2024"))
        self.labelNumberOfCheck.setText(_translate("creatingALabel", "230"))
        self.label_26.setText(_translate("creatingALabel", "Заказ №"))
        self.label_29.setText(_translate("creatingALabel", "от"))
        self.label_22.setText(_translate("creatingALabel", "ООО ПКФ \"ГРИФ-АГРО\""))
        self.label_23.setText(_translate("creatingALabel", "г. Витебск, ул. Лазо 105, оф. 14"))
        self.label_39.setText(_translate("creatingALabel", "Количество:         шт."))
        self.label_41.setText(_translate("creatingALabel", "Вся партия:         шт."))
        self.label_42.setText(_translate("creatingALabel", "Упаковщик:"))
        self.label_43.setText(_translate("creatingALabel", "Дата изготовления:"))
        self.labelDate.setText(_translate("creatingALabel", "НОЯБРЬ 2024 г."))
        self.BtnEndOfDesigning.setText(_translate("creatingALabel", "Закончить разработку заказа"))
        self.btnBack.setText(_translate("creatingALabel", "Назад"))
        self.label_5.setText(_translate("creatingALabel", "Добавить/убрать элемент:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    creatingALabel = QtWidgets.QMainWindow()
    ui = Ui_creatingALabel()
    ui.setupUi(creatingALabel)
    creatingALabel.show()
    sys.exit(app.exec_())
