# a abstração consiste em focar nos aspectos essenciais de um objeto e ocultar os detalhes complexos de sua implementação
    # exemplo seria um botão de ligar e desligar em um controle remoto

# isso é feito através do módulo nativo do python, o abc (Abstract Base Classes)

from abc import ABC, abstractmethod

# 1. Cria-se a classe abstrata herdando de ABC
class Pagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self, valor):
        pass # Não possui corpo, apenas define o comportamento obrigatório

# 2. As subclasses concretas devem implementar o método abstrato
class CartaoCredito(Pagamento):
    
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R$ {valor} via Cartão de Crédito.")

class Boleto(Pagamento):
    
    def processar_pagamento(self, valor):
        print(f"Gerando código de barras para pagamento de R$ {valor} via Boleto.")

# Tentativa de instanciar a classe abstrata (gera erro)
# pagamento = Pagamento() -> TypeError

# Uso correto (instanciando a subclasse)
pagamento1 = CartaoCredito()
pagamento1.processar_pagamento(150.00)

pagamento2 = Boleto()
pagamento2.processar_pagamento(150.00)

