# Atividade 2: Criando e Usando uma Classe
# • Descrição: Crie uma classe chamada Livro com atributos titulo e autor. Adicione um método chamado detalhes que imprime o título e o autor do livro. Crie um objeto dessa classe e chame o método. Crie o método reputação, no qual fala qual a reputação do livro

class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.notas_de_reputacao = []

    def detalhes(self):
        print(f"""
        -- Detalhes do livro --
    Título da obra: {self.titulo}
    Autor: {self.autor}
""")
        
    # def reputacao(self):
    #     op = int(input("Dê uma nota de 0 a 5 para o livro: "))
    #     if op == 1 or op == 2:
    #         print("A reputação do seu livro é baixa.")
    #     elif op == 3:
    #         print("A reputação do seu livro é mais ou menos.")
    #     elif op == 4 or op == 5:
    #         print("A reputação do seu livro é ótima.")
    #     else:
    #         print("Reputação inválida.")

    def reputacao(self, nota):
        self.notas_de_reputacao.append(nota)
        media_reputacao = sum(self.notas_de_reputacao) / len(self.notas_de_reputacao)
        if media_reputacao >= 4.5 and media_reputacao <= 5:
            return f"Reputação excelente - Média: {media_reputacao}"
        elif media_reputacao >= 3.5 and media_reputacao < 4.5:
            return f"Reputação mais ou menos - Média: {media_reputacao}"
        elif media_reputacao >= 0 and media_reputacao < 3.5:
            return f"Reputação péssima - Média: {media_reputacao}"


if __name__ == "__main__":

    livro1 = Livro("A cabeça do santo", "Socorro Acioli")
    
    livro1.detalhes()
    livro1.reputacao(2)

    print(livro1.reputacao(5))
    print(livro1.reputacao(2))
    print(livro1.reputacao(4))
    print(livro1.reputacao(1))
    print(livro1.reputacao(3.6))
    print(livro1.reputacao(5))
    print(livro1.reputacao(1.3))
    print(livro1.reputacao(3.5))
    print(livro1.reputacao(4.2))