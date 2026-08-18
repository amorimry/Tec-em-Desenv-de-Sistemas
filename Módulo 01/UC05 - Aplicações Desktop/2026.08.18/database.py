import json
import os # mexer nos arquivos do windows

ARQUIVO = "2026.08.18/contatos.json"


def carregar_contatos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as contatos:
        return json.load(contatos)


def salvar_contatos(lista_contatos):
    pasta = os.path.dirname(ARQUIVO)

    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta) # criar a pasta json se ela n existir

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista_contatos, arquivo, indent=4, ensure_ascii=False)
        # indent=4 (dar espaços para ficar organizado)
        # ensure_ascii=False (mostrar os acentos, junto com o utf-8)


def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append(novo_contato)
    salvar_contatos(contatos)


def atualizar_contato(indice, nome, telefone, email):
    pass


def excluir_contato(indice):
    pass