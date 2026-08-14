# Faça um menu de atendimento eletrônico que contenham as opções:

# 1. Falar com atendente
# 2. Finalizar contrato
# 3. Abrir nova conta
# 4. Visualizar segunda via da fatura
# 0. Sair

# Cada opção deve exibir uma mensagem relevante. Ao ver a mensagem, volte para o menu e peça uma nova opção do usuário. Se a pessoa escolher a opção Sair, encerre o programa. Caso a pessoa escreva uma opção inválida exiba uma mensagem de erro e volte para o menu.


print("== Menu de Atendimento ==")
voltar = ""
while True:
    print("""
1. Falar com atendente     2. Finalizar contrato
3. Abrir nova conta        4. Visualizar segunda via da fatura
0. Sair""")
    opcao = int(input("Digite sua opção: "))
    if opcao == 0:
        print("Atendimento finalizado!")
        break
    elif opcao == 1:
        print("Estamos com lotação no nosso serviço, mas logo logo entraremos em contato!")
        voltar = input("Deseja voltar para o menu? (S/N): ")
        if voltar == "S" or voltar == "s" or voltar == "Sim" or voltar == "sim":
            continue
        else:
            print("Atendimento finalizado!")
            break
    elif opcao == 2:
        print("Lamentamos por essa sua escolha, um atendente logo logo irá alinhar com você esse processo, aguarde!")
        voltar = input("Deseja voltar para o menu? (S/N): ")
        if voltar == "S" or voltar == "s" or voltar == "Sim" or voltar == "sim":
            continue
        else:
            print("Atendimento finalizado!")
            break
    elif opcao == 3:
        print("Entendido! Um atendente irá entrar em contato para pegar seus dados.")
        voltar = input("Deseja voltar para o menu? (S/N): ")
        if voltar == "S" or voltar == "s" or voltar == "Sim" or voltar == "sim":
            continue
        else:
            print("Atendimento finalizado!")
            break
#-----------------------
    elif opcao == 4:
        print("Acabamos de enviar a segunda via da sua fatura para seu e-mail.")
        while True:
            voltar = input("Deseja voltar para o menu? (S/N): ")
            if voltar == "S" or voltar == "s" or voltar == "Sim" or voltar == "sim":
                break
            elif voltar == "N" or voltar == "n" or voltar == "Não" or voltar == "não":
                break
            else:
                print("Não entendi, digite novamente o que deseja fazer.")
        if voltar == "S" or voltar == "s" or voltar == "Sim" or voltar == "sim":
            continue
        elif voltar == "N" or voltar == "n" or voltar == "Não" or voltar == "não":
            print("Atendimento finalizado!")
            break
#-----------------------
    else:
        print("Opção inválida, digite novamente!")
