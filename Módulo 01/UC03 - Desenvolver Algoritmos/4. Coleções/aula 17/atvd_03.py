# Crie um programa que recebe uma palavra. Imprima todos os caracteres dessa palavra, linha por linha.
palavra = "Jujuba"

for i in range(len(palavra)): #vai ler o tanto de letras e ir a quantidade de letras
    print(palavra[i])

# palavra = "Jujuba"
# texto = ""

# for i in range(len(palavra)):
#     texto += palavra[i]


# Conte quantas vogais tem na palavra do programa acima
palavra = "Jujuba"
qtd_vogais = 0

for i in range(len(palavra)): 
    print(palavra[i])

    if palavra[i] in "aeiou":
        qtd_vogais += 1

print(qtd_vogais)


# Maneira python
texto = "Abacaxi"
qtd_vogais = 0

for letra in texto: #pega o elemento por vez da coleção
    if letra in "aeiou":
        print(letra) #vai imprimir so a letra da vez que for vogal
        qtd_vogais += 1

print(qtd_vogais)