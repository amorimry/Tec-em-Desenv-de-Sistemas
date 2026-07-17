class Aluno():
    escola = "Senac Centro"
    qtd_alunos = 0

    def __init__(self, nome):
        self.nome = nome
        self.qtd_alunos += 1

aluno1 = Aluno("Paulo")
aluno2 = Aluno("Gabs")

print(aluno1.nome)
print(aluno2.nome)

print(Aluno.escola)
print(Aluno.qtd_alunos)