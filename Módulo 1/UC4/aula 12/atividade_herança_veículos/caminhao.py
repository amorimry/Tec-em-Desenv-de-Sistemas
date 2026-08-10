from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, modelo, marca, ano, capacidade):
        super().__init__(modelo, marca, ano)
        self.capacidade = capacidade

    def mostrar_capacidade(self):
        print(f"""
--- Capacidade de carga do caminhão: {self.capacidade} t""")