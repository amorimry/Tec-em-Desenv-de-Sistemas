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
        
class Carro(Veiculo): # indica que a class Carro (class filha) herda todas as coisas da class Veiculo
    def __init__(self, modelo, marca, ano, qtd_portas): # cria o construtor da classe filha
        super().__init__(modelo, marca, ano) # chama o construtor da classe mãe
        self.qtd_portas = qtd_portas # cria um atributo específico da classe Carro

    def mostrar_qtd_portas(self):
        print(f"""
--- Quantidade de portas do modelo do carro: {self.qtd_portas}
""")

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cilindradas):
        super().__init__(modelo, marca, ano)
        self.cilindradas = cilindradas

    def mostrar_cilindradas(self):
        print(f"""
--- Quantidade de cilindradas do modelo da moto indicado: {self.cilindradas}
""")
        
class Caminhao(Veiculo):
    def __init__(self, modelo, marca, ano, capacidade):
        super().__init__(modelo, marca, ano)
        self.capacidade = capacidade

    def mostrar_capacidade(self):
        print(f"""
--- Capacidade de carga do caminhão: {self.capacidade} t""")

# A herança é usada quando exite algum tipo de relação entre os termos.
# A classe mãe possui atributos e métodos gerais.
# Use herança quando a classe filha realmente for um tipo da classe mãe.

# O super() é usado para chamar métodos da classe mãe.
# Ele é muito comum quando a classe filha precisa reaproveitar o __init__ da classe mãe e adicionar novos atributos.
# Usamos super() para evitar repetir a criação dos atributos que já existem na classe mãe.