# Atividade 1: Criação de uma Classe e Objeto
# • Descrição: Crie uma classe chamada Aluno com atributos nome e matricula. Adicione um método chamado exibir_informacoes que imprime os detalhes do aluno. Crie um objeto dessa classe e chame o método. Crie o método aprovado_reprovado que verifica se o aluno foi ou não aprovado.

class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

# esse método serve para acessas informações do objeto, sem precisar chamar o método para fazer isso, é como se fosse um encurtador de caminho
    def __str__(self):
        return f"O(a) aluno(a) {self.nome} está cadastrado com a matrícula {self.matricula}"

    def exibir_informacoes(self):
        print(f"""
        -- Informações do aluno(a) --
    Nome: {self.nome}
    Matrícula: {self.matricula}
""")
        
    def aprovado_reprovado(self, situação):
        if situação.upper() == "APROVADO":
            print(f"""
    -- O(a) aluno(a) {self.nome} foi aprovado(a)!
""")
        elif situação.upper() == "REPROVADO":
            print(f"""
    -- O(a) aluno(a) {self.nome} foi reprovado(a)...
""")
            
if __name__ == "__main__":

    aluno1 = Aluno("Gabriel", 22355655874)
    aluno2 = Aluno("Fernanda", 54421558)

    aluno1.exibir_informacoes()
    print(aluno2)

    aluno2.aprovado_reprovado("aprovado")