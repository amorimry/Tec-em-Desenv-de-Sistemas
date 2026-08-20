import json
import os

ARQUIVO = "2026.08.20/contatos.json"


def carregar_contatos():
    if not os.path.exists(ARQUIVO): # Verifica se o arquivo existe usando os.path.exists()
        return [] # Se não existir (primeira vez rodando), retorna uma lista vazia []
    with open(ARQUIVO, "r", encoding="utf-8") as contatos: # Se existir, abre o arquivo em modo de leitura ("r")
        return json.load(contatos) # U o json.load() para transformar o texto do arquivo de volta em uma lista de dicionários Python


def salvar_contatos(lista_contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo: # Abre o arquivo em modo de escrita ("w")
        json.dump(lista_contatos, arquivo, indent=4, ensure_ascii=False) # O json.dump() pega a lista atualizada de contatos do Python e a converte em texto JSON dentro do arquivo
        # O parâmetro indent=4 deixa o arquivo JSON bonito e identado para leitura humana
        # O ensure_ascii=False garante que acentos (como no nome "João") sejam salvos corretamente


def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos() # Essa função chama o carregar_contatos() para pegar a lista atual do arquivo
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    } # Cria um novo dicionário com as chaves "nome", "telefone" e "email"
    contatos.append(novo_contato) # Adiciona esse dicionário no final da lista usando .append()
    salvar_contatos(contatos) # Chama salvar_contatos() para gravar a lista modificada de volta no HD


def atualizar_contato(indice, nome, telefone, email):
    contatos = carregar_contatos() # Carrega a lista atual
 
    contatos[indice] = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    } # Usa o indice (a posição numérica do contato, ex: 0, 1, 2) para substituir diretamente o dicionário antigo pelo novo conjunto de dados
 
    salvar_contatos(contatos) # Salva o arquivo atualizado


def excluir_contato(indice):
    contatos = carregar_contatos() # Carrega a lista atual

    if 0 <= indice < len(contatos):
        contatos.pop(indice) # O .pop() remove o item da lista exatamente naquela posição informada
        salvar_contatos(contatos) # Por fim, salva a lista sem o item removido