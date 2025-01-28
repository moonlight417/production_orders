def get_tabs_data(self):
    tabs_data = []

    # Проходим по всем вкладкам верхнего уровня
    for i in range(self.main_tab_widget.count()):
        # Получаем виджет текущей вкладки
        tab = self.main_tab_widget.widget(i)

        # Пропускаем вкладку "Теги"
        if self.main_tab_widget.tabText(i) == "Теги":
            continue

        # Ищем поле ввода массы в дочерних вкладках
        mass_input = self._find_mass_input(tab)
        # Найдем объект Drawing и передадим его ID
        # parent_drawing_id = Drawing.objects.get(doc_name=self.selected_radio_button).id

        # Найдем объект Drawing по имени или ID, привязанному к радиокнопке
        # parent_drawing = Drawing.objects.get(doc_name=self.selected_radio_button)

        # Собираем данные вкладки
        tab_data = {
            'doc_name': self.main_tab_widget.tabText(i),  # Имя вкладки
            'mass': mass_input.text() if mass_input else None,  # Масса
            'assembly_unit': tab.is_assembly_unit if hasattr(tab, 'is_assembly_unit') else False,
            # Сборочная единица
            # 'parent': self._get_parent_value(tab)  # Родительская радиокнопка
            'parent': self.selected_radio_button if tab in self.radio_buttons and tab in self.check_boxes and
                                                    self.check_boxes[tab].isChecked() else None  # Родитель

            # # Теперь передаем объект Drawing как родительский
            # 'parent': parent_drawing if tab in self.radio_buttons and tab in self.check_boxes and self.check_boxes[
            #     tab].isChecked() else None

            # # Передаем ID родительского чертежа
            # 'parent': parent_drawing_id if tab in self.radio_buttons and tab in self.check_boxes and
            #                                self.check_boxes[
            #                                    tab].isChecked() else None
        }

        tabs_data.append(tab_data)

    return tabs_data
