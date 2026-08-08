import utils

nome = input("Digite o nome do funcionário: ")

cpf = utils.coletar_cpf()

print(f"""-- Funcionário --
Nome: {nome}
CPF: {cpf}""")