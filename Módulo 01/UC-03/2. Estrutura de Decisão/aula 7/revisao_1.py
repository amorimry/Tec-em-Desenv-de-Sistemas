# 1. Crie um programa que pede um número inteiro. Imprima na tela uma mensagem informando se o número é Par ou Impar.

print ("== Programa de Números ==")
numero = int(input("Digite um número inteiro: "))
if numero%2 == 0:
    print ("Número par.")
else:
    print ("Número ímpar.")