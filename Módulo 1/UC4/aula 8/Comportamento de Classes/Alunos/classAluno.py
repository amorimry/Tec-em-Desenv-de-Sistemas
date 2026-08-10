class Aluno():
    def __init__(self, nome, idade, notas, turma):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        self.turma = turma

    def mostrar_informacoes(self): # é necessário botar o parâmetro para ter acesso aos dados do aluno
        print(f"""
    -- Ficha do Aluno --
Nome: {self.nome}
Idade: {self.idade}
Notas: {self.notas}
Turma: {self.turma}

Média: {self.calcular_media():.1f}

Situação: {self.exibir_situacao()}
""")
        
    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media

    def exibir_situacao(self):
        if self.calcular_media() >= 7 and self.calcular_media() <= 10:
            situacao = "Aprovado"
        elif self.calcular_media() >= 4 and self.calcular_media() < 7:
            situacao = "Recuperação"
        elif self.calcular_media() >= 0 and self.calcular_media() < 4:
            situacao = "Reprovado"
        
        return situacao

#     def calcular_media(self):
#         media = sum(self.notas) / len(self.notas)
#         print(f"Média do aluno: {media:.1f}")
    
#     def mostrar_informacoes(self):
#         print(f"""
#     -- Ficha do Aluno --
# Nome: {self.nome}
# Idade: {self.idade}
# Notas: {self.notas}
# Turma: {self.turma}
# """)