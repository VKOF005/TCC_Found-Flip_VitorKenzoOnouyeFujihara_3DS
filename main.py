from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *

#o back end, possui classes e funções feitas em python.
#pode ser dividida em mais de um arquivo para melhor organização.

#construtor para criar a tela ao iniciar.

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI
    def on_start(self):
        pass
    #metodo para mudar de tela com base no id da tela.
    def mudar_tela(self, id_tela):
        print(id_tela)
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

MainApp().run()