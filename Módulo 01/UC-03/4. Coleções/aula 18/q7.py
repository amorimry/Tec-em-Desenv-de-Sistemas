# 7. Placar de campeonato
# Duas listas paralelas armazenam os times e seus pontos:
# times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
# pontos = [58, 65, 42, 51]
# Use for com enumerate() para exibir a tabela de classificação. Depois encontre e exiba o time com mais pontos (localizando o índice do valor máximo com .index(max(...))).

times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
pontos = [58, 65, 42, 51]

# for time, ponto in zip(times, pontos): #o zip junta as duas listas; modelo python
#     print(time, ponto)

maior_time = ""
maior_pont = 0

# print(times[0], pontos[0])
# print(times[1], pontos[1])
for i in range(len(times)): #modelo mais geral
    print(times[i], pontos[i])

    if pontos[i] > maior_pont: #o cochete fica aq justamente para poder acessar o local la na lista lá de cima
        maior_pont = pontos[i]
        maior_time = times[i]

print(f"Time com maior pontuação: {maior_time} - {maior_pont}")


# print(f"Time com mais pontos: {times[pontos.index(max(pontos))]} - {max(pontos)}")