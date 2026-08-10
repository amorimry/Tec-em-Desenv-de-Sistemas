# 5. Verificação de estoque
# Um mercadinho tem a lista estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]. Peça ao usuário um produto com input() e informe se ele está ou não disponível no estoque. Depois, exiba o estoque em ordem alfabética usando sorted().

estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]
produto = input("Digite o nome do produto: ")
if produto in estoque:
    print(f"Produto: {produto}\nCom estoque!")
else:
    print("Não temos esse produto no estoque.")

print(estoque.sort()) #mexe na original

estoque_alfabetica = sorted(estoque) #faz uma cópia da lista original e coloca na ordem alfabética


# achou = False

# for p in estoque:
#     if produto == p:
#         achou == True
#         break

# if achou == True:
#     print("Produto em estoque")
# else:
#     print("Produto fora de estoque.")