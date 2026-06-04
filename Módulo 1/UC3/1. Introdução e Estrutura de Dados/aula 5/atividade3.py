idade = int(input("Digite a idade do visitante: "))
peso = float(input("digite o peso do visitante: "))

checagem_idade = idade >= 13
checagem_peso = peso >= 50

print (f"""
            Checagem de idade: {checagem_idade}
            Checagem do peso: {checagem_peso}
""")