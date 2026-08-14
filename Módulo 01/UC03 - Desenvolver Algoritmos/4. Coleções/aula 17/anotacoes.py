# CRUDE : operações feitas com qualquer estrutura de dados
# Creat - Inserir
# Read - Ler/Assistir
# Update - Alterar
# Delete - Remover

nome  = "banana"

nome = nome.lower() #pegar a primeira letra, transformar ela em minúscula e depois verificar

print(nome[0]) #0 é a primeira posição

print(nome.count("a")) #contar quantas letras "a" tem na palavra

nome = nome.replace("an", "em")
print(nome)



frutas = ["maça", "pêra", "uva", "banana", "abacaxi"] #tipo list; declarando infos na lista
#lista é ordenada, mutável

print(len(frutas)) #ler quantas coisas tem na lista

print(frutas[-1]) #última coisa a lista
print(frutas[4])

print(frutas[3]) #"banana"
print(frutas[-2]) #"banana"