
from utilities.common import Common
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp


class TryMeContent(BoxLayout):
    pass


class TM0App(MDApp, Common):
    def __init__(self):
        super().__init__()

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return TryMeContent()


if __name__ == '__main__':
    TM0App().run()



