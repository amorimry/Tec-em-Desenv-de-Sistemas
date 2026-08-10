maior = None #nada 
num_digitado = ""

for i in range(5):
    num = float(input(f"Digite o {i+1}° número: "))

    if i == 5:
        num_digitado += (f"{num}")
    else:
        num_digitado += (f"{num} - ")

    if maior == None: 
        maior = num
    
    if num < maior:
        menor = num

print(f"Números digitados: {num_digitado}")
print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")