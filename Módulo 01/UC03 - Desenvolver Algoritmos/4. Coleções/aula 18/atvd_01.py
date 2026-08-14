nomes = []
# medias = []

for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    # media = float(input("Digite a média do aluno: "))
    nomes.append(nome)

nomes.sort() #do menor para o maior
# nomes.reverse() #do maior para o menor
#altera toda a ordem das listas

print(nomes)

#percorrendo a lista para fazer algo
for n in nomes:
    print(n)
    print(f"1. {n}")

#de acordo com o tamanho da lista
for j in range(len(nomes)):
    print(f"{j}. {nomes[j]}") #últil em lista paralela