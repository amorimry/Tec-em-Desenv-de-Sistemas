# DESAFIO 8 — Sistema de contas bancárias

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def calcular_tarifa(self):
        pass

class ContaCorrente(Conta):
    def calcular_tarifa(self):
        return 25
class ContaPoupanca(Conta):
    def calcular_tarifa(self):
        return 0
class ContaEmpresarial(Conta):
    def calcular_tarifa(self):
        return 100

contas = [
    ContaCorrente("Ana", 1000),
    ContaPoupanca("Carlos", 800),
    ContaEmpresarial("Empresa XYZ", 5000)
]

for conta in contas:
    tarifa = conta.calcular_tarifa()
    print(f"Titular: {conta.titular} - Tarifa: R$ {tarifa:.2f}")
