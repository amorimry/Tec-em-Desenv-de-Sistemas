# Crie um sistema escolar onde para calcular a média de um aluno devemos receber 4 notas válidas (entre 0 e 10). Ao final exiba o status de aprovação do aluno.
contador = 0
nota_recebida = 0
while contador < 4:
    nota = float(input(f"Digite a {contador+1}° nota do aluno: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, digite novamente...")
    else:
        contador += 1
        nota_recebida += nota
media = nota_recebida/contador
print(f"Média: {media:.2f}")
if media >= 7 and media <= 10:
    print("Aprovado.")
elif media >= 4 and media < 7:
    print("Recuperação.")
elif media >= 0 and media < 4:
    print("Reprovado.")
else:
    print("Média inválida.")


contador = 0
nota_recebida = 0
while True:
    nota = nota = float(input(f"Digite a {contador+1}° nota do aluno: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, digite novamente...")
        continue
    
    contador += 1
    nota_recebida += nota

    if contador == 4:
        break
media = nota_recebida/contador
print(f"Média: {media:.1f} pontos")
if media >= 7 and media <= 10:
    print("Aprovado.")
elif media >= 4 and media < 7:
    print("Recuperação.")
elif media >= 0 and media < 4:
    print("Reprovado.")
else:
    print("Média inválida.")