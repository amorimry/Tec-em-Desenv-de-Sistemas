# Crie uma calculadora onde a pessoa informa dois números e um operação (+,-,*,/). Ao terminar um cálculo exiba o resultado e pergunte se a pessoa deseja realizar outro cálculo. Caso a resposta seja sim, peça novamente os dois números e operação, caso a pessoa não deseje continuar encerre o programa.


while True:
    num1 = float(input("Digite um número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o próximo número: "))

    match operacao:
        case "+":
            print(f"Resultado: {num1 + num2}")
        case "-":
            print(f"Resultado: {num1 - num2}")
        case "*":
            print(f"Resultado: {num1 * num2}")
        case "/":
            if num2 == 0:
                print("Não é possivel dividir por 0.")
            else:
                print(f"Resultado: {num1 / num2}")
        case _:
            print("Cálculo inválido, digite novamente.")
            continue

    parar = input("Deseja continuar calculando? (S/N): ")

    if parar == "N" or parar == "n":
        break