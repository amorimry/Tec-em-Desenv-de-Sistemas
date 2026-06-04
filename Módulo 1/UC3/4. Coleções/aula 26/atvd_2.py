def calcular (valor_conta, porcentagem_gorjeta): # aq te devolte algo, diferente de executar alguma ação; usar verbos e nomes no infinitivo para as funções
    valor_gorjeta = valor_conta * (porcentagem_gorjeta/100)
    valor_total = valor_conta + valor_gorjeta

    return valor_total

    # print(f"""-- Nota Fiscal --
    # Valor da conta: R$ {valor_conta:,.2f}
    # Valor da gorgeja (Desconto de {porcentagem_gorjeta}%): R$ {valor_gorjeta:,.2f}
    
    # Valor total: R$ {valor_total:,.2f}""")

conta = float(input("Digite o valor total da conta do cliente: "))
gorjeta = float(input("Digite o valor da porcentagem (%) da gorjeta: "))

total_conta = calcular(conta, gorjeta)

print(f"""-- Nota Fiscal --
Valor da conta: R$ {conta:,.2f}
Porcentagem da gorgeja: {gorjeta:.2f}%
    
Valor total: R$ {total_conta:,.2f}""")



def calcular (valor_conta, porcentagem_gorjeta=10): # defol: se a pessoa não declarar algo fica sendo o valor que ta em defol; se o primeiro tiver um defol e o segundo não, o código fica errado, ou é só o segundo ou os dois
    valor_gorjeta = valor_conta * (porcentagem_gorjeta/100)
    valor_total = valor_conta + valor_gorjeta

    return valor_total

conta = float(input("Digite o valor total da conta do cliente: "))
gorjeta = float(input("Digite o valor da porcentagem (%) da gorjeta: "))

total_conta = calcular(conta, gorjeta)

print(f"""-- Nota Fiscal --
Valor da conta: R$ {conta:,.2f}
Porcentagem da gorgeja: {gorjeta:.2f}%
    
Valor total: R$ {total_conta:,.2f}""")



def calcular (valor_conta, porcentagem_gorjeta=10):
    valor_gorjeta = valor_conta * (porcentagem_gorjeta/100)
    valor_total = valor_conta + valor_gorjeta

    return valor_total

print(calcular(porcentagem_gorjeta=10, valor_conta=150)) # caso não tiver que colocar em ordem