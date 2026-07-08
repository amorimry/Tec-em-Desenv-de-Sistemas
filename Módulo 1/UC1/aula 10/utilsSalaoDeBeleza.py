def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o número do telefone do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    return {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf,
        "email": email
    }

def cadastrar_servico():
    nome = input("Digite o nome do serviço: ")
    valor = float(input("Digite o valor do serviço: "))
    duracao = input("Digite a duração, em minutos, do serviço: ")

    return {
        "nome": nome,
        "valor": valor,
        "duração": duracao
    }

def exibir_cliente(lista):
    for i, nome_cliente in enumerate(lista):
        print(f"{i+1}. {nome_cliente.nome}")

def agendar_atendimento(lista1, lista2):
    nomes_clientes = []
    print("== CLIENTES ==")
    for i, nome_cliente in enumerate(lista1):
        print(f"{i+1}. {nome_cliente.nome}\n")
        nomes_clientes.append(nome_cliente.nome)

    escolha = input("Digite o nome do cliente que deseja agendar um serviço: \n")
    print("== SERVIÇOS ==")
    if escolha.title() in nomes_clientes:
        for i, nome_servico in enumerate(lista2):
            print(f"{i+1}. {nome_servico.nome}\n")
            escolha = input(f"Digite o nome do serviço que deseja agendar para {escolha.title}: \n")
            
    else:
        print("Cliente não cadastrado no sistema, cadastre o cliente primeiro.")