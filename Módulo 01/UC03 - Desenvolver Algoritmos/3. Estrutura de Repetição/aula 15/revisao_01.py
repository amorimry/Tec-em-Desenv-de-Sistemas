idade = 0
while idade < 18:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Você é menor de idade, digite novamente.")

print("Maior de idade.")


while True:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Você é menor de idade, digite novamente.")
    else:
        print("Maior de idade.")
        break

print()
print("Bem vindo ao programa!")