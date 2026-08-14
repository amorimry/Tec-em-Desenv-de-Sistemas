# 4. Receba o nome, o preço e a quantidade de 5 produtos diferentes. Ao final exiba o valor total que o cliente deverá pagar.
# Bônus: Exiba uma nota fiscal com tudo que foi comprado e as informações da venda ao final.

produto_comprado = ""
preco = 0
qtd = 0
valor_pago = 0
valor_total = 0
nota_fiscal = ""

for i in range(3):
    #pedir o nome, preço e qtd de cada um dos produtos comprados e repetir
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    qtd = int(input("Digite a quantidade comprada: "))

    valor_pago = (preco * qtd) #aqui é quanto o cliente pagou, usando a quantidade e o valor de cada produto separadamente
    valor_total += valor_pago #aqui vai guardar o valor que foi pago em cada produto para no final fazer a soma de quanto foi pago totalmente

    nota_fiscal += (f"{produto}   |    R${preco:.2f}    |    {qtd} --- R${valor_pago:.2f}\n") #aqui vc já vai construindo cada linha da nota fiscal

    print()

valor_total = valor_pago

print()

print("== Nota Fiscal ==")
print(f"{nota_fiscal}")
print(f"O total a ser pago é: R${valor_total:.2f}")