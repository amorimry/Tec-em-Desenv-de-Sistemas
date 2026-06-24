# atributos são variáveis internas do objeto que definem seus comportamentos

# características de um objeto

# os atributos são definidos dentro do método construtor __init__

class Pessoa:

    ano_atual = 2026 # esse valor vai ser o mesmo para todos os objetos dessa classe

    def __init__(self, nome, idade, cpf):
        self.nome = nome # público
        self._idade = idade # protegido
        self.__cpf = cpf # privado

# aqui a classe Pessoa possui 4 atributos: nome, salário, idade e cargo

# == VISIBILIDADE DO ATRIBUTO ==
    
# 'nome' é um atributo público, podendo ser acessado diretamente fora da classe e alterado

# 'idade' é um atributo protegido por conveção, pois vem com um _ após o self
        # aqui mostra que o atributo 'idade' deve ser acessado apenas pela própria classe e por suas classes filhas
        # um _ é apenas uma convenção, ele indica para outros programadores que o atributo não deveria ser acessado diretamente fora da classe, mas o Python não impede que você acesse e altere esse atributo fora da classe

# 'cpf' é um atributo privado, pois vem com dois _ após o self
        # isso mostra que o atributo 'cpf' só pode ser acessado ou alterado dentro da própria classe

# == LOCALIDADE DO ATRIBUTO ==

# atributos de instância (aqueles que pertencem a um objeto especifico):
    # self.nome
    # self.salario
    # self.idade
    # self.cargo

# atributos de classe (pertence a classe como um todo):
    # ano_atual

    def apresentar_pessoa(self):
        print(f"""
-- DADOS DA PESSOA --
              
        Nome: {self.nome}
        Idade: {self._idade} anos
        CPF: {self.__cpf}
""")

if __name__ == "__main__":

# a criação de um objeto é chamado de instanciar uma classe

    pessoa1 = Pessoa("Paulo", 21, "02145632554")

    pessoa1.apresentar_pessoa()

    pessoa1.nome = "Marcos"
    pessoa1._idade = 22
    pessoa1.cpf = "11111111111111"

    pessoa1.apresentar_pessoa()