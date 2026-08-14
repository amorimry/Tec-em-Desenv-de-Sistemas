nome1 = "José"
nome2 = "Maria"

nome2 = nome1

nome1 = "Carlos"

print(nome1)
print(nome2)


# REFERÊNCIA EM LISTA
frutas = ["uva", "maçã", "banana"]
vegetais = ["alface", "cenoura", "penino"]

vegetais = frutas # aqui as duas variaveis vão estar apontando para a mesma lista

print(frutas) # quando trabalha com lista a gente trabalha com a referência da lista
print(vegetais)

frutas.append("abacaxi")

print(frutas)
print(vegetais)

vegetais.remove("uva")

print(frutas) # usando a mesma lista em duas variáveis
print(vegetais)

print(frutas[0])
print(vegetais[0])



# frutas = ["uva", "maçã", "banana"]
# vegetais = ["alface", "cenoura", "penino"]

# vegetais = frutas.copy() # caracteristicas para coleções


funcionarios = [
    {"Nome": "Paulo", "Salário": 1600},
    {"Nome": "Joana", "Salário": 1800}
]
print(funcionarios)
funcionarios[1]["Salário"] = 2000
print(funcionarios)

func_escolhido = funcionarios[1] # aqui eu não faço uma cópia, eu levo justamente o dicionario que eu tenho dentro da lista; deixa o processo mais simples, pra não precisar mudar e guardar de novo

func_escolhido["Salário"] = 2300
print(funcionarios)