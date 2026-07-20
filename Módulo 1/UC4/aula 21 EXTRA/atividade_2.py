# Crie uma classe que modele um quadrado:
# ● Atributos: Tamanho do lado
# ● Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self, lado1):
        self.lado1 = lado1

    def mudar_valor(self, novo_lado1):
        self.lado1 = novo_lado1
        print(f"Lado atualizado para {novo_lado1} m.")

    def retornar_valor(self):
        print(f"""
- Valor dos lados

                {self.lado1}       
        . . . . . . . . . .
        .                 .
        .                 .
        .                 .
{self.lado1}       .                 .     {self.lado1}
        .                 .
        .                 .
        . . . . . . . . . .
                {self.lado1}
""")
        
teste1 = Quadrado(5)
teste1.retornar_valor()