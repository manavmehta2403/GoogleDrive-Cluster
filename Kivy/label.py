from kivy.app import App 
from kivy.uix.widget import Widget
# import label and use it 
from kivy.uix.label import Label 

class lbl(Widget):
    pass
  
# defining the App class 
class LabelApp(App): 
    def build(self):
        return lbl()
  
if __name__=="__main__":
    LabelApp().run()