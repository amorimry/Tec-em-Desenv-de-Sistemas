# 1. Receba 10 números inteiros. Imprima na tela a soma dos números e quantos eram números pares.

soma_num = 0 #lembrar que começa em 0 só em soma e subtração
num_par = 0
num_impar = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}° número inteiro: "))
    soma_num += num

    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

print(f"A soma dos 10 números digitados é: {soma_num}")
print(f"Desses 10 números, {num_par} são pares e {num_impar} são ímpares")