# DESAFIO 5 — Sistema de entregas

from abc import ABC, abstractmethod

class Entrega(ABC):
    def __init__(self, peso, distancia = 0):
        self.peso = peso
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass

class EntregaLocal(Entrega):
    def calcular_frete(self):
        return self.peso * 2
class EntregaNacional(Entrega):
    def calcular_frete(self):
        return self.peso * self.distancia * 0.05
class RetiradaLoja(Entrega):
    def calcular_frete(self):
        return 0
    
entregas = [
    EntregaLocal(10, 2),
    EntregaNacional(30, 100),
    RetiradaLoja(5, 0)
]
for entrega in entregas:
    frete = entrega.calcular_frete()
    print(f"Frete: R$ {frete:.2f}")