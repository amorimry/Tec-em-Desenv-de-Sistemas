valor_soma = 0

for i in range(5):
    produto = input("Digite o produto: ")
    valor = float(input("Digite o valor do produto: "))

    valor_soma += valor

print(f"Valor da compra: R$ {valor_soma}")