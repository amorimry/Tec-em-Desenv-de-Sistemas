class Lampada():
    def __init__(self, ligada = False):
        self.ligada = ligada

    def estado(self):
        if self.ligada == True:
            print("A lâmpada está acesa.")
        else:
            print("A lâmpada está apagada.")

    def ligar(self):
        if self.ligada == True:
            print("A lâmpada já está ligada.")
        else:
            self.ligada = True

    def desligar(self):
        if self.ligada == False:
            print("A lâmpada já está desligada.")
        else:
            self.ligada = False


if __name__ == "__main__":

    teste1 = Lampada()

    teste1.desligar()
    teste1.estado()

    teste1.ligar()
    teste1.estado()
