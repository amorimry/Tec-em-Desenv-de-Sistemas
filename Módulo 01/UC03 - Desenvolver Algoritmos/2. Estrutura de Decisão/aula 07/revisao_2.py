# 2. Crie um programa que pede a altura de uma pessoa. Se a altura for maior que 1.40m imprima "Entrada liberada" se não imprima "Entrada Negada".

print ("== Conferir entrada ==")
altura = float(input("Digite sua altura: "))
if altura >= 1.40:
    print ("Entrada liberada.")
else:
    print ("Entrada Negada.")