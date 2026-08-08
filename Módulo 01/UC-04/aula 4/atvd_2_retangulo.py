class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        print(f"A área do retângulo é de {area:.2f} m.")

    def calcular_perimetro(self):
        perimetro = (2 * self.largura) + (2 * self.altura)
        print(f"O perímetro do retângulo é de {perimetro:.2f} m.")

    # def desenhar_figura(self):
    #     linha = "+" * self.largura
    #     print(linha)
    #     for i in range(self.altura-2)
    #         print(f"")


if __name__ == "__main__":

    teste1 = Retangulo(56.3, 28.5)
    teste2 = Retangulo(5, 8)

    teste1.calcular_area()
    teste1.calcular_perimetro()

    teste2.calcular_area()
    teste2.calcular_perimetro()