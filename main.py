from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 0, 0, 1)
        return Widget()

if __name__ == '__main__':
    MainApp().run()
