def minha_funcao(): # o que entra dentro do parenteses é chamado de parâmetros
    print("testanto a nova função")
    print("função nova")

minha_funcao() # precisa chamar a função para o seu código antes de executar; o uso dos parenteses da o comando de rodar para a função

def ver_detalhes(nome, salario, cargo):
    print(f"""
-- Detalhes do Funcioário
          
Nome: {nome}
Salário: R$ {salario:,.2f}
Cargo: {cargo}
""") # as variaveis aq dentro so exitem aq dentro
    
ver_detalhes("Daniel", 3200, "Vendedor")

funcionario_1 = {"Nome": "Paulo", "Salário": 5200, "Cargo": "Gerente"}

ver_detalhes(funcionario_1["Nome"], funcionario_1["Salário"], funcionario_1["Cargo"])

nome = input("Digite o nome do funcionario: ") # não é legal colocar input dentro da função, isso deixa as coisas mais problemáticas, até pq tudo que vc cria dentro de uma função só existe lá dentro
salario = float(input("Digite o salário: "))
cargo = input("Digite o cargo: ")

ver_detalhes(nome, salario, cargo)



def minha_funcao(): 
    print("testanto a nova função")
    print(f"{texto}")

texto = "Oláaaa" # escopo
minha_funcao() 