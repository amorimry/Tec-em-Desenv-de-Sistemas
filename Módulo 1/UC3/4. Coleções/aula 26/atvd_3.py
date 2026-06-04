def calculadora (num1, num2, operacao):
    match operacao:
        case "+":
            calculo = num1 + num2
        case "-":
            calculo = num1 - num2
        case "*":
            calculo = num1 * num2
        case "/":
            if num2 == 0:
                calculo = "Não é possível dividir por 0."
            else:
                calculo = num1 / num2
        case _:
            calculo = "Operação inválida."

    return calculo

# numero1 = float(input("Digite um número: "))
# op = input("Digite uma operação: ")
# numero2 = float(input("Digite um próximo número: "))

# print(calculadora(numero1, numero2, op))

print(calculadora(30, 20, "+"))

resultado1 = calculadora(15, 30, "*")
resultado2 = calculadora(15, 0, "/")

print(f"""
{resultado1}
{resultado2}
""")