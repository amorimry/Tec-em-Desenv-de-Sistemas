# Bônus: Evite que um mesmo número seja impresso múltiplas vezes

print("== Programa Mega-Sena ==")

linha_sorteio = ""
import random

for i in range(6):
    num_sorteado = random.randint(1,60)
    print(f"O computador gerou:", num_sorteado)

    if num_sorteado < 10:
        num = (f"0{num_sorteado}") #aqui é pra os números ficarem 01, 02, 03...

    if num_sorteado in linha_sorteio: #se o numero que eu gerei estiver na linha do sorteio, não vamos contabilizar, gera novamente
        print("Número duplicado.")
        num_sorteado = random.randint(1,60) #um novo número vai ser gerado
        if num_sorteado < 10:
            num = (f"0{num_sorteado}")
        print(f"O computador gerou:", num_sorteado)

        if num_sorteado in linha_sorteio:
            print("Número duplicado.")
            num_sorteado = random.randint(1,60) #um novo número vai ser gerado se caso o que já tiver sido gerado novo já tiver
            if num_sorteado < 10:
                num = (f"0{num_sorteado}")
            print(f"O computador gerou:", num_sorteado)

    if i == 5:
        linha_sorteio += (f"{num_sorteado}")
    else:
        linha_sorteio += (f"{num_sorteado} - ")

print()

print(f"""Números sorteados:
{linha_sorteio}""")