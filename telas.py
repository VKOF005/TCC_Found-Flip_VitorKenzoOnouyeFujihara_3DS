from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.app import App

#methodos das classes de cada tela

class QuizTela(Screen):
    pass

class XXX(Screen):
    pass

class ConecteOsConceitosTela(Screen):
    counter = 2
    bar1_image = StringProperty("imgs/barra1.png")
    bar2_image = StringProperty("imgs/barra1.png")
    bar3_image = StringProperty("imgs/barra2.png")
    bar4_image = StringProperty("imgs/barra2.png")
    
    def on_enter(self): #builder rodando quando a tela é aberta.

        self.update_bars()

    def update_bars(self):

        # State lookup table: maps counter value to bar images
        bar_states = { # mapa de valores, funciona como um conjunto de arrays com seus respectivos valores e condições.
                       # sendo counter = 2 o conjunto de valores source respectivamente para o kivy.
            4: ("imgs/barra1.png", "imgs/barra1.png", "imgs/barra1.png", "imgs/barra1.png"),
            3: ("imgs/barra1.png", "imgs/barra1.png", "imgs/barra1.png", "imgs/barra2.png"),
            2: ("imgs/barra1.png", "imgs/barra1.png", "imgs/barra2.png", "imgs/barra2.png"),
            1: ("imgs/barra1.png", "imgs/barra2.png", "imgs/barra2.png", "imgs/barra2.png"),
            0: ("imgs/barra2.png", "imgs/barra2.png", "imgs/barra2.png", "imgs/barra2.png"),
        }
        bars = bar_states.get(self.counter, ("imgs/barra2.png", "imgs/barra2.png", "imgs/barra2.png", "imgs/barra2.png"))
        # parâmetros para caso de valores diferentes dos definidos (4 < counter ou counter < 0)
        
        self.bar1_image = bars[0]
        self.bar2_image = bars[1]
        self.bar3_image = bars[2]
        self.bar4_image = bars[3]

    def decrease_counter(self):
        if self.counter > 0:
            self.counter -= 1
        else:
            App.get_running_app().mudar_tela("XXX")
        self.update_bars()

