# 6. Controle de presença
# Uma turma tem 6 alunos. Use um for com enumerate() para percorrer a lista de nomes e perguntar ao usuário "presente" ou "ausente" para cada um. Ao final, exiba quantos alunos estiveram presentes e quantos faltaram.

alunos = ["PAULO", "PEDRO", "HENRIQUE", "GABRIELA", "LUIZA", "LIZ"]
presente = 0
ausente = 0
print("-- Sistema de Presença --")
print("P: Presente  |  A: Ausente")
print()
for i in alunos:
    while True:
        presenca = input(f"Aluno {i}\nSituação: ")
        if presenca == "P":
            presente += 1
            print()
            break
        elif presenca == "A":
            ausente += 1
            print()
            break
        else:
            print("Situação inválida, digite novamente.")
print(f"""
Alunos presentes: {presente}
Alunos ausentes: {ausente}
""")



turma = []

while True:
    aluno = input(f"Digite o nome do aluno Nº{len(turma)+1} (Vazio para finalizar): ")

    if aluno == "":
        break

    turma.append(aluno)

    # resp = input("Quer continuar? (S/N): ")
    # if resp.upper() == "N":
    #     break

ausente = 0
presente = 0
for a in turma:
    print(f"Frequência do aluno {a}.")
    frequencia = input("Digite o estado do aluno (P = Presente /A = Ausente): ")
    
    if frequencia == "P":
        presente += 1

    if frequencia == "N":
        ausente += 1


print(f"""
Presentes: {presente}
Ausentes: {ausente}
""")


#colocar a parte 2

# ausentes = 0
# presentes = 0
# for a in turma:
#     while True:
#         print(f"Frequência do aluno {a}.")
#         frequencia = input("Digite o estado do aluno (P = Presente /A = Ausente): ")
        
#         if frequencia == "P":
#             presente += 1
#             break
#         elif frequencia == "N":
#             ausente += 1
#             break
#         else:
#             print("Presença incorreta, digite novamente.")