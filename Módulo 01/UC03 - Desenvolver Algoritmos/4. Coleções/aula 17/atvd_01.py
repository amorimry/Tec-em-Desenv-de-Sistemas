# Crie um programa que recebe uma palavra. Imprima a última letra dessa palavra.

palavra = "Casa"
print(palavra[3])

palavra = input("Digite uma palavra: ")
print(palavra[-1]) #pegar o último elemento de uma coleção, funciona com lista também; em uma lista ou coleção segue aquele mesmo esquema do range, de sempre parar um a menos
print(len(palavra)) #ler toda a palavra, usado pra descobrir o tamanho de algo
print(palavra[len(palavra)-1]) #pega a palavra, vê o tamanho dela e puxa a última que é o tamanho normal dela -1