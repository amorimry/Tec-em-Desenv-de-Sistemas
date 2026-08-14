import json
# # primeiro vc precisa importar o json em si
# # dps vc importa o nome do seu arquivo

with open("2026.08.14/dados_01.json", "r", encoding="utf-8") as arquivo:
# o open abre o arquivo, carrega e depois fecha
    # por isso tem que transformar em dicionario
# (nome do arquivo, forma que ele vai abrir, reconhece acentuação)
# o as vai renomear meu json todo para arquivo
# pesquisar os tipos de encoding
    dados = json.load(arquivo)
    # aqui vai colocar o json, que foi renomeado
    # o load transforma o json em dict ai guarda tudo dentro da variável dados
    # json.load(arquivo); json --> python
    # dump(dado, arquivo); python --> json
    # loads(texto);
    # dumps(dado)

print(dados)


# Transformando dict python em dict json

dados = {"nome": "João", "idade": 20}
with open("2026.08.14/novo_cadastro.json", "w", encoding="utf-8") as arqv:
    json.dump(dados, arqv)
    # json.dump(arquivo que vai virar json (dict), nome da variável (arquivo que será escrito, oq tem dps do open))
    # se caso não tiver o arquivo ele vai criar