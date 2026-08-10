from classes import Cliente, Servico, Agendamento
import utils
import storage

lista_clientes, lista_servicos, lista_agendamentos = storage.load_data()


print(f"""
{"="*10} Bem vindo ao Sistema Beauty Manager {"="*10}
""")
while True:
    print(f"""
    {"="*10} Menu de opções {"="*10}

        1. Cadastrar Cliente
        2. Cadastrar Serviço
        3. Agendar Atendimento
        4. Lista de Agendamentos
        5. Cancelar Agendamento
        6. Editar Cliente

        0. Sair do Sistema Beauty Manager
    """)
    op = input("Digite sua opção: ")
    if op == "1":
        print(f"""
{"="*5} Cadastrar Cliente {"="*5}
""")
        dados_cliente = utils.cadastrar_cliente(lista_clientes)

        novo_cliente = Cliente(
            dados_cliente["nome"],
            dados_cliente["telefone"],
            dados_cliente["cpf"],
            dados_cliente["email"]
        )

        lista_clientes.append(novo_cliente)
        storage.save_data(lista_clientes, lista_servicos, lista_agendamentos)

        print("""
    -- Cliente cadastrado com sucesso!
""")
        input("Digite Enter...")

  
    elif op == "2":
        print(f"""
{"="*5} Cadastrar Serviço {"="*5}
""")
        dados_servico = utils.cadastrar_servico()

        novo_servico = Servico(
            dados_servico["nome"],
            dados_servico["valor"],
            dados_servico["duração"]
        )
        
        lista_servicos.append(novo_servico)
        storage.save_data(lista_clientes, lista_servicos, lista_agendamentos)

        print("""
    -- Serviço cadastrado com sucesso!
""")
        input("Digite Enter...")

    elif op == "3":
        print(f"""
{"="*5} Agendar Atendimentos {"="*5}
""")
        dados_agendamento = utils.agendar_atendimento(lista_clientes, lista_servicos, lista_agendamentos)

        if dados_agendamento is not None:

            novo_agendamento = Agendamento(
                dados_agendamento["cliente"],
                dados_agendamento["serviço"],
                dados_agendamento["data"],
                dados_agendamento["horário"]
            )

            lista_agendamentos.append(novo_agendamento)
            storage.save_data(lista_clientes, lista_servicos, lista_agendamentos)

        input("Digite Enter...")

    elif op == "4":
        print(f"""
{"="*5} Lista de Agendamentos {"="*5}
""")
        utils.exibir_agendamentos(lista_agendamentos)

        input("Digite Enter...")

    elif op == "5":
        print(f"""
{"="*5} Cancelar Agendamento {"="*5}
""")
        utils.exibir_agendamentos(lista_agendamentos)
        utils.remover_agendamento(lista_agendamentos)
        storage.save_data(lista_clientes, lista_servicos, lista_agendamentos)

        input("Digite Enter...")

    elif op == "6":
        print(f"""
{"="*5} Editar Cliente {"="*5}
""")
        dados_edit = utils.editar_cliente(lista_clientes)
        if dados_edit is not None:
            i = dados_edit["indice"]
            lista_clientes[i].nome = dados_edit["nome"]
            lista_clientes[i].telefone = dados_edit["telefone"]
            lista_clientes[i].cpf = dados_edit["cpf"]
            lista_clientes[i].email = dados_edit["email"]
            print("Cliente atualizado com sucesso!")
            storage.save_data(lista_clientes, lista_servicos, lista_agendamentos)

        input("Digite Enter...")

    elif op == "0":
        print("Encerrando programa, até breve!")
        break
    else:
        print("Opção inválida, digite novamente.")

        input("Digite Enter...")

input("Digite Enter...")