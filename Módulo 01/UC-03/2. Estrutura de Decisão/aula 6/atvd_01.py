# Usando o if e else

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print ("Seu acesso está liberado!")
else:
    print ("Acesso negado!")
    print ("Menor de idade.")
print ("Boa Noite!")


# tudo que tiver recuado é um bloco de notas do que está em cima (identação), então so será executado se o de cima for executado
"""outra forma:
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print ("Seu acesso está liberado!")
if idade < 18:
    print ("Acesso negado!")
    print ("Menor de idade.")
"""