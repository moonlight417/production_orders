from PyQt5 import QtWidgets, QtCore
from products.models import Drawing, DrawingSheet, Tag
from .tags_tab_content import TagsTabContent
from .drawing_tab_widget import UnifiedDrawingTabWidget

class MainTabWidget(QtWidgets.QWidget):
    def __init__(self, ui, main_id):
        super().__init__()
        self.main_id = main_id
        self.ui = ui
        self.initialize_ui()

    def initialize_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        self.main_tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(self.main_tab_widget)

        self.tags_tab_content = TagsTabContent()
        self.main_tab_widget.addTab(self.tags_tab_content, "Теги")

        self.scroll_areas = {}
        self.tab_types = {}
        self.check_boxes = {}
        self.radio_buttons = {}

        self.main_name = ""
        self.linked_tab = None

    def create_tab(self, drawing):
        tab = QtWidgets.QWidget()
        tab.doc_name = drawing.doc_name
        tab.drawing_tab_widget = UnifiedDrawingTabWidget()

        layout = QtWidgets.QVBoxLayout(tab)
        layout.addWidget(tab.drawing_tab_widget)

        self.main_tab_widget.addTab(tab, drawing.doc_name)
        return tab

    def save_to_db(self):
        try:
            for i in range(self.main_tab_widget.count()):
                tab = self.main_tab_widget.widget(i)
                if hasattr(tab, 'drawing_tab_widget'):
                    drawing = Drawing.objects.get(doc_name=tab.doc_name)
                    for sheet_data in tab.drawing_tab_widget.get_inner_tabs_data():
                        DrawingSheet.objects.update_or_create(
                            drawing=drawing,
                            file=sheet_data['file'],
                            defaults={
                                'is_actual': sheet_data['is_actual'],
                                'mass': sheet_data['mass']
                            }
                        )
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {str(e)}")






    