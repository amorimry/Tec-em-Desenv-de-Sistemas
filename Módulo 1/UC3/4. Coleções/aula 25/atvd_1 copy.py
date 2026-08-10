# 6 — 🌱 Estoque de Hortifruti
# Atributos: produto, unidade (kg/unidade), quantidade em estoque, preço, fornecedor

# Funcionalidade extra: alertar quais produtos estão abaixo de uma quantidade mínima informada pelo usuário

def imprimirLista(lista):
    for i,item in enumerate(lista):
            print(f"{i+1}. {item["Nome"]} | Estoque: {item["Estoque"]}")

produtos = [
    {
        "Nome": "Tomate",
        "Preço": 8.50,
        "Estoque": 120,
        "Unidade": "kg",
        "Fornecedor": "Verde Vida Hortifruti"
    },
    {
        "Nome": "Banana Prata",
        "Preço": 5.99,
        "Estoque": 200,
        "Unidade": "kg",
        "Fornecedor": "Frutas do Vale"
    },
    {
        "Nome": "Alface Americana",
        "Preço": 3.50,
        "Estoque": 80,
        "Unidade": "un",
        "Fornecedor": "Horta Natural"
    },
    {
        "Nome": "Batata Inglesa",
        "Preço": 6.75,
        "Estoque": 150,
        "Unidade": "kg",
        "Fornecedor": "Campo Fresco"
    },
    {
        "Nome": "Cenoura",
        "Preço": 4.20,
        "Estoque": 100,
        "Unidade": "kg",
        "Fornecedor": "Raízes da Terra"
    },
    {
        "Nome": "Maçã Gala",
        "Preço": 9.90,
        "Estoque": 90,
        "Unidade": "kg",
        "Fornecedor": "Pomar Central"
    },
    {
        "Nome": "Cebola",
        "Preço": 7.30,
        "Estoque": 130,
        "Unidade": "kg",
        "Fornecedor": "Sabor do Campo"
    },
    {
        "Nome": "Mamão Formosa",
        "Preço": 6.10,
        "Estoque": 60,
        "Unidade": "kg",
        "Fornecedor": "Frutas Tropicais"
    },
    {
        "Nome": "Cheiro Verde",
        "Preço": 2.80,
        "Estoque": 70,
        "Unidade": "molho",
        "Fornecedor": "Horta Feliz"
    },
    {
        "Nome": "Laranja Pera",
        "Preço": 4.99,
        "Estoque": 180,
        "Unidade": "kg",
        "Fornecedor": "Citrus Brasil"
    }
]

while True:
    print("== BEM VINDO AO SISTEMA DE GERENCIAMENTO HORTIFRUTI ==")
    print(f"""
MENU DE OPÇÕES:
          
    1. Cadastrar um produto
    2. Ver lista de produtos
    3. Ver produto específico
    4. Ver produtos pelo estoque mínimo
    5. Pesquisar produtos pelo preço
    6. Comprar algum produto

    0. Sair 
""")
    op = input("Digite a opção desejada: ")

    if op == "1":
        print("__ CADASTRO DE PRODUTO __")

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        unidade = input("Digite o tipo de unidade (kg/und): ")
        estoque = int(input("Digite a quantidade do produto: "))
        fornecedor = input("Digite o fornecedor: ")

        novo_produto = {
            "Nome": nome,
            "Preço": preco,
            "Estoque": estoque,
            "Unidade": unidade,
            "Fornecedor": fornecedor
        }

        produtos.append(novo_produto)

        print("-- Produto cadastrado com sucesso!")
        print(f"Quantidade de produtos no catálogo: {len(produtos)}")
        
    elif op == "2":
        print("__ VER PRODUTOS __")

        for i,produto in enumerate(produtos):
            print(f"{i+1}. {produto["Nome"]} | Estoque: {produto["Estoque"]}")

    elif op == "3":
        print("__ ESCOLHER PRODUTO __")

        contador = 1
        for produto in produtos:
            print(f"{contador}. {produto["Nome"]} | {produto["Estoque"]}")
            contador += 1
        
        numero = int(input("Digite o número do produto que deseja visualizar: "))
        if numero == 0:
            print("CANCELANDO OPERAÇÃO")
            break
        elif numero >= 1 and numero <= len(produtos):

            produto_escolhido = produtos[numero-1]

            print(f"""
INFORMAÇÕES DO PRODUTO
        
    Nome: {produto_escolhido["Nome"]}
    Preço: R$ {produto_escolhido["Preço"]:,.2f}
    Estoque: {produto_escolhido["Estoque"]} {produto_escolhido["Unidade"]} 
    Fornecedor: {produto_escolhido["Fornecedor"]}
    """)
        else:
            print("NÚMERO INVÁLIDO")
        
    elif op == "4":
        print("__ VER PRODUTOS POR ESTOQUE __")
        estoque_minimo = int(input("Digite o estoque mínimo: "))

        print("Nº | Nome | Estoque | Unidade")
        for i, produto in enumerate(produtos):
            if produto["Estoque"] <= estoque_minimo:
                print(f"{i+1} | {produto["Nome"]} | {produto["Estoque"]} | {produto["Unidade"]}")

    elif op == "5":
        print("__ PESQUISAR PELO PREÇO __")
        valor = float(input("Digite o preço que dejesa pesquisar: "))

        print("-- Produtos com preço igual ou acima do preço digitado --")
        contador = 1
        for produto in produtos:
            if produto["Preço"] >= valor:
                print(f"{contador}. {produto["Nome"]} | R$ {produto["Preço"]:,.2f} | {produto["Estoque"]} {produto["Unidade"]}")
            contador += 1 

    elif op == "6":
        print("__ VENDA __")
        print("-- Produtos em estoque:")
        for i,produto in enumerate(produtos):
            print(f"""
    {i+1}. {produto["Nome"]} | R$ {produto["Preço"]:,.2f}
    Estoque: {produto["Estoque"]} {produto["Unidade"]} 
    Fornecedor: {produto["Fornecedor"]}
    """)

        while True:
            escolha = int(input("Digite o número do produto que deseja comprar: "))
            if escolha >= 1 and escolha <= len(produtos):
                produto_para_venda = produtos[escolha-1]
                break
            else:
                print("Digite o número de um produto válido!")
            
        print(f"""
    Nome: {produto_para_venda["Nome"]}
    Preço: R$ {produto_para_venda["Preço"]:,.2f}
    Estoque: {produto_para_venda["Estoque"]} {produto_para_venda["Unidade"]} 
    Fornecedor: {produto_para_venda["Fornecedor"]}
    """)
        
        while True:
            qtd = float(input("Digite a quantidade (kg/un) que deseja comprar: "))
            if qtd <= produto_para_venda["Estoque"] and qtd > 0:
                break
            else:
                print("Estoque insuficiente! Digite novamente.")
                
        pagar = produto_para_venda["Preço"] * qtd
        print(f"Valor a ser pago no total: R$ {pagar:,.2f}")

        produto_para_venda["Estoque"] -= qtd
        print()
        print("-- Produto atualizado")
        print(f"""
    Nome: {produto_para_venda["Nome"]}
    Preço: R$ {produto_para_venda["Preço"]:,.2f}
    Estoque: {produto_para_venda["Estoque"]} {produto_para_venda["Unidade"]} 
    Fornecedor: {produto_para_venda["Fornecedor"]}
    """)

    elif op == "0":
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("DIGITE UMA OPÇÃO VÁLIDA")

    input("DIGITE ENTER PARA CONTINUAR...")