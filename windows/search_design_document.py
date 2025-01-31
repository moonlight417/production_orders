
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFrame, QVBoxLayout, QLabel, QPushButton, QWidget, QSizePolicy
import resources_rc
from products.models import MainDocument, Tag, Drawing, DrawingSheet
from windows.document_editor import DocumentEditor


class Ui_SearchDesignDoc(object):
    def setupUi(self, SearchDesignDoc):
        SearchDesignDoc.setObjectName("SearchDesignDoc")
        SearchDesignDoc.resize(1132, 698)

        self.centralwidget = QtWidgets.QWidget(SearchDesignDoc)
        self.centralwidget.setObjectName("centralwidget")

        # Главный вертикальный layout для размещения всех виджетов
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(0, 0, 0, 10)
        main_layout.setSpacing(10)

        # ======= Шапка с виджетами =======
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setMinimumHeight(80)  # Устанавливаем минимальную высоту для шапки
        self.frame_3.setObjectName("frame_3")

        # Горизонтальный layout для шапки
        header_layout = QtWidgets.QHBoxLayout(self.frame_3)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(10)

        self.labelSearchByName = QtWidgets.QLabel(self.frame_3)
        # self.labelSearchByName.setGeometry(QtCore.QRect(90, -1, 101, 20))
        self.labelSearchByName.setObjectName("labelSearchByName")
        header_layout.addWidget(self.labelSearchByName)

        self.lineEditSearchByName = QtWidgets.QLineEdit(self.frame_3)
        # self.lineEditSearchByName.setGeometry(QtCore.QRect(10, 19, 301, 21))
        self.lineEditSearchByName.setObjectName("lineEditSearchByName")
        header_layout.addWidget(self.lineEditSearchByName)

        self.BtnSearchByName = QtWidgets.QPushButton(self.frame_3)
        # self.BtnSearchByName.setGeometry(QtCore.QRect(315, 9, 31, 31))
        self.BtnSearchByName.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/utils/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnSearchByName.setIcon(icon)
        self.BtnSearchByName.setObjectName("BtnSearchByName")
        header_layout.addWidget(self.BtnSearchByName)

        self.labelSearchByTag = QtWidgets.QLabel(self.frame_3)
        # self.labelSearchByTag.setGeometry(QtCore.QRect(410, -1, 71, 20))
        self.labelSearchByTag.setObjectName("labelSearchByTag")
        header_layout.addWidget(self.labelSearchByTag)

        self.lineEditSearchByTag = QtWidgets.QLineEdit(self.frame_3)
        # self.lineEditSearchByTag.setGeometry(QtCore.QRect(360, 19, 161, 21))
        self.lineEditSearchByTag.setObjectName("lineEditSearchByTag")
        header_layout.addWidget(self.lineEditSearchByTag)

        self.BtnSearchByTag = QtWidgets.QPushButton(self.frame_3)
        # self.BtnSearchByTag.setGeometry(QtCore.QRect(525, 10, 31, 31))
        self.BtnSearchByTag.setText("")
        self.BtnSearchByTag.setIcon(icon)
        self.BtnSearchByTag.setObjectName("BtnSearchByTag")
        header_layout.addWidget(self.BtnSearchByTag)

        # Добавляем шапку в главный layout
        main_layout.addWidget(self.frame_3)

        # ======= Прокручиваемая область =======
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("""
                    QScrollArea {
                        background-color: #383838;
                    }
                    QScrollArea::widget {
                        background-color: #383838;
                    }
                    QScrollBar {
                        background-color: #d0d0d0;
                        width: 12px;
                    }
                    QScrollBar::handle {
                        background-color: #888888;
                        border-radius: 6px;
                    }
                    QScrollBar::add-line, QScrollBar::sub-line {
                        background-color: #a0a0a0;
                    }
                """)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutTask = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.layoutTask.setContentsMargins(5, 5, 5, 5)
        self.layoutTask.setSpacing(5)
        self.scrollAreaWidgetContents.setLayout(self.layoutTask)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Добавляем scrollArea в главный layout
        main_layout.addWidget(self.scrollArea)

        # self.frameLineDesignDoc = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.frameLineDesignDoc.setGeometry(QtCore.QRect(0, 0, 696, 41))
        # self.frameLineDesignDoc.setStyleSheet("background-color: rgb(247, 247, 247);")
        # self.frameLineDesignDoc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frameLineDesignDoc.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frameLineDesignDoc.setObjectName("frameLineDesignDoc")
        #
        # self.LbDesignDocName = QtWidgets.QLabel(self.frameLineDesignDoc)
        # self.LbDesignDocName.setGeometry(QtCore.QRect(10, 10, 601, 16))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.LbDesignDocName.setFont(font)
        # self.LbDesignDocName.setObjectName("LbDesignDocName")
        #
        # self.BtnDocOpen = QtWidgets.QPushButton(self.frameLineDesignDoc)
        # self.BtnDocOpen.setGeometry(QtCore.QRect(665, 5, 31, 31))
        # self.BtnDocOpen.setText("")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap("../utils/icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.BtnDocOpen.setIcon(icon1)
        # self.BtnDocOpen.setIconSize(QtCore.QSize(23, 23))
        # self.BtnDocOpen.setObjectName("BtnDocOpen")
        #
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # # self.BtnBack = QtWidgets.QPushButton(self.centralwidget)
        # # self.BtnBack.setGeometry(QtCore.QRect(10, 620, 111, 31))
        # # font = QtGui.QFont()
        # # font.setPointSize(10)
        # # self.BtnBack.setFont(font)
        # # self.BtnBack.setObjectName("BtnBack")
        # self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        # self.frame_2.setGeometry(QtCore.QRect(530, 610, 151, 31))
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")
        # # self.BtnAddNewDoc = QtWidgets.QPushButton(self.centralwidget)
        # # self.BtnAddNewDoc.setGeometry(QtCore.QRect(570, 10, 161, 31))
        # # font = QtGui.QFont()
        # # font.setPointSize(10)
        # # self.BtnAddNewDoc.setFont(font)
        # # self.BtnAddNewDoc.setObjectName("BtnAddNewDoc")
        # self.LbSearchInfo = QtWidgets.QLabel(self.centralwidget)
        # self.LbSearchInfo.setGeometry(QtCore.QRect(570, 620, 116, 16))
        # self.LbSearchInfo.setObjectName("LbSearchInfo")

        SearchDesignDoc.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(SearchDesignDoc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName("menubar")
        SearchDesignDoc.setMenuBar(self.menubar)

        self.retranslateUi(SearchDesignDoc)
        QtCore.QMetaObject.connectSlotsByName(SearchDesignDoc)

    def retranslateUi(self, SearchDesignDoc):
        _translate = QtCore.QCoreApplication.translate
        SearchDesignDoc.setWindowTitle(_translate("SearchDesignDoc", "Поиск документа"))
        self.labelSearchByName.setText(_translate("SearchDesignDoc", "Поиск по названию"))
        self.labelSearchByTag.setText(_translate("SearchDesignDoc", "Поиск по тегу"))
        # self.LbDesignDocName.setText(_translate("SearchDesignDoc", "Название документа"))
        # self.BtnBack.setText(_translate("SearchDesignDoc", "Назад"))
        # self.BtnAddNewDoc.setText(_translate("SearchDesignDoc", "Добавить новую запись"))
        # self.LbSearchInfo.setText(_translate("SearchDesignDoc", "Найдено 12 записей"))

class SearchDesignDoc(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_SearchDesignDoc()
        self.ui.setupUi(self)
        self.parent = parent  # Сохраняем ссылку на родительское окно

        self.ui.BtnSearchByName.clicked.connect(self.search_design_document_by_main_name)
        self.ui.BtnSearchByTag.clicked.connect(self.search_design_document_by_tag)
        # self.ui.BtnBack.clicked.connect(self.go_back)
        # self.ui.BtnAddNewDoc.clicked.connect(self.design_document_filling_window)

    # def design_document_filling_window(self):
    #     try:
    #         from design_document_filling_form import DesignDocumentFillingForm
    #         self.design_document_filling = DesignDocumentFillingForm(parent=self)
    #         self.design_document_filling.show()
    #         self.close()
    #     except Exception as e:
    #         QMessageBox.critical(self, "Ошибка", f"Не удалось открыть окно поиска КД: {e}")

    # def go_back(self):
    #     self.parent.show()  # Показываем родительское окно
    #     self.close()  # Закрываем дочернее окно

    from PyQt5.QtWidgets import QMessageBox
    from products.models import MainDocument  # Импорт модели

    from PyQt5.QtWidgets import QMessageBox, QLabel, QPushButton, QFrame, QWidget, QSizePolicy, QVBoxLayout
    from PyQt5 import QtWidgets, QtCore
    from products.models import MainDocument

    def search_design_document_by_main_name(self):
        """Ищет конструкторский документ в базе данных по имени главного документа."""
        document_main_name = self.ui.lineEditSearchByName.text().strip()

        if not document_main_name:
            QMessageBox.warning(self, "Ошибка", "Введите название документа.")
            return

        try:
            # 🔹 Ищем документы напрямую в базе данных (по вхождению текста)
            documents = MainDocument.objects.filter(main_name__icontains=document_main_name)

            if documents.exists():
                # 🔹 Формируем список результатов
                data = [
                    {"id": doc.id, "name": doc.main_name, "comment": doc.comment}
                    for doc in documents
                ]
                self.update_document_list(data)  # Обновляем интерфейс
            else:
                QMessageBox.information(self, "Результат", "Документ не найден.")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка поиска: {e}")

    def update_document_list(self, documents):
        """
        Обновление списка конструкторских документов в прокручиваемой области.
        :param documents: Список найденных конструкторских документов.
        """
        # Очистка текущего списка
        for i in reversed(range(self.ui.layoutTask.count())):
            widget = self.ui.layoutTask.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Добавление новых документов
        for document in reversed(documents):
            # Создаем рамку для документа
            document_frame = QFrame()
            document_frame.setFrameShape(QFrame.StyledPanel)
            document_frame.setStyleSheet("border: 1.5px solid #666666; padding: 1px; margin: 1px;")

            # Вертикальный layout для документа
            document_layout = QVBoxLayout(document_frame)

            # Верхняя часть документа: название и комментарий
            document_info = QLabel(f"Документ: {document['name']} / Комментарий: {document['comment']}")
            document_info.setStyleSheet(
                "font-size: 14px; font-weight: bold; background: white; border: 1px solid #ff0f0f; margin: 3px;")
            document_info.setFixedHeight(34)
            document_layout.addWidget(document_info)

            # Кнопка для открытия окна редактирования документа
            edit_button = QPushButton("Открыть")
            edit_button.clicked.connect(lambda checked, doc_id=document['id']: self.open_document_editor(doc_id))
            document_layout.addWidget(edit_button, alignment=QtCore.Qt.AlignRight)
            edit_button.setFixedSize(80, 30)  # ширина: 80px, высота: 30px

            # Добавляем рамку документа в общий layout
            self.ui.layoutTask.addWidget(document_frame)

        # Пустой заполнитель
        self.empty_placeholder = QWidget()
        self.empty_placeholder.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.layoutTask.addWidget(self.empty_placeholder)  # Добавляем заполнитель в конец layout

    def search_design_document_by_tag(self):
        """Ищет конструкторские документы по тегу."""
        tag_name = self.ui.lineEditSearchByTag.text().strip()

        if not tag_name:
            QMessageBox.warning(self, "Ошибка", "Введите название тега.")
            return

        try:
            # 🔹 Ищем документы, связанные с тегом
            documents = MainDocument.objects.filter(tags__name__icontains=tag_name).distinct()

            if documents.exists():
                # 🔹 Формируем список результатов
                data = [
                    {"id": doc.id, "name": doc.main_name, "comment": doc.comment}
                    for doc in documents
                ]
                self.update_document_list(data)  # Обновляем интерфейс
            else:
                QMessageBox.information(self, "Результат", "Документы с таким тегом не найдены.")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка поиска: {e}")

    def open_document_editor(self, doc_id):
        """Открывает редактор документа внутри текущего окна."""
        print(f"📂 Открываем редактор документа с ID: {doc_id}")
        self.document_editor = DocumentEditor(doc_id, self)
        print("✅ Окно DocumentEditor создано, сейчас откроем его...")
        self.document_editor.exec_()
        print("✅ Окно DocumentEditor закрыто")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchDesignDoc = QtWidgets.QMainWindow()
    ui = Ui_SearchDesignDoc()
    ui.setupUi(SearchDesignDoc)
    SearchDesignDoc.show()
    sys.exit(app.exec_())
