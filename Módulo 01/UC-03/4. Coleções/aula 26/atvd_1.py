def calculadora (valor_da_conta): # função void (retorna um vazio, já que ela só é utilizada para mostrar algo)
    gorjeta = valor_da_conta * 0.1
    valor_final = valor_da_conta + gorjeta
    print(f"""-- Cupom dos valores --
    Valor da conta: R$ {valor_da_conta:,.2f}
    Gorjeta: R$ {gorjeta:,.2f}
    
    Valor total: R$ {valor_final:,.2f}""")

conta = float(input("Digite o valor da conta do cliente: "))
calculadora(conta)