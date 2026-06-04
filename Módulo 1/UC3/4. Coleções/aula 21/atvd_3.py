# Crie um programa que guarda as pontuações do brasileirão. Para guardar essas pontuações use um dicionário onde a chave será o nome do time e o valor será a pontuação do time. Crie pelo menos 5 entradas.

brasileirao = {
}

print("Digite abaixo 5 times e suas 5 pontuações.")
for i in range(5):
    time = input(f"{i+1}° Time: ")
    pontuacao = int(input(f"{i+1}° Pontuação: "))

    brasileirao[time] = pontuacao
    print()

print(brasileirao)



times = ["Flamengo", "Vasco", "Fortaleza", "Botafogo", "Ceará"]
pontos = [48, 52, 28, 23, 36]

brasileirao = {
    "Flamengo": 48,
    "Vasco": 52,
    "Fortaleza": 28,
    "Botafogo": 23,
    "Ceará": 36
}

print(f"Flamengo", brasileirao["Flamengo"])

# for chave in dicionario:
for time in brasileirao: # retorna só informação de chave
    print(time, brasileirao[time]) # complemento para trazer o valor de acordo com a chave

print(brasileirao.items()) # mostra a lista de chaves com valor

print(brasileirao.keys()) # mostra a lista de chaves

print(brasileirao.values()) # mostra a lista de valores; ótimo para verificar 


for time, pontos in brasileirao.items: # te retorna as duas informações, tanto chave quanto valor
    print(time, pontos)