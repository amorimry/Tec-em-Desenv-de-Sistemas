class Termometro():
    def __init__(self, temperatura = 0):
        self.temperatura = temperatura

    def mostrar_temp(self):
        print(f"""
        Temperatura atual: {self.temperatura:.2f}°C
""")

    def aumentar(self, valor):
        self.temperatura += valor
        print(f"""
--- Temperatura aumentada em {valor:.2f}°C
""")
        
    def diminuir(self, valor):
        self.temperatura -= valor
        print(f"""
--- Temperatura diminuida em {valor:.2f}°C
""")
        
    def verificar_temp(self):
        if self.temperatura < 15:
            print("-- Frio 🥶 --")
        elif self.temperatura >= 15 and self.temperatura <= 30:
            print("-- Agradável 🤗 --")
        else:
            print("-- Quente 🥵 --")

if __name__ == "__main__":

    teste1 = Termometro()
    teste2 = Termometro(20)

    teste1.mostrar_temp()
    teste1.verificar_temp()
    teste1.aumentar(31)
    teste1.aumentar(5)
    teste1.mostrar_temp()
    teste1.verificar_temp()
    print("-------------------------------------------------")
    teste2.mostrar_temp()
    teste2.verificar_temp()
    teste2.diminuir(10)
    teste2.mostrar_temp()
    teste2.verificar_temp()