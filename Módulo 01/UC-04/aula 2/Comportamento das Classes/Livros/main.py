from classLivro import Livro

livro1 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899)
livro2 = Livro("1984", "George Orwell", "Ficção Distópica", 1949)
livro3 = Livro("O Alquimista", "Paulo Coelho", "Ficção", 1988)

print(f"""
    --- Livros ---
Livro: {livro1.nome}
Autor: {livro1.autor}
Gênero: {livro1.genero}
Ano: {livro1.ano}

Livro: {livro2.nome}
Autor: {livro2.autor}
Gênero: {livro2.genero}
Ano: {livro2.ano}

Livro: {livro3.nome}
Autor: {livro3.autor}
Gênero: {livro3.genero}
Ano: {livro3.ano}
""")