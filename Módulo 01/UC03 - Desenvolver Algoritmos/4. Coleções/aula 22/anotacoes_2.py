# é bom trabalhar com lista
funcionarios = [
    {"Nome": "Patrícia", "Idade": 32, "Cargo": "Marketing", "Salário": 2500},
    {"Nome": "Carlos", "Idade": 21, "Cargo": "Auxiliar Adm", "Salário": 1200},
    {"Nome": "Pedro", "Idade": 25, "Cargo": "Porteiro", "Salário": 1800}
]

nome = input("Digite o nome do funcionário: ")
idade = int(input("Digite a idade: "))
cargo = input("Digite o cargo: ")
salario = float(input("Digite o salário: "))

novo_funcionario = {
    "Nome": nome,
    "Idade": idade,
    "Cargo": cargo,
    "Salário": salario
}

funcionarios.append(novo_funcionario)

print(funcionarios) # todos os funcionários
print(funcionarios[0]) # um funcionário específico
print(funcionarios[0]["Nome"]) # elemento específico de um funcionário específico

print("Lista de funcionários")
contador = 1
for func in funcionarios:
    print(f"{contador}. {func["Nome"]}")
    contador += 1

numero = int(input("Digite o número do funcionário que deseja visualizar: "))
# print(funcionarios[numero-1])

funcionario_escolhido = funcionarios[numero-1]
print(f"""
Ficha Profissional

    Nome: {funcionario_escolhido["Nome"]}
    Idade: {funcionario_escolhido["Idade"]} anos
    Cargo: {funcionario_escolhido["Cargo"]}
    Salário: R$ {funcionario_escolhido["Salário"]:.2f}

""")