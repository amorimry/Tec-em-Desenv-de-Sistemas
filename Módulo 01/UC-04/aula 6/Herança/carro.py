from veiculo import Veiculo

class Carro(Veiculo): # indica que a class Carro (class filha) herda todas as coisas da class Veiculo
    def __init__(self, modelo, marca, ano, qtd_portas): # cria o construtor da classe filha
        super().__init__(modelo, marca, ano) # chama o construtor da classe mãe
        self.qtd_portas = qtd_portas # cria um atributo específico da classe Carro

    def mostrar_qtd_portas(self):
        print(f"""
--- Quantidade de portas do modelo do carro: {self.qtd_portas}
""")