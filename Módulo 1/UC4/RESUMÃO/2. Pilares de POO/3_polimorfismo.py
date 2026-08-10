# a palavra "polimorfismo" significa "muitas formas" e, em programação, refere-se a métodos/funções/operadores com o mesmo nome que podem ser executados em vários objetos ou classes
    # len() é um exemplo de polimorfismo

# é a capacidade de diferentes classes responderem à uma mesma chamada de um método ou função, mas sendo específico para cada objeto

# permite aos programadores usar uma única interface com diferentes formas subjacentes

class Animal(): # classe pai
    def emitir_som(self):
        print("O animal emite um som.")


class Cachorro(Animal):
    def emitir_som(self):
        print("Cachorro: Au au!")
    # aqui ocorreu uma sobrescrita de método, que é quando a classe filha cria um método com o mesmo nome de um método da classe pai
    # o método na classe filha deve ter o mesmo nome e a mesma quantidade/tipo de parâmetros do método na classe pai
    # a classe filha substitui o comportamento padrão herdado para atender às suas próprias necessidades
    # 

class Gato(Animal):
    def emitir_som(self):
        print("Gato: Miau!")
    # a classe filha apenas escolhe uma versão mais específica para ela do método, mas outras filhas ainda podem usar a versão do pai

class Vaca(Animal):
    def emitir_som(self):
        print("Vaca: Muuu!")

class Peixe(Animal):
    def emitir_som(self):
        return super().emitir_som()
    # o método da classe pai serve como uma "rede de segurança"; se uma classe filha não precisar de um comportamento especial, ela usa o padrão do pai; o método do pai só é "inutilizado" para a filha que escolheu sobrescrevê-lo
    

if __name__ == "__main__":

    cachorro = Cachorro()
    gato = Gato()
    vaca = Vaca()

    cachorro.emitir_som()
    gato.emitir_som()
    vaca.emitir_som()

    #---------------------------------

    animais = [
    Cachorro(),
    Gato(),
    Vaca(),
    Peixe()
]
    # polimordismo em ação
    for animal in animais:
        animal.emitir_som() # para cada classe de animal da vez, roda o método de emitir_som de cada uma das classes

    #---------------------------------

