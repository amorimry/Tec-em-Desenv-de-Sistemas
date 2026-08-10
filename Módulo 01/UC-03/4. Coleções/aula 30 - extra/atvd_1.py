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
        print("""
        - CADASTRO DE FUNCIONÁRIOS -
        """)
        while True:
            nome = input("Digite o nome do Funcionário: ")
            op = utils.vericando_nome(nome)
            if op == True:
                break
            print()

        while True:
            cpf = input("Digite o cpf do Funcionário: ")
            op = utils.verificando_cpf(cpf, funcionarios)
            if op == True:
                break
                # for dados in funcionarios: # verificar se o cpf já existe
                #     if dados["cpf"] == cpf:
                #         print("CPF já existente.")
                #         existe = False # existe
                #     else:
                #         existe = True # não existe
                # if existe == True: # pq ta identada para a frente??
                #     break
            print()
    
        while True:
            salario = float(input("Digite o salário do Funcionário: R$ "))
            op = utils.verificando_salario(salario)
            if op == True:
                # salario = salario.replace(",", ".") # aq é pra se caso a pessoa digitar 1500,50 para trocar a virgula por um ponto e depois converter em float e subir para o dicionário ; quando for perguntar o salário não coloca logo o float, deixa como input e str
                # salario = float(salario)
                break
            print()

        while True:
            cargo = input("Digite o cargo do Funcionário: ")
            op = utils.vericando_cargo
            if op == True:
                break
            print()


        novo_funcionario = {
        "nome": nome,            # Nome completo
        "cpf": cpf,             # CPF (11 dígitos)
        "cargo": cargo,           # Cargo/Função
        "salário": salario        # Salário mensal
    }
        funcionarios.append(novo_funcionario)
        input("""
        Tecle Enter para voltar para o menu...
        """)

    elif op == "2":
        print("""
        - VISUALIZAÇÃO DE FUNCIONÁRIOS -
        """)

        utils.listar_funcionarios(funcionarios)

        input("""
        Tecle Enter para voltar para o menu...
        """)

    elif op == "3":
        print("""
        - EDITAR DE FUNCIONÁRIOS -
        """)

        utils.listar_funcionarios(funcionarios)

        while True:
            num_remover = int(input("Digite o número do funcionário que deseja editar: "))
            if num_remover < 0 or num_remover > len(funcionarios):
                print("Número inválido, digite novamente.")
            else:
                func_escolhido = funcionarios[num_remover-1]
                break
            
        print(f"""
        -- Funcionário --
    Nome: {func_escolhido["nome"]}
    CPF: {func_escolhido["cpf"]}
    Cargo: {func_escolhido["cargo"]}
    Salário: {func_escolhido["salário"]:,.2f}""")
        
        

        input("""
        Tecle Enter para voltar para o menu...
        """)

    elif op == "4":
        pass
    elif op == "0":
        break
    else:
        print("Opção inválida.")