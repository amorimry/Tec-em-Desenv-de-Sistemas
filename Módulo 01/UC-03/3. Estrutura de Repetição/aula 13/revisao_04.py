# 4. Uma estação de metereologia contratou você para criar um programa que calcula a média de temperatura de um dia. O seu programa deve: perguntar quantas temperaturas serão inseridas fazer a leitura dessas temperaturas e ao final informar qual foi a temperatura média daquele dia, a temperatura máxima e a temperatura mínima do dia.

print("""== Programa de Temperaturas ==
    
OBS: Digite as temperaturas em grau Celsius!""")
print()
num_temp = int(input("Digite quantas temperaturas serão contabilizas: "))

print()

soma_temp = 0
lista = ""
maior_temp = None
menor_temp = None

for i in range(num_temp):
    temperatura = float(input(f"Digite a {i+1}° temperatura: "))
    soma_temp += temperatura

    if i == num_temp - 1:
        lista += (f"{temperatura}°C")
    else:
        lista += (f"{temperatura}°C | ")
    #-----------------------------
    if maior_temp == None: #como começa sem nada, vc já  implementa o primeiro número que foi escrtio
        maior_temp = temperatura
    
    if temperatura > maior_temp: #nas próximas já vai valendo o que for maior
        maior_temp = temperatura

    if menor_temp == None: #mesma lógica da maior
        menor_temp = temperatura

    if temperatura < menor_temp:
        menor_temp = temperatura

media = soma_temp/num_temp

print(f"""
--- Resultado do Dia ---
      
Temperaturas catalogadas:
{lista}
      
A temperatura mais ALTA foi de {maior_temp}°C
A temperatura mais BAIXA foi de {menor_temp}°C

A media das temperaturas digitadas é de {media}°C""")