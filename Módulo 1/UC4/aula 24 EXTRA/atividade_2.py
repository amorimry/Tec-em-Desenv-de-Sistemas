from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, marca, modelo, ano):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def custo_viagem(self):
        pass

class Caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, carga_toneladas):
        super().__init__(placa, marca, modelo, ano)
        self.custo_basico = 470
        self.carga_toneladas = carga_toneladas

    def custo_viagem(self):
        return self.carga_toneladas * self.custo_basico

class Onibus(Veiculo):
    def __init__(self, placa, marca, modelo, ano, qtd_passageiros):
        super().__init__(placa, marca, modelo, ano)
        self.custo_basico = 5.40
        self.qtd_passageiros = qtd_passageiros

    def custo_viagem(self):
        return self.qtd_passageiros * self.custo_basico

class Taxi(Veiculo):
    def __init__(self, placa, marca, modelo, ano, bandeira, km_rodado):
        super().__init__(placa, marca, modelo, ano)
        self.custo_basico = 10
        self.bandeira = bandeira
        self.km_rodado = km_rodado

    def custo_viagem(self):
        return self.bandeira + (self.km_rodado * self.custo_basico)


teste1 = Caminhao("ABC-1234", "Volvo", "FH", 2022, carga_toneladas=4)
teste2 = Onibus("XYZ-5678", "Mercedes", "Marcopolo", 2020, qtd_passageiros=45)
teste3 = Taxi("KGB-9999", "Chevrolet", "Spin", 2023, bandeira=25, km_rodado=3)

print(f"R$ {teste1.custo_viagem():.2f}")
print(f"R$ {teste2.custo_viagem():.2f}")
print(f"R$ {teste3.custo_viagem():.2f}")