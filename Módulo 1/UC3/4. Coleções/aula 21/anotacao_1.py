# Tupla
meses = ("Janeiro", "Fevereiro", "Março")
# não tem as funcionalidades da lista (segurança de código); é bom para pode verificar; trabalhar com bancos de dados; é igual a lista mas perdendo a funcionalidade; 

mes = input("Digite um mês: ")
if mes in meses:
    print("Mês válido")
else:
    print("Mês não catalogado")

print(meses[0])

for m in meses:
    print(m)


# Dicionário (dict)
# não ordenado e mutável; parece com a lista; um objeto com várias informações
# CHAVE: VALOR
# identificação/atributo: resposta
funcionário = {
"Nome": "Carlos",
"Salário": 3000,
"Cargo": "Vendedor"
}

pokemon = {
    "Nome": "Pikachu",
    "Tipo": "Elétrico",
    "Ataque": 50
}
print(pokemon)
print(pokemon["Tipo"])