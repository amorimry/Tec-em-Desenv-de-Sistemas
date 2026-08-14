# 3. Crie um programa que pede um número inteiro e verifique se ele é par. Imprima na tela o resultado da verificação:
#Ex: "Par: {True/False}"

num = int(input("Insira um número inteiro: "))
par = num%2 == 0 and num != 0
print (f"Número par: {par}")