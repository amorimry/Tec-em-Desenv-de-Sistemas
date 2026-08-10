# DESAFIO 3 — Sistema de relatórios

from abc import ABC, abstractmethod

class Relatorio(ABC):

    @abstractmethod
    def gerar(self, dados):
        pass

class RelatorioPDF(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório em PDF: {dados}")
class RelatorioExcel(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório em Excel: {dados}")
class RelatorioHTML(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório em HTML: {dados}")

relatorios = [
    RelatorioPDF(),
    RelatorioExcel(),
    RelatorioHTML()
]
for relatorio in relatorios:
    relatorio.gerar("Vendas do mês")