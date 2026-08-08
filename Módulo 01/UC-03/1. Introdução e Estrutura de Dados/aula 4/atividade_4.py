print(f"Vamos organizar seus produtos comprados!")

produto = input("O que vc comprou?: ")
valor = float(input("Qual o valor do produto?: "))
quantidade = int(input("Quantos produtos você comprou?: "))

valor_produto = valor*quantidade

print(f"Você comprou um(a) {produto} e irá pagar R${valor_produto:.2f} por ele.")
# o . significa que ta fazendo uma formatação e o 2f é pra ter duas casa decimais, 1f é uma casa decimal, 2f é dua, 3f é 3...