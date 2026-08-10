class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self):
        print(f"Cor atual: {self.cor}")
        nova_cor = input("Digite a nova cor: ")
        self.cor = nova_cor
        print("Cor atualizada!")

    def mostrar_cor(self):
        return f"Cor atual da bola: {self.cor}"
    
bola1 = Bola("Azul", 10, "Couro")