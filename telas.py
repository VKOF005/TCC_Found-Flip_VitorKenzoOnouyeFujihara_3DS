from kivy.uix.screenmanager import Screen
from conecteOsConceitos import ConecteOsConceitos

class QuizTela(Screen):
    pass

class XXX(Screen):
    pass

class ConecteOsConceitosTela(Screen):
    game = ConecteOsConceitos()
    
    def decrease_counter(self):
        self.game.root = self
        self.game.decrease_counter()
    
    def increase_counter(self):
        self.game.root = self
        self.game.increasse_counter()
