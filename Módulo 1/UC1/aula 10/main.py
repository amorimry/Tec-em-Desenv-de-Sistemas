from classSalaoDeBeleza import Cliente, Servico, Agendamento
import utilsSalaoDeBeleza

lista_clientes = [
    Cliente("Ana Silva", "85952478563", "23562485692", "ana.silva@email.com"),
    Cliente("Bruno Souza", "85963247561", "03641251478", "bruno.souza@email.com"),
    Cliente("Carla Oliveira", "85965234475", "09547852315", "carla.oliveira@email.com"),
    Cliente("Diego Santos", "85965554782", "56474123058", "diego.santos@email.com"),
    Cliente("Elena Costa", "8596322541", "65874123584", "elena.costa@email.com")
]
lista_servicos = [
    Servico("Corte Feminino", 80.0, "45"),
    Servico("Escova", 50.0, "30"),
    Servico("Manicure", 35.0, "40"),
    Servico("Pedicure", 40.0, "45"),
    Servico("Hidratação", 120.0, "60")
]
lista_agendamentos = []

print(f"""
{"="*10} Bem vindo ao Sistema Beauty Manager {"="*10}
""")
while True:
    print(f"""
    {"="*10} Menu de opções {"="*10}

        1. Cadastrar Cliente
        2. Cadastrar Serviço
        3. Agendar Atendimento
        4. Listar Agendamentos
        5. Cancelar Agendamento

        0. Sair do Sistema Beauty Manager
    """)
    op = input("Digite sua opção: ")
    if op == "1":
        print(f"""
{"="*5} Cadastra Cliente {"="*5}
""")
        dados_cliente = utilsSalaoDeBeleza.cadastrar_cliente() #cadastra meu cliente, pelo utils, e me retorna o cliente com as informações em uma lista, jogando dentro da variável dados_cliente

        novo_cliente = Cliente(
            dados_cliente["nome"],
            dados_cliente["telefone"],
            dados_cliente["cpf"],
            dados_cliente["email"]
        ) #passo a instanciar o meu cliente colocando ele em uma classe, pego uma variável qualquer, chamo a classe dele e depois passo a puxar os dados da lista para cada informação que minha classe precisa

        lista_clientes.append(novo_cliente)

        print("Cliente cadastrado com sucesso!")

        utilsSalaoDeBeleza.exibir_cliente(lista_clientes)
  
    elif op == "2":
        print(f"""
{"="*5} Cadastra Serviço {"="*5}
""")
        dados_servico = utilsSalaoDeBeleza.cadastrar_servico()

        novo_servico = Servico(
            dados_servico["nome"],
            dados_servico["valor"],
            dados_servico["duração"]
        )
        lista_servicos.append(novo_servico)

        print("Serviço cadastrado com sucesso!")

    elif op == "3":
        print(f"""
{"="*5} Agendar Atendimentos {"="*5}
""")
        utilsSalaoDeBeleza.agendar_atendimento(lista_clientes, lista_servicos)
    elif op == "4":
        print(f"""
{"="*5} Listar Agendamentos {"="*5}
""")
    elif op == "5":
        print(f"""
{"="*5} Cancelar Agendamento {"="*5}
""")
    elif op == "0":
        print("Encenrrando programa, até breve!")
        break
    else:
        print("Opcão inválida, digite novamente.")
input("Digite Enter...")