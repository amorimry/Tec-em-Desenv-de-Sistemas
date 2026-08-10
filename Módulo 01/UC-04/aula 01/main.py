# nome main é onde roda nosso programa em si, melhor nomear assim / aq fica so a execução do código

# func_1 = {
#     "nome": "João",
#     "salário": 5000,
#     "cargo": "Vendedor",
#     "idade": 25
# }

# func_1["telefone"] = "85985647752"

# print(func_1)


# NOVA FORMA COM PROGRAMAÇÃO ORIENTADA

from classFuncionario import Funcionario # do arquivo tal vc me importa tal coisa

func_1 = Funcionario("João", 5000, 25, "Vendedor")

print(func_1.nome)