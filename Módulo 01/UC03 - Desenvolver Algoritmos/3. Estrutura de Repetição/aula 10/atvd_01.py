# estruturas de repetição servem justamente pra repetir e trabalhar com acúmulos, deixando o código mais dinâmico
# for -> para
# while -> enquanto
# a variavel i conta quantas vezes o programa ja repetiu, guarda em qualrepetição que você tá; se chama de iterador
# for "elemento" in "lista":

for i in range(5):
    print("Hello World")

nome1 = input("Digite seu nome: ")

for i in range(5):
    print(f"Hello, {nome1}")

nome2 = input("Digite seu nome: ")

repeticao = int(input("Digite quantas vezes quer repetir: "))
for i in range(repeticao):
    print(f"Hello, {nome2}")

