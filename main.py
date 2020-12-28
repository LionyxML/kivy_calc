from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from math import *
from math import degrees, radians


color = ([.4, .5, .7, 1], [.7, .8, 1, 1], [.95, .98, 1, 1], [1, .7, .7, 1])

class CalculadoraForm(GridLayout):
    def __init__(self, **kwargs):
        super(CalculadoraForm, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        self.padding = [20, 20, 20, 20]
        self.spacing = [20, 20]
        
        self.resultado = Label(text='', font_size=100,
            color=color[2], size_hint_y=.5)
        self.add_widget(self.resultado)
        self.nums = []
        self.pad = GridLayout(cols=4, rows=11, spacing=[3, 3])
        self.ans = 0.0
        self.processa = ""


        def callback(instance):
            if instance.text == '=' or instance.text ==')=':
                if instance.text == ')=':
                    self.resultado.text += ')'
                try:
                    self.processa = str(self.resultado.text.replace('ANS', str(self.ans)))
                    self.processa = str(self.resultado.text.replace('^', '**'))
                    self.ans = float(eval(self.processa))
                    self.resultado.text = "{:.3e}".format(self.ans)
                except:
                    self.resultado.text = ''
            elif instance.text == 'C':
                self.resultado.text = ''
            elif instance.text == '<':
                self.resultado.text = self.resultado.text[:-1]
            else:
                self.resultado.text += instance.text


        for x in ('(', ')', 'C', '<',
            'sin(', 'cos(', 'tan(', 'log10',
            'asin(', 'acos(', 'atan(', '10^',
            'log', '^2', 'sqrt(', 'abs',
            'e^', '^', '^(1/', '1/(',
            'ANS', ')=', 'degrees(', 'radians(', 
            'e', 'E+','E-', 'pi',  
            '7', '8', '9', '+',
            '4', '5', '6', '-', 
            '1', '2', '3', '*',
            '.', '0', '=', '/'):
            #self.nums.append(Button(text=x, font_size=45, color=color[2]))
            self.nums.append(Button(text=x,color=color[2]))
        
            if x.isdigit():
                self.nums[-1].background_color = color[1]

            elif x == 'C' or x == '<':
                self.nums[-1].background_color = color[3]

            else:
                self.nums[-1].color = color[2]
                self.nums[-1].background_color = color[0]

            self.nums[-1].bind(on_press=callback)
            self.pad.add_widget(self.nums[-1])

        self.add_widget(self.pad)

class CalculadoraApp(App):
    def build(self):
        Window.clearcolor = (.1, .1, .1, .1)
        return CalculadoraForm()

if __name__ == '__main__':
    CalculadoraApp().run()


