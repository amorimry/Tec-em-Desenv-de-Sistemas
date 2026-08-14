soma = 0
contador = 0

for i in range(1,11):
    if i  % 2 == 0:
        print(i)
        soma += i #pode usar todos os símbolos matemáticos
        contador += 1
print(f"""
A soma desses números é: {soma}
A quantidade de números que tem é: {contador}""")