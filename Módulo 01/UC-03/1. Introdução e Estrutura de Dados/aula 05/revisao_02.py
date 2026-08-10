#Revisão 2: Faça um programa de cadastro de funcionário onde são pedidos 5 informações de um funcionário. Pelo menos uma informação deve ser número inteiro e outra informação deve ser número decimal (float). Ao final imprima a ficha do funcionário (use multi-linha).

print ("Seja bem vindo ao cadastramento de funcionários!")
print ("Vamos iniciar cadastrando um funcionário!")

print ()

print ("Digite alguns dados do funcionário que vai ser cadastrado.")
nome_funcionario = input("Nome do funcionário.\n-->")
cpf_funcionario = input("CPF.\n-->")
# nesse caso o cpf tem que ser armazenado como texto, pois se juntar tudo ele vai ficar um número muito grande ou se tiver um 0 na frente o programa não vai ler, pois não exites número com - na frente
cargo_funcionario = input("Qual o cargo do funcionário?\n-->")
salario_funcionario = float(input("Salário.\n-->"))
nascimento_funcionario = int(input("Ano de nascimento.\n-->"))
altura_funcionario = float(input("Altura do funcionário.\n-->"))
tamanho_farda = input("Tamanho da farda do funcionário.\n-->")

idade_funcionario = 2026 - nascimento_funcionario

print ()

#ficha do funcionário
print ("Ficha do funcionário.")
print (f"""Nome: {nome_funcionario}
CPF: {cpf_funcionario[0:3]}.{cpf_funcionario[3:6]}.{cpf_funcionario[6:9]}-{cpf_funcionario[9:11]}
Cargo: {cargo_funcionario}
Salario: R${salario_funcionario:.2f}
Idade: {idade_funcionario}
Altura: {altura_funcionario}
Tamanho da farda: {tamanho_farda}""")
#usando o :.2f na parte de salário para vir com as duas casas decimais