import json
import os # mexer nos arquivos do windows

ARQUIVO = "2026.08.19/contatos.json"


def carregar_contatos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as contatos:
        return json.load(contatos)


def salvar_contatos(lista_contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista_contatos, arquivo, indent=4, ensure_ascii=False)


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
    contatos = carregar_contatos()
 
    contatos[indice] = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
 
    salvar_contatos(contatos)


def excluir_contato(indice):
    pass