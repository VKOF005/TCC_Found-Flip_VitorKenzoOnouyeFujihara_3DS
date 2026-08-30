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
    def build(self):
        self.title = 'Found-Flip'
        return GUI
    def on_start(self):

        pass
    #metodo para mudar de tela com base no id da tela.
    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

MainApp().run()