contador = 0
while contador <= 10: #enquanto a variavel for menor ou igual a 10, faz o que tá em baixo
    print(contador)
    contador += 1


soma = 0
numero = int(input("Digite um número inteiro (0 para sair): "))
while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero

soma = 0
numero = -1 #coloca um valor que obrigue a entrar na repetição
while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero

soma = 0
numero = None #não é muito legal pois em comparações não vai rodar (<, >), mas da pra usar
# float("-inf")
while numero != 0:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    soma += numero