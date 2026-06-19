from classPessoa import Pessoa

p1 = Pessoa("Luiz", 20) # criando um objeto a partir de uma classe; utilizando um "molde"; oq entra dentro é atributo/variavel da classe
p2 = Pessoa("João", 18)

print(p1.nome)
print(p1.idade)

print(p2.nome)
print(p2.idade)
print("-------------------------------------------------")
p1.apresentar_pessoa()
print(p1.ano_de_nascimento())
p2.apresentar_pessoa()
print("-------------------------------------------------")
p1.comer("maçã")
print(p1.comendo)
p1.parar_de_comer()
p1.falar()
print(p1.comendo)
p1.parar_de_comer()
print("-------------------------------------------------")
p2.comer("banana")
p2.falar()
p2.parar_de_falar()
p2.comer("uva")
print("-------------------------------------------------")
