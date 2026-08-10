print("=== SISTEMA DE RH ===")
funcionarios = [
    {"Nome": "PEDRO HENRIQUE", "Idade": 22, "CPF": "11111111111", "Cargo": "AUXILIAR", "Salário": 2200.0},
    {"Nome": "RYAN AMORIM", "Idade": 25, "CPF": "22222222222", "Cargo": "APRENDIZ", "Salário": 1000.0},
    {"Nome": "ANA BEATRIZ SILVA", "Idade": 28, "CPF": "33333333333", "Cargo": "ANALISTA", "Salário": 4500.0},
    {"Nome": "CARLOS EDUARDO SANTOS", "Idade": 35, "CPF": "44444444444", "Cargo": "GERENTE", "Salário": 8500.0},
    {"Nome": "MARIANA COSTA", "Idade": 31, "CPF": "55555555555", "Cargo": "COORDENADORA", "Salário": 6200.0},
    {"Nome": "JOAO PEDRO SOUZA", "Idade": 24, "CPF": "66666666666", "Cargo": "DESENVOLVEDOR", "Salário": 3800.0},
    {"Nome": "BEATRIZ NUNES", "Idade": 29, "CPF": "77777777777", "Cargo": "DESIGNER", "Salário": 3500.0},
    {"Nome": "LUCAS OLIVEIRA", "Idade": 27, "CPF": "88888888888", "Cargo": "SUPORTE", "Salário": 2500.0},
    {"Nome": "GABRIELA ROCHA", "Idade": 33, "CPF": "99999999999", "Cargo": "RECURSOS HUMANOS", "Salário": 4200.0},
    {"Nome": "FALCAO VIEIRA", "Idade": 40, "CPF": "10101010101", "Cargo": "DIRETOR", "Salário": 15000.0},
    {"Nome": "JULIA MARTINS", "Idade": 23, "CPF": "12121212121", "Cargo": "ESTAGIARIA", "Salário": 1200.0},
    {"Nome": "MATHEUS LIMA", "Idade": 26, "CPF": "13131313131", "Cargo": "ASSISTENTE", "Salário": 2800.0},
    {"Nome": "AMANDA REIS", "Idade": 30, "CPF": "14141414141", "Cargo": "CONTADORA", "Salário": 5000.0},
    {"Nome": "BRUNO ALVES", "Idade": 45, "CPF": "15151515151", "Cargo": "SUPERVISOR", "Salário": 7000.0},
    {"Nome": "CAMILA MOREIRA", "Idade": 32, "CPF": "16161616161", "Cargo": "PSICOLOGA", "Salário": 4800.0},
    {"Nome": "THIAGO GOMES", "Idade": 38, "CPF": "17171717171", "Cargo": "ADMINISTRADOR", "Salário": 5500.0},
    {"Nome": "LARISSA DIAS", "Idade": 21, "CPF": "18181818181", "Cargo": "RECEPCIONISTA", "Salário": 2000.0},
    {"Nome": "RODRIGO MELO", "Idade": 29, "CPF": "19191919191", "Cargo": "VENDEDOR", "Salário": 3000.0},
    {"Nome": "FERNANDA BARROS", "Idade": 34, "CPF": "20202020202", "Cargo": "SECRETARIA", "Salário": 2600.0},
    {"Nome": "VINICIUS ARAUJO", "Idade": 36, "CPF": "21212121212", "Cargo": "SEGURANCA", "Salário": 2400.0}
]

while True:
    print()
    print("""--> Menu de opções
        1. Cadastrar funcionário.
        2. Ver funcionários.
        3. Remover funcionários.
        
        0. Finalizar o sistema.
    """)
    opcao1 = (input("Digite o número da sua opção: "))
    print()
    if opcao1 == "1":
        while True:
            print("--- CADASTRAMENTO DE FUNCIONÁRIO ---")
            nome = input("Digite o nome do funcionário: ")
            nome = nome.upper()
            idade = int(input("Digite a idade do funcionário: "))
            cpf = input("Digite o CPF do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            cargo = cargo.upper()
            salario = float(input("Digite o salário do funcionário: "))

            novo_func = {
                "Nome": nome,
                "Idade": idade,
                "CPF": cpf,
                "Cargo": cargo,
                "Salário": salario
            }

            funcionarios.append(novo_func)

            print(f"Funcionário {nome.title()} cadastrado com sucesso!")
            
            print("O que deseja fazer?")
            opcao2 = (input("1. Continuar cadastrando.\n2. Finalizar cadastro e voltar para o menu inicial.\n---> "))
            if opcao2 == "1":
                continue
            elif opcao2 == "2":
                break
    elif opcao1 == "2":
        while True:
            print("--- VISUALIZAÇÃO DE FUNCIONÁRIOS ---")
            print("Opções:\n1. Pesquisar funcionários.\n2. Ver lista completa com nome de funcionários.\n0. Sair da visualização.")
            opcao3 = (input("---> "))

            if opcao3 == "1":
                nome_func_pesquisar = input("Digite o nome completo do funcionário: ")
                nome_func_pesquisar = nome_func_pesquisar.upper()

                for funci in funcionarios:
                    if funci["Nome"] == nome_func_pesquisar:
                        print(f"Funcionário(a): {funci["Nome"].title()}")
                        print(f"Idade: {funci["Idade"]}")
                        print(f"CPF: {funci["CPF"]}")
                        print(f"Cargo: {funci["Cargo"].title()}")
                        print(f"Salário: R$ {funci["Salário"]:.2f}")

            elif opcao3 == "2":
                contador = 1
                for func in funcionarios:
                    print(f"{contador}. {func["Nome"].title()} -- CPF: {funci["CPF"]}")
                    contador += 1

            elif opcao3 == "0":
                break
            else:
                print("Opção inválida.")
            
            print("O que deseja fazer? ")
            print("1. Continuar visualizando funcionários.\n2. Finalizar visualização e voltar para o menu inicial.")
            opcao4 = (input("---> "))
            if opcao4 == "1":
                continue
            elif opcao4 == "2":
                break
            else:
                print("Opção inválida, digite novamente.")
    elif opcao1 == "3":
        while True:
            print("--- REMOÇÃO DE FUNCIONÁRIOS ---")
            remover_func = input("Digite o nome completo do funcionário que deseja remover: ")

            remover_func = remover_func.upper()

            for funci in funcionarios:
                if funci["Nome"] == remover_func:
                    print(f"Funcionário: {funci["Nome"].title()}")
                    print(f"Idade: {funci["Idade"]}")
                    print(f"CPF: {funci["CPF"]}")
                    print(f"Cargo: {funci["Cargo"].title()}")
                    print(f"Salário: R$ {funci["Salário"]:.2f}")
                    opcao5 = input("Deseja remover esse funcionário? (SIM/NÃO)\n---> ")

                    if opcao5.upper() == "SIM":
                        funcionarios.remove(funci)
                        print("Funcionário removido.")
                        break
    
            print("O que deseja fazer? ")
            print("1. Continuar removendo funcionários.\n2. Finalizar remoção e voltar para o menu inicial.")
            opcao6 = (input("---> "))
            if opcao6 == "1":
                continue
            elif opcao6 == "2":
                break
            else:
                print("Opção inválida, digite novamente.")
    elif opcao1 == "0":
        break
    else:
        print("Opção inválida, digite novamente.")

print("Sistema de RH finalizado...")