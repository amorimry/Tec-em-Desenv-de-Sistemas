# Crie uma classe que modele um retangulo:
# ● Atributos: LadoA, LadoB
# ● Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# ● Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valor(self, novoA, novoB):
        self.ladoA = novoA
        self.ladoB = novoB

        print(f"""Lados do retângulo atualizados com sucesso.
    ALtura: {self.ladoA}
    Largura: {self.ladoB}""")

    def retornar_lados(self):
        print(f"""
-- Valor atual dos lados do retângulo

            {self.ladoB}
. . . . . . . . . . . . . . . .
.                             .
.                             .     {self.ladoA}
.                             .
.                             .
. . . . . . . . . . . . . . . .
""")
        
    def calcular_area(self):
        area = self.ladoB * self.ladoA
        print(f"Área do retângulo: {area}")

    def calcular_perimetro(self):
        perimetro = (self.ladoB * 2) + (self.ladoA * 2)
        print(f"Perímetro do retângulo: {perimetro}")

teste1 = Retangulo(5, 20)
teste1.retornar_lados()
teste1.calcular_area()
teste1.calcular_perimetro()