notas = []

for i in range(3):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

print(sum(notas))

media = sum(notas)/len(notas)
print(f"{media:.2f}")

for n in notas:
    print(n)

ordem = 1
for n in notas:
    print(f"{ordem}° nota - {n:.1f}")
    ordem += 1



notas = []
ordem1 = 1
while True:
    nota = float(input(f"Digite a {ordem1}° nota: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        ordem1 += 1
    else:
        print("Nota inválida, digite novamente.")

    if len(notas) >= 3:
        break

print(sum(notas))

media = sum(notas)/len(notas)
print(f"{media:.2f}")

for n in notas:
    print(n)

ordem2 = 1
for n in notas:
    print(f"{ordem}° nota - {n:.1f}")
    ordem2 += 1



notas = []
alunos = []
ordem1 = 1
while True:
    aluno = input(f"Digite o nome do {ordem1}° aluno: ")
    nota = float(input(f"Digite a {ordem1}° nota: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        alunos.append(aluno)
        ordem1 += 1
    else:
        print("Nota inválida, digite novamente.")

    if len(notas) >= 3:
        break

print(notas)
print(alunos)

media = sum(notas)/len(notas)
print(f"{media:.2f}")

for n in notas:
    print(n)

for a in alunos:
    print(a)

ordem2 = 0
for n in notas:
    print(f"{alunos[ordem2]} - {n:.1f}")
    ordem2 += 1



for aluno, nota in zip(alunos, notas):
    print(aluno, nota)