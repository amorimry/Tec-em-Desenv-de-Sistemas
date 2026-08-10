# Utilizando a agenda do problema anterior, realize as seguintes melhorias no programa:

# 1 - Peça para o usuário o nome e telefone de 5 novas pessoas e adicione na agenda.
# 2 - Utilize um loop while para permitir que a pessoa consulte os números da agenda. O usuário deverá escrever o nome de um dos contatos e o programa deve exibir o número na tela (caso exista, se não exibir mensagem de erro) e depois pedir o nome do próximo. Continue até que a pessoa escreva o nome "Sair".
# 3 - No começo de cada repetição, exiba a lista de contatos na tela.

agenda = {
    "JULIA": "85985423657",
    "GABRIEL": "85996547231",
    "FERNANDO": "85935246875",
    "HENRIQUE": "85932597564"
}

print("Digite 5 novos nomes e contatos para cadastrar.")
for i in range(2):
    nome = input(f"{i+1}° Nome: ")
    telefone = input("Telefone: ")

    agenda[nome.upper()] = telefone

    print()

print("Números adicionados com sucesso.")
print()

print("-- Visualizar Telefones --")
while True:
    print("Contatos disponíveis: ")
    for i in agenda:
        print(f"- {i.title()}")

    print()
    nome_procurar = input("Digite o nome que deseja saber o número (digite sair para finaliar a busca): ")
    if nome_procurar.upper() == "SAIR":
        break

    # print(agenda.get(nome_procurar.upper(), "Nome não cadastrado, digite novamente."))

    print(f">> {nome_procurar.title()}: {agenda.get(nome_procurar.upper(), "Nome não cadastrado, digite novamente.")}")

    # if nome_procurar.upper() in agenda:
    #     print(f">> {nome_procurar.title()}: {agenda[nome_procurar.upper()]}")
    # elif nome_procurar.upper() == "SAIR":
    #     break
    # else:
    #     print("Nome não cadastrado, digite novamente.")

    input("DIGITE ENTER PARA CONTINUAR..")
    
    print()

print("Lista encerrada.")
print("Agenda completa:")
for i in agenda:
    print(f"- {i}: {agenda[i]}")
