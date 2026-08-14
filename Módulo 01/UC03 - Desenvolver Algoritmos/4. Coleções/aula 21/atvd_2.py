# Faça um programa que pede as informações nome, espécie, peso e idade de um animal de atendimento veterinário. Salve essas informações em um dicionário e exiba a ficha do paciente.

animal = {
}
# animal = {
#     "Nome": "",
#     "Espeécie": "",
#     "Peso": 0,
#     "Idade": 0
# }

animal["Nome"] = input("Digite o nome do animal: ")
animal["Espécie"] = input("Digite a espécie do animal: ")
animal["Peso"] = float(input("Digite o peso do animal: "))
animal["Idade"] = int(input("Digite a idade do animal em meses: "))

print(f"""-- Lista do Paciente --
Nome: {animal['Nome']}
Espécie: {animal['Espécie']}
Idade: {animal['Idade']} meses
Peso: {animal['Peso']:.2f} kg
""")



animal = {
}

nome = input("Digite o nome do animal: ")
especie = input("Digite a espécie do animal: ")
peso = float(input("Digite o peso do animal: "))
idade = int(input("Digite a idade do animal em meses: "))

animal["Nome"] = nome # guardando assim não tem perigo de inserirem problemas com o input
animal["Espécie"] = especie
animal["Peso"] = peso
animal["Idade"] = idade

print(f"""-- Lista do Paciente --
Nome: {animal['Nome']}
Espécie: {animal['Espécie']}
Idade: {animal['Idade']} meses
Peso: {animal['Peso']:.2f} kg
""")