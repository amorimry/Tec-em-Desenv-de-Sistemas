# 5. Crie um programa que recebe o preço e a quantidade de um produto que foi vendido. Calcule o valor final a pagar considerando um desconto que segue a regra abaixo:

# Se o valor total da venda superar 100 reais ou o cliente comprar 5 produtos -> Desconto de 15%
# Se o valor for menor do que 100 e o cliente comprou pelo menos 3 produtos -> Desconto de 10%
# Em qualquer outra situação não aplicar desconto

# Ao final imprima o valor original do cálculo e o valor a ser pago pelo cliente

print ("== Validade de descontos ==")
produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quant_produto = int(input("Digite a quantidade que foi comprada: "))
valor_pg = preco_produto * quant_produto

print ()

print ("== Nota de descontos ==")
print (f"""Produto: {produto}
Preço: {preco_produto}
Quantidade: {quant_produto}

Valor total: {valor_pg}
""")
print ()
if valor_pg >= 100 or quant_produto >= 5: