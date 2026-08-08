class Carro():
    def __init__(self, modelo, velocidade = 0, ligado = False):
        self.modelo = modelo
        self.velocidade = velocidade
        self.ligado = ligado

    def ligar(self):
        self.ligado = True
        print("""
    Carro ligado.         
""")

    def acelerar(self, valor):
        if self.ligado == True:
            self.velocidade += valor
            print(f"""
Aumetando velocidade para {valor:,.2f} km/h
""")
        else:
            print("""
    Carro desligado, ligue primeiro.
""")
            
    def frear(self, valor):
        if self.ligado == True:
            if self.velocidade - valor <= 0:
                print("Velocidade irá ficar negativa.")
            else:
                self.velocidade -= valor
                print(f"""
Diminuindo velocidade em {valor:,.2f} km/h
""")
        else:
            print("""
    Carro desligado, ligue primeiro.
""")

    def mostrar_velocidade(self):
        print(f"--- Velocidade atual do carro: {self.velocidade:,.2f} km/h")


if __name__ == "__main__":
    
    teste1 = Carro("Idea")

    teste1.acelerar(10)
    teste1.ligar()
    teste1.mostrar_velocidade()
    teste1.acelerar(25)
    teste1.mostrar_velocidade()
    teste1.acelerar(30)
    teste1.mostrar_velocidade()
    teste1.frear(100)
    teste1.frear(55)
    teste1.frear(20)
    teste1.mostrar_velocidade()
