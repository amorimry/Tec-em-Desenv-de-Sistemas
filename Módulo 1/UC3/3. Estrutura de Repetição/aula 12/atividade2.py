# 2. Faça um programa que repete 4 vezes a seguinte operação: Pede uma nota de um aluno e acrescenta a nova nota à soma das notas. Ao final das repetições exiba a média do aluno e se ele foi aprovado, reprovado ou está de recuperação.(Defina as notas para cada condição)
# Bônus: Considere apenas notas entre 0 e 10.
# Bônus: Permita que o professor decida quantas notas serão registradas.
# Bônus: Exiba o boletim do aluno ao final

nota = 0
divisao = 0
boletim = ""

#permitir quantas notas vão ser calculadas
qdt_notas = int(input("Digite quantas notas quer calcular: "))

for i in range(qdt_notas):
    valor_nota = float(input(f"Digite a {i+1}° nota do aluno: "))

    if valor_nota >= 0 and valor_nota <= 10:
        nota += valor_nota #os valores que serão anotados na variavel _qdt_notas vai ser acrescentado na variavel _notas_
        divisao += 1 #para que a divisão da média seja só com as notas válidas, insere isso para ser somado 1 na variavel _divisao_

        boletim += (f"AV{divisao} = {valor_nota}\n") #já calcula aqui no if a tabulação do boletim, para justamente lá no final só puxar a variavel; _divisao_ seria a quantidade de notas, ou seja, a qdt de avaliações, então da pra puxar daq; lembrar de usar o \n no final para as notas que forem sendo inseridas quebrarem de linha
    else:
        print("Nota inválida, não será contada.")

media = nota/divisao

#saber a situação do aluno de acordo com sua média
print(f"A média do aluno foi de: {media:.1f} pontos")
if media >= 6 and media <= 10:
    print("Aluno aprovado!")
elif media >= 4 and media < 6:
    print("Aluno de recuperação!")
elif media >= 0 and media < 4:
    print("Alundo reprovado!")
else:
    print("Média inválida, tente novamente.")

#imprimir o boletim
print("== Boletim de notas ==")
print(f"{boletim}")