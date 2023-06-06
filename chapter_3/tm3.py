
from utilities.common import Common
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable


class TryMeContent(BoxLayout):
    pass


class TM3App(MDApp, Common):
    def __init__(self):
        super().__init__()

    # ############################################################### navbar top-right tip

    def tip_dialog(self, title, tip):
        dialog = MDDialog(
            title=title,
            text='[color=222222]' + tip,
            buttons=[
                MDFlatButton(
                    text='Dismiss',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def callback_top_nav(self, x):
        self.root.ids.screen_manager.current = x

    # ############################################################## input boxes

    def data_entry_inputs(self):
        de_date = str(self.root.ids.de_date.text)
        de_nm = str(self.root.ids.de_name.text)
        de_age = str(self.root.ids.de_age.text)
        de_city = str(self.root.ids.de_city.text)
        data_input = [de_date, de_nm, de_age, de_city]
        return data_input

    def data_entry_check(self, x):
        data_input = self.data_entry_inputs()
        table = MDDataTable(
            use_pagination=True,
            column_data=[
                ('Input', dp(35)),
                ('Value', dp(35))
            ],
            row_data=[
                ('Date', data_input[0]),
                ('Name', data_input[1]),
                ('Age', data_input[2]),
                ('City', data_input[3])
            ]
        )

        if x == 'same_screen':
            self.root.ids.input_check_table.clear_widgets()
            self.root.ids.input_check_table.add_widget(table)
        else:
            self.callback_top_nav(x)
            self.root.ids.new_screen.clear_widgets()
            self.root.ids.new_screen.add_widget(table)

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return TryMeContent()


if __name__ == '__main__':
    TM3App().run()
