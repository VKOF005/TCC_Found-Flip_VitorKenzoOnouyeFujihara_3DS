from kivy.app import App
from kivy.lang import Builder

    #import de classes separadas para melhor visualização de partes do codigo

from telas import *
from elementosExtras import *


from kivy.config import Config



#construtor para criar a tela ao iniciar.

#tamanho fixo da tela?


Config.set('graphics', 'resizable', '0')

Config.set('graphics', 'height', '917')

Config.set('graphics', 'width', '412')





#criação da tela + methodos basicos

GUI = Builder.load_file("main.kv")
class MainApp(App):

    counter = 2

    #"initialize" para o valor ser usado

    def build(self):
        self.title = 'Found-Flip'
        return GUI
    
    def decrease_counter(self):

        current_screen = self.root.ids["screen_manager"].current_screen #current_screen faz parte da biblioteca kivy.
        if hasattr(current_screen, 'decrease_counter'):
            current_screen.decrease_counter()
        print(f"Counter on screen: {getattr(current_screen, 'counter', 'N/A')}") # excceção caso não possua um valor.


    def on_start(self):

        pass

    #metodo para mudar de tela com base no id da tela.
    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela
        pass





MainApp().run()