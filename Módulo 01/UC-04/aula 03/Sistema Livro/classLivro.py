class Livro():
    def __init__(self, titulo, autor, genero): # aqui, após o self, entra os atributos; informações obrigatórias para serem informadas, sem elas nada vai ser criado
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        # self.ano = 2026 # informação fixa

        # if autor == "Machado de Assis":
        #     self.ano = 1800
        # elif autor == "Tolkien":
        #     self.ano = 1947
        # else:
        #     self.ano = 2026

    def mostrar_informacoes (self):
        print(f"""
INFORMAÇÕES DO LIVRO
              
    Título: {self.titulo}
    Autor: {self.autor}
    Gênero: {self.genero}

""")
        
    def transformar_em_dict(self):
        dict_livro = {
            "Título": self.titulo,
            "Autor": self.autor,
            "Gênero": self.genero
        }
        return dict_livro