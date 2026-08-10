# DESAFIO 7 — Sistema de documentos

from abc import ABC, abstractmethod

class Documento(ABC):

    @abstractmethod
    def imprimir(self):
        pass

class Contrato(Documento):
    def imprimir(self):
        print("Imprimindo contrato empresarial.")
class NotaFiscal(Documento):
    def imprimir(self):
        print("Imprimindo nota fiscal empresarial.")
class Recibo(Documento):
    def imprimir(self):
        print("Imprimindo recibo empresarial.")

documentos = [
    Contrato(),
    NotaFiscal(),
    Recibo()
]
for documento in documentos:
    documento.imprimir()
