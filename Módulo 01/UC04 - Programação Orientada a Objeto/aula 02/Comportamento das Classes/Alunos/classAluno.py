class Aluno(): # criando a entidade que representa o Aluno / criando o objeto do tipo Aluno
    def __init__(self, nome, idade, matricula, notas, turma): # o que eu preciso receber para criar o Aluno
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = notas
        self.turma = turma
        