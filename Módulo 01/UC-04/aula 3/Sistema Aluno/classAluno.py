class Aluno(): 
    def __init__(self, nome, idade, matricula, notas, turma):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = notas
        self.turma = turma

    def mostrar_informacoes(self):
        print(f"""
INFORMAÇÕES DO ALUNO
    
    Nome: {self.nome}
    Idade: {self.idade} anos
    Matrícula: {self.matricula}
    Turma: {self.turma}

    Notas: {self.notas}
""")
        print(f"""
SITUAÇÃO DO ALUNO
    
    Média das notas: {self.calcular_media():.1f}
    {self.calcular_situacao()}
""")
        
    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        return media
    
    def calcular_situacao(self):
        media = self.calcular_media()
        if media >= 7 and media <= 10:
            return "Aprovado!"
        elif media >= 4 and media < 7:
            return "Recuperação."
        elif media >= 0 and media < 4:
            return "Recuperação."
        else:
            return "Média inválida."