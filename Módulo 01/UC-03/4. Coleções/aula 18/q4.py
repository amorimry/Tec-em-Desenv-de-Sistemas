# 4. Fatiamento de ranking
# Uma competição registrou os tempos (em segundos) dos 8 participantes em ordem de chegada: [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4]. Usando slicing, exiba apenas o pódio (os 3 primeiros), os 3 últimos colocados e os participantes do meio (posições 3 a 5).

tempos = [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4]

print(tempos[0:3:1])
print(tempos[5:8])
# print(tempos[len(tempos)-3:len(tempos)])
print(tempos[3:5])