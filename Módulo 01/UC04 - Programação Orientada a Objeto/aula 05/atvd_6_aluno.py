class Aluno():
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        print(f"""
    -- Nota 1: {self.nota1}
    -- Nota 2: {self.nota2}

        A média das notas do aluno foi de: {self.media:.1f} pontos
""")
        
    def verificar_situacao(self):
        if self.media >= 6:
            print("--- Situação: APROVADO")
        else:
            print("--- Situação: REPROVADO")


if __name__ == "__main__":

    teste1 = Aluno("João", 5.8, 9.2)

    teste1.calcular_media()
    teste1.verificar_situacao()