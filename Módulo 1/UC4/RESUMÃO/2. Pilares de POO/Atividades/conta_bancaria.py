class ContaBancaria():
    def __init__(self, titular, saldo):
        self._titular = titular
        self.__saldo = saldo

# GETTER (permite ler o saldo de fora com: conta1.saldo)
    @property
    def saldo(self):
        return self.__saldo
    
# SETTER (permite alterar o saldo de fora com: conta1.saldo = valor)
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("O saldo não pode ser negativo.")
        elif novo_saldo > 20*self.__saldo:
            print("Saldo ultrapassou o valor para altereação.")
        else:
            self.__saldo = novo_saldo
            print("Saldo atualizado.")

    def ver_informacoes(self):
        print(f"""
== INFORMAÇÕES DA CONTA ==

        Titular: {self._titular}
        Saldo: R$ {self.__saldo:,.2f}
""")
        
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para deposito.")

        else:
            self.__saldo += valor
            print(f"Deposito de R$ {valor:,.2f} efetuado com sucesso.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        
        elif valor <= 0:
            print("Valor inválido para saque.")

        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:,.2f} efetuado com sucesso.")

if __name__ == "__main__":

    conta1 = ContaBancaria("Pedro", 2000)

    conta1.ver_informacoes()
    conta1.titula = "Ryan"
        # não funciona porque não existe um atributo chamado titular, o que existe é _titular. aqui foi criado um novo atributo
    conta1._titular = "Ryan"
        # quando você usa um underscore (self._titular), isso é apenas uma convenção; significa: “esse atributo não deveria ser acessado diretamente fora da classe”, mas o Python não impede, por isso conta1._titular = "Ryan" funciona
    conta1.__saldo = 5000000000 # não ocorre alteração pois foi criado um novo atributo, já que o atributo saldo só pode ser acessado para ver por meio do getter e acessado para alterar por meio do setter
    conta1.ver_informacoes()
    conta1.saldo = -500000000 # setter usa-se o = ; ERRO
    conta1.saldo = 100 # altera pois eu chamei o setter para alterar e validar, não estou adicionando nem retirando valores, com deposito ou saque, estou alterando diretamente o saldo da conta da pessoa (mantendo ainda as validações necessárias)
    conta1.ver_informacoes()
    conta1.sacar(50) # método usa-se os ()
    conta1.ver_informacoes()
    conta1.depositar(0)
    conta1.depositar(100)
    conta1.ver_informacoes()
    conta1.sacar(10000)
    conta1.sacar(20)
    conta1.ver_informacoes()
    print(conta1.__saldo) # isso aqui ta puxando as informações de um novo atributo que eu criei, nada a ver com o original
    print(conta1.saldo) # chama o getter para poder me mostrar o valor do atributo real


    # OBS:
        # PERGUNTA:
        # mas se no setter eu coloco def e peço um valor dentro dos parenteses, pq quando eu vou alterar eu uso o = e não faço como se fosse um método? pq os métodos se vc quer um valor a mais vc pede dentro dos parenteses após o self, ai vc puxa o método e depois bota nos parenteses o seu valor a parte

        # RESPOSTA:
        # Isso é justamente a “mágica” do decorador @property em Python. Ele transforma um método em algo que se comporta como um atributo.
        # Normalmente, um método é chamado com parênteses: obj.metodo(valor).
        # Mas quando você usa @property e @atributo.setter, o Python faz um “encapsulamento elegante”:
            # O getter permite acessar como se fosse um atributo: conta1.saldo (sem parênteses).
            # O setter permite atribuir com =: conta1.saldo = 500.
        # Ou seja, você escreve como se fosse um atributo simples, mas por trás o Python está chamando o método que você definiu. Isso é feito para deixar o código mais natural e legível.