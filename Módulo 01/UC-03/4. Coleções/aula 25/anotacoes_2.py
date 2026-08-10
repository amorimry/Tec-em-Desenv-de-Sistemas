# USANDO FUNÇÕES
# você pega um bloco de código, joga em uma função e utiliza aquilo sempre que quiser

def hello_word():
    print("Hello World!")
    print("Welcome programmer.")
    print("Ryan :^")
    print("-------------------")

hello_word()
hello_word()
hello_word()
hello_word()
hello_word()

def saudacao(nome, idade): # aqui vc diz que a função precisa receber algo, precisa receber essa informação antes de rodar, se chama parâmetro
    print(f"Seja bem vindo, {nome}! Você tem {idade} anos.")
    print(f"Olá {nome}")

saudacao("Gabriel", 23) # aqui eu forneci a info e a função vai rodar com o nome que tiver aqui
saudacao("Marcelo", 30) # cuidado com a ordem adequada
saudacao("Liz", 29)
saudacao("Pedro", 18)