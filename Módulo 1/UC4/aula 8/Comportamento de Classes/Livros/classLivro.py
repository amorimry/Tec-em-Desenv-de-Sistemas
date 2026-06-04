class Livro():
    def __init__(self, nome, autor, genero, ano):
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.ano = ano

    def exibir_livro(self):
        print(f"""{"-"*40}

    Título: {self.nome}
    Autor: {self.autor}
    Gênero: {self.genero}
    Ano de lançamento: {self.ano}
""")