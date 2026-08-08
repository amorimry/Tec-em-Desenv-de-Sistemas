print("--- Cadastro de Paciêntes ---")

pacientes = [
    {"Nome": "Ana Silva", "Idade": 28, "Gênero": "Feminino", "Peso": 62},
    {"Nome": "Carlos Souza", "Idade": 35, "Gênero": "Masculino", "Peso": 84},
    {"Nome": "Mariana Costa", "Idade": 42, "Gênero": "Feminino", "Peso": 68},
    {"Nome": "Bruno Oliveira", "Idade": 19, "Gênero": "Masculino", "Peso": 73},
    {"Nome": "Beatriz Santos", "Idade": 31, "Gênero": "Feminino", "Peso": 55},
    {"Nome": "Ricardo Lima", "Idade": 50, "Gênero": "Masculino", "Peso": 90},
    {"Nome": "Juliana Ribeiro", "Idade": 24, "Gênero": "Feminino", "Peso": 60},
    {"Nome": "Fernando Almeida", "Idade": 45, "Gênero": "Masculino", "Peso": 79},
    {"Nome": "Camila Martins", "Idade": 37, "Gênero": "Feminino", "Peso": 64},
    {"Nome": "Gabriel Pereira", "Idade": 29, "Gênero": "Masculino", "Peso": 81}
]

while True:
    nome = input("Digite o nome do paciênte: ")
    idade = int(input("Digite a idade do paciênte: "))
    genero = input("Digite o gênero do paciênte: ")
    peso = float(input("Digite o peso do paciênte: "))

    paciente = {
        "Nome": nome,
        "Idade": idade,
        "Gênero": genero,
        "Peso": peso
    }

    pacientes.append(paciente)
    print()
    parar = input("Deseja continuar? (S/N): ")
    if parar.upper() == "N":
        print("Encerrando cadastro..")
        break

print()

print("--- Paciêntes cadastrados:")
contador = 1
for pac in pacientes:
    print(f"{contador} - {pac["Nome"]}")
    contador += 1

print()

print("--- Paciêntes acima de 30 anos:")
acima_de_30 = 0
contador = 1
for pac in pacientes:
    idade = pac["Idade"]
    if idade > 30:
        print(f"{contador} - {pac["Nome"]}: {pac['Idade']} anos")
        contador += 1
        acima_de_30 += 1
print(f"Total -acima- de 30 anos: {acima_de_30}")
print(f"Total -abaixo- de 30 anos: {acima_de_30-len(pacientes)}") # Funcionou mas precisa aprimorar pra não sair um resultado negativo

# ficha = input("Deseja imprimir a ficha de algum paciênte? (S/N): ")
# if ficha.upper() == "S":
#     numero_paciente = int(input("Digite o número do paciênte: "))
#     if pac in pacientes: