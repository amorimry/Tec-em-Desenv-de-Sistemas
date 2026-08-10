class Veiculo(): # class mãe
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def apresentar_veiculo(self):
        print(f"""
--- Informações do veículo

        Modelo: {self.modelo}
        Marca: {self.marca}
        Ano: {self.ano}
""")