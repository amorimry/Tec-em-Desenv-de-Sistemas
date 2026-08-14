print("--- LISTA DE NÚMEROS ---")

numeros = [10, 55, 8, 1, 43, 100, 23]
soma = 0
maior_numero = float("-inf")
for num in numeros:
    soma += num

    if num > maior_numero:
        maior_numero = num

print (soma)


numeros = [10, 55, 8, 1, 43, 100, 23]
soma = sum(numeros)
maior_numero = max(numeros)
menor_numero = min(numeros)
media = sum(numeros)/len(numeros)
print(f"""
{soma}
{maior_numero}
{menor_numero}
{media}
""")