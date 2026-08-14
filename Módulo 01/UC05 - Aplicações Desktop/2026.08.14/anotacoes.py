# para poder guardar uma quantidade não muito grande de dados, a gente pode usar o json
# arquivo chave --> valor

# dict em python
pessoa = {
    'nome': "Ana",
    'idade': 28,
    'estudante': True,
    'cidade': None,
    'hobbies': ["ler", "escrever", "estudar", "programar"]
}

# dict em json
json = {
    "nome": "Ana",
    "idade": 28,
    # "estudante": true,
    # "cidade": null,
    "hobbies": ["ler", "escrever", "estudar", "programar"]
}

# com funciona o json:
# true e false é com letra minúscula;
# usa-se null em vez de none;
# em json tem que usar aspas duplas;
# não tem variável pra guardar pois é só um arquivo, ele não roda;
# o json só aceita lista e dicionário, por enquanto não aceita tuplas;
# possivel usar identação