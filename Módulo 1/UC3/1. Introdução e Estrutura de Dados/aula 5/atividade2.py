# Crie um programa que pede o nome de um produto, o preço de um produto e a quantidade. Calcule o valor total a pagar e exiba na tela. Exiba também True ou False para a meta de venda. Meta é True ou False se a venda for maior ou igual a 100 reais.

print ("Sistema de compras.")
produto = input("Digite o nome do produto comprado: ")
preco = float(input("Digite o preço do produto: "))
quant_produto = int(input("Digite a quantidade comprada: "))

total_pagar = quant_produto * preco
meta_venda = total_pagar >= 100

print (f"""--------- Nota Fiscal ---------
Produto: {produto}
Preço: {preco}
Quantidade: {quant_produto}
Total a pagar: R${total_pagar:.2f}
Meta de venda: {meta_venda}.
""")