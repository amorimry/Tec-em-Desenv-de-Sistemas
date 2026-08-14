import json

# 1 - ler o arquivo existente
with open("2026.08.14/dados_01.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# 2 - adicionar novo hobby na lista
dados["hobbies"].append("cozinhar")

# 3 - salvar de volta o arquivo
with open("2026.08.14/dados_01.json", "w", encoding="utf-8") as arquivo: # a variável vai se sobreescrever
    json.dump(dados, arquivo, ensure_ascii=False)