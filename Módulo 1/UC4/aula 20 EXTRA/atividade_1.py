class Aluno():
    escola = "Senac Centro"
    qtd_alunos = 0

    def __init__(self, nome):
        self.nome = nome

aluno1 = Aluno("Paulo")
Aluno.qtd_alunos += 1
aluno2 = Aluno("Gabs")
Aluno.qtd_alunos += 1

print(aluno1.nome)
print(aluno2.nome)

print(f"Escola: {Aluno.escola}")
print(f"Quantidade de alunos cadastrados: {Aluno.qtd_alunos}")