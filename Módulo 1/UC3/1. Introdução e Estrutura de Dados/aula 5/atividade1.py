# Crie um programa que recebe a idade de uma pessoa e exiba na tela se ela pode entrar ou não (True ou False). O critério para entrar no sistema é ter idade maior ou igual a 18 anos.

idade = int(input("Digite sua idade: "))
verificacao_idade = idade>=18
print (f"Acesso ao Sistema: {verificacao_idade}")