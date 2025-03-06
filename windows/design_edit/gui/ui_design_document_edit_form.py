from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DesignDocumentEditForm(object):
    def setupUi(self, DesignDocumentEditForm):
        DesignDocumentEditForm.setObjectName("DesignDocumentEditForm")
        DesignDocumentEditForm.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(DesignDocumentEditForm)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.textEditComments = QtWidgets.QTextEdit(self.centralwidget)
        self.BtnSave = QtWidgets.QPushButton("Сохранить", self.centralwidget)

        self.gridLayout.addWidget(self.textEditComments, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.BtnSave, 1, 0, 1, 1)

        DesignDocumentEditForm.setCentralWidget(self.centralwidget)