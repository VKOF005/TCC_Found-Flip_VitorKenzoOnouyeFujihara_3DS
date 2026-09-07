from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior


#classes para suportar atributos de multiplos tipos de elementos

class ImageButton(ButtonBehavior, Image ): #ButtonBehavior tem de ser o primeiro no grupo
    pass

