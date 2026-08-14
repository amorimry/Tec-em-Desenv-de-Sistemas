from classLivro import Livro # construtor

livro1 = Livro("Senhor do Anéis", "Tolkien", "Fantasia")

# livro1.mostrar_informacoes()

livro1.titulo = "Silmarillion" # método ERRADO, pois esse tipo de manipulação não faz nenhum tipo de verificação, o correto é usar uma função para poder decidir se pode trocar ou não

livro1.mostrar_informacoes()