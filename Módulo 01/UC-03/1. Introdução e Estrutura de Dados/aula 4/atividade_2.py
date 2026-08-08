print ("Olá, vamos calcular seus números!")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
# o que entrar aqui vai entrar sempre como str se vc n colocar o tipo
# int para números interios e float para números com casa decimal
# para saber o tipo da variável é só colocar print(type(42)) ou passando o mouse em cima

som = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2

print(f"""O resultado da soma é: {som}
O resultado da subtração é: {sub}
O resultado da multiplicação é: {mult}
O resultado da divisão é: {div}""")