# nome = input("Digite o nome do cliente: ")

# idade = int(input("Digite a idade do cliente: "))

# cpf = input("Digite o cpf: ")

# if len(cpf) == 11:
#     print("CPF válido.")
# else:
#     print("CPF inválido.")

#----------------------------------------------------------- NÍVEL 1

# def verificar_cpf(num_cpf):
#     if len(num_cpf) == 11:
#         print("CPF válido.")
#     else:
#         print("CPF inválido.")

# nome = input("Digite o nome do cliente: ")

# idade = int(input("Digite a idade do cliente: "))

# cpf = input("Digite o CPF: ")

# verificar_cpf(cpf)


# print(f"""-- Cliente --
# Nome: {nome}
# Idade: {idade}
# CPF: {cpf}""")

#----------------------------------------------------------- NÍVEL 2

# def verificar_cpf(num_cpf):
#     if len(num_cpf) == 11:
#         # print("CPF válido.")
#         return "Válido"
#     else:
#         # print("CPF inválido.")
#         return "Inválido"

# nome = input("Digite o nome do cliente: ")

# idade = int(input("Digite a idade do cliente: "))

# while True:
#     cpf = input("Digite o CPF: ")

#     resultado = verificar_cpf(cpf) # a função deve me retornar algo válido ou inválido

#     if resultado == "Válido":
#         print("CPF válido.")
#         break
#     elif resultado == "Inválido":
#         print("CPF inválido.")
#         continue

# print(f"""-- Cliente --
# Nome: {nome}
# Idade: {idade}
# CPF: {cpf}""")

#----------------------------------------------------------- NÍVEL 3

def coletar_cpf():
    while True:
        novo_cpf = input("Digite seu CPF: ")
        if len(novo_cpf) == 11:
            print("CPF válido.")
            return novo_cpf # ou coloca o break e fora do while lá no final da função vc joga o return
        else:
            print("CPF inválido.")
            continue

nome = input("Digite o nome do cliente: ")

idade = int(input("Digite a idade do cliente: "))

cpf = coletar_cpf()

print(f"""-- Cliente --
Nome: {nome}
Idade: {idade}
CPF: {cpf}""")

#----------------------------------------------------------- NÍVEL 4

nome = input("Digite o nome do cliente: ")

idade = int(input("Digite a idade do cliente: "))

cpf = coletar_cpf()

print(f"""-- Cliente --
Nome: {nome}
Idade: {idade}
CPF: {cpf}""")