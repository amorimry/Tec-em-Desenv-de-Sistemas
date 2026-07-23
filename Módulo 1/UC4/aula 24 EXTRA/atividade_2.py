from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, marca, modelo, ano):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def custo_viagem(self):
        return 20
        # taxa base para qualquer veículo rodar

class Caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, carga_toneladas):
        super().__init__(placa, marca, modelo, ano)
        self.carga_toneladas = carga_toneladas

    def custo_viagem(self):
        taxa_base = super().custo_viagem()
        return taxa_base + (self.carga_toneladas * 10) # R$ 10,00 por tonelada de carga

class Onibus(Veiculo):
    def __init__(self, placa, marca, modelo, ano, qtd_passageiros):
        super().__init__(placa, marca, modelo, ano)
        self.qtd_passageiros = qtd_passageiros

    def custo_viagem(self):
        taxa_base = super().custo_viagem()
        return taxa_base + (self.qtd_passageiros * 4.50) # R$ 4,50 por passageiro

class Taxi(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodado):
        super().__init__(placa, marca, modelo, ano)
        self.km_rodado = km_rodado

    def custo_viagem(self):
        taxa_base = super().custo_viagem()
        return taxa_base + (self.km_rodado * 15) # R$ 15,00 por km rodado


teste1 = Caminhao("ABC-1234", "Volvo", "FH", 2022, carga_toneladas=20)
teste2 = Onibus("XYZ-5678", "Mercedes", "Marcopolo", 2020, qtd_passageiros=45)
teste3 = Taxi("KGB-9999", "Chevrolet", "Spin", 2023, km_rodado=3)

print(f"R$ {teste1.custo_viagem():.2f}")
print(f"R$ {teste2.custo_viagem():.2f}")
print(f"R$ {teste3.custo_viagem():.2f}")