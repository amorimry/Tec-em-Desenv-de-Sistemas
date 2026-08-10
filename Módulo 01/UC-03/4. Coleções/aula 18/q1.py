# 1. Lista de compras
# Crie uma lista com 5 itens de supermercado. Exiba o primeiro item, o último e o total de itens da lista usando len().

supermercado = ["arroz", "feijão", "açúcar", "iorgute", "refrigerante"]

for i in range(5):
    item = input("Digite o novo item: ")
    supermercado.append(item)

print(supermercado)

print(supermercado[0])
print(supermercado[4])
print(len(supermercado))