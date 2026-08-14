# 3. Crie um programa que recebe 5 números reais, exiba na tela o maior entre os números inseridos.

num_maior = float("-inf") #menor número é o menos infinito
num_menor = 0
num_digitado = ""
#aqui vai ser feita uma seleção pra escolher
for i in range(5):
    num = float(input(f"Digite o {i+1}° número: "))

    if i == 5:
        num_digitado += (f"{num}")
    else:
        num_digitado += (f"{num} - ")

    if num > num_maior: 
        num_maior = num
    #uma situação não depende da outra
    if num < num_menor:
        num_menor = num

print(f"Números digitados: {num_digitado}")
print(f"O maior número digitado foi {num_maior}")
print(f"O menor número digitado foi {num_menor}")