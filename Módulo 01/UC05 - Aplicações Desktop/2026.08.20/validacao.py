def validar_nome(nome):
    nome = nome.strip() # remove os espaços do inicio e fim
    if nome == "":
        return False
    else:
        return nome.isalpha()