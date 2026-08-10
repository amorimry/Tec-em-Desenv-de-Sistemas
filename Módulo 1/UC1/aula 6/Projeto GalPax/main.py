from classGalpao import Galpao

galpoes = []

def cadastrar_novo_galpao():
    print("CADASTRO DE NOVO GALPÃO")

    codigo = input("Digite o código do galpão: ").strip() # esse comando verifica espaço vazio ou remove caracteres que vc definir
    if not codigo:
        print("Código não pode ficar vazio.")
        return # serve para voltar para o menu, pelo escopo que ele tá
    
    nome = input("Digite o nome do galpão: ").strip()
    if not nome:
        print("Nome não pode ficar vazio.")
        return
    
    endereco = input("Digite o endereço do galpão: ").strip()
    if not endereco:
        print("Endereço não pode ficar vazio.")
        return
    
    novo_galpao = Galpao(codigo, nome, endereco)

    galpoes.append(novo_galpao)

def remover_galpao():
    print("Você deseja remover o galpão?")
    print(galpoes[0])

print("""
        == Bem vindo a GALPAX ==
""")
while True:
    print("""
    -- Menu de opções --
1. Cadastrar Novo Galpão
2. Remover Galpão
      
0. Finalizar sistema
""")
    op = input("Digite sua opção: ")
    if op == "1":
        cadastrar_novo_galpao()
        print("""
    -- Produto cadastrado com sucesso!
""")
    elif op == "0":
        print("Finalizando programa, até breve!")
        break
    else:
        print("Opção inválida, digite novamente.")