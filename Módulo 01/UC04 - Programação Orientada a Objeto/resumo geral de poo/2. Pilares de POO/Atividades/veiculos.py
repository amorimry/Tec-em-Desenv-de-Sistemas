class Veiculo():
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def mover(self):
        print("Veiculo se movendo!")

class Carro(Veiculo):
    def __init__(self, modelo, marca):
        super().__init__(modelo, marca)

    def mover(self):
        print("Dirija!")

class Barco(Veiculo):
    def __init__(self, modelo, marca):
        super().__init__(modelo, marca)

    def mover(self):
        print("Nade!")

class Aviao(Veiculo):
    def __init__(self, modelo, marca):
        super().__init__(modelo, marca)

    def mover(self):
        print("Voe!")

car1 = Carro("Ford", "Mustang")
boat1 = Barco("Ibiza", "Touring 20")
plane1 = Aviao("Boeing", "747")

for veiculo in (car1, boat1, plane1):
  print(veiculo.marca)
  print(veiculo.modelo)
  veiculo.mover()