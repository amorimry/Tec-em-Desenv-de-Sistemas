#Crie um programa que recebe três números inteiros e imprima eles em ordem crescente.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

ordem_crescente = ""

# 1, 2, 3
# 1, 3, 2
# 2, 1, 3
# 2, 3, 1
# 3, 1, 2
# 3, 2, 1

if numero1 <= numero2 and numero1 <= numero3:
    if numero2 >= numero1 and numero2 <= numero3:
        ordem_crescente = (f"{numero1, numero2, numero3}")
    else:
        ordem_crescente = (f"{numero1, numero3, numero2}")
elif numero2 <= numero1 and numero2 <= numero3:
    if numero1 >= numero2 and numero1 <= numero3:
        ordem_crescente = (f"{numero2, numero1, numero3}")
    else:
        ordem_crescente = (f"{numero2, numero3, numero1}")
elif numero3 <= numero2 and numero3 <= numero3:
    if numero1 >= numero3 and numero1 <= numero2:
        ordem_crescente = (f"{numero3, numero1, numero2}")
    else:
        ordem_crescente = (f"{numero3, numero2, numero1}")
else:
    ordem_crescente = (f"ERRO")

print (f"{ordem_crescente}")