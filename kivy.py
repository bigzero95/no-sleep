#import kivy
#from kivy.app import App
#from kivy.uix.label import Label

#class KivyApp(App):
   # def build(self):
  #      return Label(text='KIVY LABEL TEST')
#if __name__ == '__main__':
 #   KivyApp().run()

#출처: https://digiconfactory.tistory.com/302 [코딩각]
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
#fontk = 'font/Cafe24Dangdanghae.ttf'
class KivyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(KivyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='title: ', font_name=fontk, font_size=30))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='good: ', font_name=fontk, font_size=30))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='writer: ', font_name=fontk, font_size=30))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class KivyApp(App):
    def build(self):
        return KivyGrid()

if __name__ == '__main__':
    KivyApp().run()

#출처: https://digiconfactory.tistory.com/302 [코딩각]