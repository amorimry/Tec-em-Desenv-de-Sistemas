# 2. Crie um programa que gera bilhetes da mega-sena. O programa deve gerar 6 números inteiros entre 1 e 60 e imprimi-los no formato:
# num1 - num2 - num3 - num4 - num5 - num6

print("== Programa Mega-Sena ==")

linha_sorteio = "" #ótimo para imprimir o histórico das informações; concatenação
import random

for i in range(6):
    num_sorteado = random.randint(1,60)

    if i == 5:
        linha_sorteio += (f"{num_sorteado}")
    else:
        linha_sorteio += (f"{num_sorteado} - ")

print(f"""Números sorteados:
{linha_sorteio}""")