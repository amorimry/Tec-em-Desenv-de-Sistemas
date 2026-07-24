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
    def __init__(self, placa, marca, modelo, ano, carga_toneladas, km_rodado):
        super().__init__(placa, marca, modelo, ano)
        self.carga_toneladas = carga_toneladas
        self.km_rodado = km_rodado

    def custo_viagem(self):
        return (self.km_rodado * 35) + (self.carga_toneladas * 470)

class Onibus(Veiculo):
    def __init__(self, placa, marca, modelo, ano, qtd_passageiros):
        super().__init__(placa, marca, modelo, ano)
        self.qtd_passageiros = qtd_passageiros

    def custo_viagem(self):
        return self.qtd_passageiros * 5.40

class Taxi(Veiculo):
    def __init__(self, placa, marca, modelo, ano, bandeira, km_rodado):
        super().__init__(placa, marca, modelo, ano)
        self.bandeira = bandeira
        self.km_rodado = km_rodado

    def custo_viagem(self):
        return self.bandeira + (self.km_rodado * 10)


teste1 = Caminhao("ABC-1234", "Volvo", "FH", 2022, carga_toneladas=4, km_rodado=20)
teste2 = Onibus("XYZ-5678", "Mercedes", "Marcopolo", 2020, qtd_passageiros=45)
teste3 = Taxi("KGB-9999", "Chevrolet", "Spin", 2023, bandeira=25, km_rodado=3)

print(f"R$ {teste1.custo_viagem():.2f}")
print(f"R$ {teste2.custo_viagem():.2f}")
print(f"R$ {teste3.custo_viagem():.2f}")