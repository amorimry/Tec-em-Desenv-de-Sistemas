# 1. Crie um programa que imprime na tela os números de 0 a 100

num = 0
while num <= 100:
    print(num)
    num += 1


#números pares até 100
num = 0
while num <= 100:
    if num % 2 == 0:
        print(num)
    num += 1


#100 primeiros números pares
num = 0
num_atual = 0
while num <= 100:
    if num_atual % 2 == 0:
        print(num_atual)
        num += 1
    num_atual += 1