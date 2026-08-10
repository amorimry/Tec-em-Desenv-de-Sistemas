funcionarios = [
    {"nome": "Fernando", "cpf": "05264785962", "cargo": "Supervisor", "salário": 2500},
    {"nome": "Mariana Souza", "cpf": "98765432100", "cargo": "Gerente de Vendas", "salário": 4800},
    {"nome": "Carlos Eduardo", "cpf": "45612378955", "cargo": "Analista de TI", "salário": 3500},
    {"nome": "Ana Beatriz", "cpf": "78945612311", "cargo": "Assistente de RH", "salário": 2100},
    {"nome": "Rodrigo Alves", "cpf": "32165498722", "cargo": "Desenvolvedor", "salário": 4200},
    {"nome": "Juliana Costa", "cpf": "05975346833", "cargo": "Designer Gráfico", "salário": 2900},
    {"nome": "Ricardo Pereira", "cpf": "85296374144", "cargo": "Suporte Técnico", "salário": 1800},
    {"nome": "Camila Martins", "cpf": "96385274155", "cargo": "Coordenadora de Marketing", "salário": 3900},
    {"nome": "Lucas Oliveira", "cpf": "14725836966", "cargo": "Auxiliar Administrativo", "salário": 1600},
    {"nome": "Beatriz Rocha", "cpf": "75315948677", "cargo": "Recepcionista", "salário": 1550}
]

def cadastrar_funcionario():
    print("CADASTRO DE FUNCIONÁRIOS")

    nome = input("Digite o nome do Funcionário: ")
    cpf = input("Digite o cpf do Funcionário: ")
    salario = float(input("Digite o salário do Funcionário: R$ "))
    cargo = input("Digite o cargo do Funcionário: ")

    novo_funcionario = {
    "nome": nome,            # Nome completo
    "cpf": cpf,             # CPF (11 dígitos)
    "cargo": cargo,           # Cargo/Função
    "salário": salario        # Salário mensal
}
    funcionarios.append(novo_funcionario)

def ver_funcionarios():
    print("VISUALIZAÇÃO DE FUNCIONÁRIOS")

    for i, funcionario in enumerate(funcionarios):
        print(f"{i+1}. {funcionario["nome"]} - {funcionario["cpf"]}")

# def remover_funcionario():
#     print("REMOVER FUNCIONÁRIOS")

#     for i, funcionario in enumerate(funcionarios):
#         print(f"{i+1}. {funcionario["nome"]} - {funcionario["cpf"]}")

#     escolha = int(input("Digite o número do funcionário que você deseja remover: "))

#     if escolha > 0 and escolha <= len(funcionarios):




# -------------------------------------------------------------------------------------- #

while True:
    print("""
=== BEM VINDO AO SISTEMA DA EMPRESA ===
    1. Cadastrar Funcionário
    2. Ver Funcionários
    3. Altera Funcionário
    4. Remover Funcionário
          
    0. Sair""")
    op = input("--> ")

    if op == "1":
        cadastrar_funcionario()
        input("Tecle Enter para voltar para o menu...")
    elif op == "2":
        ver_funcionarios()
        input("Tecle Enter para voltar para o menu...")
    elif op == "3":
        pass
    elif op == "4":
        pass
    elif op == "0":
        break
    else:
        print("Opção inválida.")