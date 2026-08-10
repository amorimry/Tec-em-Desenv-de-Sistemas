numero = -1
soma = 0
maior = None
menor = None
num_neg = 0
num_pos = 0

while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero

    if maior == None:
        maior = numero
    if maior < numero:
        maior = numero

    if menor == None:
        menor = numero
    if menor > numero:
        menor = numero

    if numero < 0:
        num_neg += 1
    else:
        num_pos += 1

print(f"""
soma: {soma}
maior num: {maior}
menor num: {menor}
qtd de num positivos: {num_pos}
qtd de num negativos: {num_neg}
""")

#--------------------------------------

numero = -1
soma = 0
maior = float("-inf")
menor = float("inf")
num_neg = 0
num_pos = 0

while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero

    if maior < numero:
        maior = numero

    if menor > numero:
        menor = numero

    if numero < 0:
        num_neg += 1
    else:
        num_pos += 1

print(f"""
soma: {soma}
maior num: {maior}
menor num: {menor}
qtd de num positivos: {num_pos}
qtd de num negativos: {num_neg}
""")