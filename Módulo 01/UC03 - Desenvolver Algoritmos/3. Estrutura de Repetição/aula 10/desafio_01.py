#Crie um programa que recebe três números inteiros e imprima o maior deles.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"O maior número é: {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O maior número é: {numero2}")
elif numero3 >= numero1 and numero3 >= numero2:
    print(f"O maior número é: {numero3}")