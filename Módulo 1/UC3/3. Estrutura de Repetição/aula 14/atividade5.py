# 2. Crie um programa que pede números inteiros até que seja digitado -1. Quando o usuário digitar -1,encerre e exiba a soma de todos os números

num = 1
soma = 0
while num != -1:
    num = int(input("Digite um número inteiro (-1 para sair): "))
    soma += num

print(f"A soma dos números é: {soma+1}")



soma = 0
while True:
    num = int(input("Digite um número inteiro (-1 para sair): "))

    if num == -1:
        break #comando de saída é logo dps de pedir algo

    soma += num

print(f"A soma dos números é: {soma}")