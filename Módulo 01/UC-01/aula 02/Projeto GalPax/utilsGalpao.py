from classGalpao import Galpao

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