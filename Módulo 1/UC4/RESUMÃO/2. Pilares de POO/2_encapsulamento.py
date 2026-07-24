# o encapsulamento serve para proteger dados de uma classe e controlar como esses dados podem ser acessados ou alterados

# proteger os atributos de uma classe
    # proteção de dados

# em vez de alterar um atributo diretamente, você cria métodos para poder controlar essa alteração

# é feito usando métodos e variáveis privadas, que não pode ser acessada diretamente fora da classe

#  usar atributos privados é a principal ferramenta para aplicar encapsulamento

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome # público
        self._idade = idade # protegido
        self.__cpf = cpf # privado

    def apresentar_pessoa(self):
        print(f"""
-- DADOS DA PESSOA --
              
        Nome: {self.nome}
        Idade: {self._idade} anos
        CPF: {self.__cpf}
""")

if __name__ == "__main__":

    pessoa1 = Pessoa("Paulo", 21, "02145632554")
    print(pessoa1._idade)
    # print(pessoa1.__cpf) ERRO!
    pessoa1.apresentar_pessoa()

    pessoa1.nome = "Felipe"
    pessoa1.__cpf = "11111111111111111111"

    pessoa1.apresentar_pessoa()



# == DICA:
# Pense no botão de volume de uma televisão: O circuito elétrico e a voltagem que passa nos alto-falantes são os atributos privados. Eles ficam escondidos dentro da carcaça da TV. O botão físico (ou o controle remoto) é o método público (o Setter). Se os atributos fossem públicos, seria o equivalente a você abrir a TV com uma chave de fenda e mexer direto nos fios elétricos para aumentar o som. Você poderia tomar um choque ou queimar a TV.Com o encapsulamento, você gira o botão. A TV (classe) recebe o seu pedido, valida se o volume não passou do máximo (segurança) e altera o circuito interno por você.



# == GETTERS E SETTERS ==
# são métodos que servem de "porteiros" de um atributo privado
# getter = pegador
    # serve apenas para ler o valor do atributo, ele não altera nada, apenas pega o valor e te entrega.
# setter = definidor
    # serve para alterar o valor do atributo; a grande vantagem dele é que você pode criar regras de validação antes de aceitar o novo valor
# os métodos podem fazer já todo o trabalho de validar e afins, mas se você precisar apenas ler o saldo sem imprimir um textão de um método? nesse caso vc entra com o getter