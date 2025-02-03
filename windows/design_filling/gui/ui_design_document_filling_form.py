from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

class Ui_DesignDocumentFillingForm(object):
    def setupUi(self, DesignDocumentFillingForm):
        DesignDocumentFillingForm.setObjectName("DesignDocumentFillingForm")
        DesignDocumentFillingForm.resize(1027, 791)

        self.centralwidget = QtWidgets.QWidget(DesignDocumentFillingForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")


        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)



        # Первый виджет
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)

        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout.setSpacing(0)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout")

        # spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout.addItem(spacerItem2)

        # self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget_2)

        # Второй виджет
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout_7.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.widget_3)

        # Третий виджет
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 70))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 10, -1)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEditComments = QtWidgets.QTextEdit(self.widget)
        self.textEditComments.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEditComments.setObjectName("textEditComents")
        self.horizontalLayout_5.addWidget(self.textEditComments)
        self.BtnSave = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnSave.sizePolicy().hasHeightForWidth())
        self.BtnSave.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BtnSave.setFont(font)
        self.BtnSave.setToolTipDuration(3000)
        self.BtnSave.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/utils/icons/floppy.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSave.setIcon(icon6)
        self.BtnSave.setIconSize(QtCore.QSize(30, 30))
        self.BtnSave.setObjectName("BtnSave")
        self.horizontalLayout_5.addWidget(self.BtnSave)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget)

        DesignDocumentFillingForm.setCentralWidget(self.centralwidget)
        self.retranslateUi(DesignDocumentFillingForm)
        QtCore.QMetaObject.connectSlotsByName(DesignDocumentFillingForm)


    def retranslateUi(self, DesignDocumentFillingForm):
        _translate = QtCore.QCoreApplication.translate
        DesignDocumentFillingForm.setWindowTitle(_translate("DesignDocumentFillingForm", "MainWindow"))
        self.textEditComments.setPlaceholderText(_translate("DesignDocumentFillingForm", "Комментарии"))
        self.BtnSave.setToolTip(_translate("DesignDocumentFillingForm", "Сохранить документ"))