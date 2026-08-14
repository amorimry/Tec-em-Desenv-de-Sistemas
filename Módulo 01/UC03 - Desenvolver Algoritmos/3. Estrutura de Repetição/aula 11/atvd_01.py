# usando números de 0 ate 10 nessas questões:

for a in range(11):
    print(a)

print()

for b in range(0, 11, 2):
    print(b)

for c in range(11):
    if c % 2 == 0:
        print(c)

print()

soma1 = 0
for d in range(0, 11, 2):
    soma1 += d
print(f"A soma é: {soma1}")

soma2 = 0
for e in range(11):
    if e % 2 == 0:
        soma2 += e
        # se o número que ta no "e" tiver o resto 0 na divisão por 2, vai pegar a variavel "soma" e incrementar nela os valores que vão chegando no "e"
print(f"soma dos números pares de 0 até 10: {soma2}")

print()

contador1 = 0
for e in range(11):
    if e % 2 == 0:
        contador1 += 1
        # aqui vai olhar os números de 0 até 10, encotrou um número par vai somar 1 na variavel, encontrou outro sobe na variavel 1.. e assim vai
print(f"quantidade de números pares de 0 até 10: {contador1}")

print()

soma3 = 0
contador2 = 0
produto = 0
for f in range(11):
    if f % 2 == 0:
        print(f)
        soma3 += f
        produto *= f #vai da um resultado 0 pois inicia multiplicando com o 0
        contador2 += 1 #contar é subir instâncias, diferente da soma
        

print(f"""Soma: {soma3}
Multiplicação: {produto}
Contador: {contador2}""")