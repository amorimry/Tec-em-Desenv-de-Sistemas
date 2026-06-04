from classAluno import Aluno

aluno1 = Aluno("Gabriel", 16, 5, [8.9, 6.2, 7], "A")

aluno2 = Aluno("Liz", 17, 10, [6, 10, 7.8], "B")

aluno3 = Aluno("José", 16, 33, [5.5, 3, 10], "C")

# def ver_aluno(aluno):
#     print(f"""
#         ---- Ficha dos alunos ----
#     1° Aluno: {aluno.nome}
# Idade: {aluno.idade}
# Matricula: {aluno.matricula}
# Nota 1: {aluno.notas[0]} | Nota 2: {aluno.notas[1]} | Nota 3: {aluno.notas[2]}
# Média: {sum(aluno.notas) / len(aluno.notas)}
# Turma: {aluno.turma}""")

print(f"""
        ---- Ficha dos alunos ----
    1° Aluno: {aluno1.nome}
Idade: {aluno1.idade}
Matricula: {aluno1.matricula}
Nota 1: {aluno1.notas[0]} | Nota 2: {aluno1.notas[1]} | Nota 3: {aluno1.notas[2]}
Média: {sum(aluno1.notas) / len(aluno1.notas)}
Turma: {aluno1.turma}

2° Aluno: {aluno2.nome}
Idade: {aluno2.idade}
Matricula: {aluno2.matricula}
Nota 1: {aluno2.notas[0]} | Nota 2: {aluno2.notas[1]} | Nota 3: {aluno2.notas[2]}
Média: {sum(aluno2.notas) / len(aluno2.notas)}
Turma: {aluno2.turma}

3° Aluno: {aluno3.nome}
Idade: {aluno3.idade}
Matricula: {aluno3.matricula}
Nota 1: {aluno3.notas[0]} | Nota 2: {aluno3.notas[1]} | Nota 3: {aluno3.notas[2]}
Média: {sum(aluno3.notas) / len(aluno3.notas)}
Turma: {aluno3.turma}
""")

