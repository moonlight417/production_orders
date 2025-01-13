from PyQt5 import QtCore, QtGui, QtWidgets
from gui.ui_design_document_filling_form import Ui_DesignDocumentFillingForm
from tab_manager import TabManager
import sys

class ImageHandler:
    def __init__(self, label_image):
        self.label_image = label_image
        self.rotation_angle = 0
        self.current_image_path = ""

    def open_file(self):
        """Открыть изображение и отобразить в QLabel."""
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Выберите файл", "../utils/drawings/",
            "Изображения (*.png *.jpg *.bmp *.gif)"
        )
        if file_path:
            self.current_image_path = file_path
            self.rotation_angle = 0
            self.update_image()
        else:
            print("Файл не выбран")

    def update_image(self):
        """Обновление изображения с учетом поворота."""
        if not self.current_image_path:
            return
        pixmap = QtGui.QPixmap(self.current_image_path)
        if self.rotation_angle != 0:
            transform = QtGui.QTransform()
            transform.rotate(self.rotation_angle)
            pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        scaled_pixmap = pixmap.scaled(self.label_image.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_image.setPixmap(scaled_pixmap)

    def rotate_left(self):
        """Поворот изображения влево."""
        self.rotation_angle -= 90
        self.rotation_angle %= 360
        self.update_image()

    def rotate_right(self):
        """Поворот изображения вправо."""
        self.rotation_angle += 90
        self.rotation_angle %= 360
        self.update_image()


class DesignDocumentFillingForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DesignDocumentFillingForm()
        self.ui.setupUi(self)

        self.tab_manager = TabManager(self.ui.tabWidget)  # Менеджер вкладок
        self.image_handler = ImageHandler(self.ui.label_image)  # Обработчик изображений

        self.setup_connections()

    def setup_connections(self):
        """Подключение сигналов к методам."""
        self.ui.BtnAddDetail.clicked.connect(self.tab_manager.add_tab_detail)
        self.ui.BtnAddAssemblyUnit.clicked.connect(self.tab_manager.add_tab_assembly_unit)
        self.ui.BtnEditTabName.clicked.connect(self.tab_manager.save_tab_name)

        self.ui.BtnRotateLeft.clicked.connect(self.image_handler.rotate_left)
        self.ui.BtnRotateRight.clicked.connect(self.image_handler.rotate_right)
        self.ui.BtnOpenFile.clicked.connect(self.image_handler.open_file)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignDocumentFillingForm()
    window.show()
    sys.exit(app.exec_())
