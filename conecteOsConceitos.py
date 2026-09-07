class ConecteOsConceitos:

    counter = 1

    def decrease_counter(self):
        if self.counter > 1:
            self.counter -= 1
        self.atualizar_nEtapa()

    def increasse_counter(self):
        if self.counter < 5:
            self.counter += 1
        self.atualizar_nEtapa()

    def atualizar_nEtapa(self):
        if self.counter > 0:
            self.root.ids.etapa1.source =f"imgs/barra1.png"
            self.root.ids.etapa2.source = f"imgs/barra2.png"
            self.root.ids.etapa3.source = f"imgs/barra2.png"
            self.root.ids.etapa4.source = f"imgs/barra2.png"
        else:
            if self.counter > 1:
                self.root.ids.etapa1.source = f"imgs/barra1.png"
                self.root.ids.etapa2.source = f"imgs/barra1.png"
                self.root.ids.etapa3.source = f"imgs/barra2.png"
                self.root.ids.etapa4.source = f"imgs/barra2.png"
            else:
                if self.counter >2:
                    self.root.ids.etapa1.source = f"imgs/barra1.png"
                    self.root.ids.etapa2.source = f"imgs/barra1.png"
                    self.root.ids.etapa3.source = f"imgs/barra1.png"
                    self.root.ids.etapa4.source = f"imgs/barra2.png"
                else:
                    self.root.ids.etapa1.source = f"imgs/barra1.png"
                    self.root.ids.etapa2.source = f"imgs/barra1.png"
                    self.root.ids.etapa3.source = f"imgs/barra1.png"
                    self.root.ids.etapa4.source = f"imgs/barra1.png"
