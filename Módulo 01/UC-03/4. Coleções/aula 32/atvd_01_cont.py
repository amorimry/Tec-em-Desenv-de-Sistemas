import utils

funcionarios = [
    {"nome": "Fernando", "cpf": "05264785962", "cargo": "Supervisor", "salário": 2500.50},
    {"nome": "Mariana Souza", "cpf": "98765432100", "cargo": "Gerente de Vendas", "salário": 4800},
    {"nome": "Carlos Eduardo", "cpf": "45612378955", "cargo": "Analista de TI", "salário": 3500.60},
    {"nome": "Ana Beatriz", "cpf": "78945612311", "cargo": "Assistente de RH", "salário": 2100},
    {"nome": "Rodrigo Alves", "cpf": "32165498722", "cargo": "Desenvolvedor", "salário": 4200},
    {"nome": "Juliana Costa", "cpf": "05975346833", "cargo": "Designer Gráfico", "salário": 2900.20},
    {"nome": "Ricardo Pereira", "cpf": "85296374144", "cargo": "Suporte Técnico", "salário": 1800},
    {"nome": "Camila Martins", "cpf": "96385274155", "cargo": "Coordenadora de Marketing", "salário": 3900},
    {"nome": "Lucas Oliveira", "cpf": "14725836966", "cargo": "Auxiliar Administrativo", "salário": 1600.80},
    {"nome": "Beatriz Rocha", "cpf": "75315948677", "cargo": "Recepcionista", "salário": 1550.10}
]

while True:
    print("""
=== BEM VINDO AO SISTEMA DA EMPRESA ===

    1. Cadastrar Funcionário
    2. Ver Funcionários
    3. Editar Funcionário
    4. Remover Funcionário
          
    0. Sair""")
    op = input("--> ")

    if op == "1":
       pass

    elif op == "2":
        pass

    elif op == "3":
        print("""
        - EDITAR DE FUNCIONÁRIOS -
        """)

        utils.listar_funcionarios(funcionarios) # puxou a função de listar os funcionários

        # if len(funcionarios) == 0: # validação só para caso não tiver nada na lista
        #     print("Nenhum funcionário cadastrado.")

        num_func = utils.num_funcionario(funcionarios) # função para escolher o número da posição do funcionário

        funcionario_escolhido = funcionarios[num_func-1] # pego o número do func que guardei na variável num_func, tiro 1, pego a posição dele na lista e depois eu guardo esse funcionário em outra variavel funcionario_escolhido
            
        print(f"""
        -- Funcionário que será EDITADO --
    Nome: {funcionario_escolhido["nome"]}
    CPF: {"*"*8}{funcionario_escolhido["cpf"][8:10]}
    Cargo: {funcionario_escolhido["cargo"]}
    Salário: {funcionario_escolhido["salário"]:,.2f}""") # apresento o funcionário que escolhi
        
        print("Altere as informações seguintes. Deixe vazio se caso não quiser editar!")

        novo_nome = input(f"Digite o novo nome: ")
        if novo_nome:
            funcionario_escolhido["nome"] = novo_nome

        novo_cpf = input("Digite o novo CPF: ")
        if novo_cpf:
            funcionario_escolhido["cpf"] = novo_cpf

        novo_cargo = input("Digite o novo cargo: ")
        if novo_cargo:
            funcionario_escolhido["cargo"] = novo_cargo

        novo_salario = input("Digite o novo salário: ")
        if novo_salario:
            funcionario_escolhido["salário"] = float(novo_salario)

        input("""
        Tecle Enter para voltar para o menu...""")

    elif op == "4":
        print("""
        - APAGAR FUNCIONÁRIO -
        """)

        utils.listar_funcionarios(funcionarios) # função para mostrar os funcionários

        func_escolhido = utils.num_funcionario(funcionarios) # o número do func escolhido entra dentro da variavel e guarda

        funcionario_removido = funcionarios.pop(func_escolhido-1) # aqui remove o funcionario de acordo com sua posição, pois o pop remove pelo índice (número) ; guarda o func removido em uma variavel para poder apresentar depois, só se quiser

        print(f"""
        -- Funcionário que foi REMOVIDO --
    Nome: {funcionario_removido["nome"]}
    CPF: {funcionario_removido["cpf"]}
    Cargo: {funcionario_removido["cargo"]}
    Salário: {funcionario_removido["salário"]:,.2f}""")

        input("""
        Tecle Enter para voltar para o menu...
        """)

    elif op == "0":
        print("""
        - SAINDO DO PROGRAMA -
        """)
        break
    else:
        print("Opção inválida.")