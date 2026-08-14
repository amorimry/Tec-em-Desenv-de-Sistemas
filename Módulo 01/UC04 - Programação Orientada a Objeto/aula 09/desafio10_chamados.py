# DESAFIO 10 — Sistema de chamados administrativos

from abc import ABC, abstractmethod

class Chamado(ABC):

    @abstractmethod
    def calcular_prazo(self):
        pass

class BaixaPrioridade(Chamado):
    def calcular_prazo(self):
        return 90
class MediaPrioridade(Chamado):
    def calcular_prazo(self):
        return 60
class AltaPrioridade(Chamado):
    def calcular_prazo(self):
        return 10

chamados = [
    BaixaPrioridade(),
    MediaPrioridade(),
    AltaPrioridade()
]
for chamado in chamados:
    prazo = chamado.calcular_prazo()
    print(f"Prazo de atendimento: {prazo} minutos")
