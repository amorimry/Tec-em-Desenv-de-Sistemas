# CRUDE

# --> Create:
produto = {
} # Chave: Valor

# Adicionar no dict
produto["Nome"] = input("Digite o nome do produto: ")
produto["Preço"] = float(input("Digite o preço do produto: "))

# --> Read
print(produto)

print(produto["Nome"])
print(produto["Preço"])

print(produto.get("Estoque", "Chave não encontrada"))

# --> Update
produto["Nome"] = "Café"
produto["Preço"] = 8.50

print(produto)

# --> Delete
# produto.clear() # Remove todos os elementos do dict
del produto["Nome"] # Remove algo específico
produto.pop("Estoque", "Chave não encontrada para remover")

print(produto)