# escopo
def e(b): # variáveis aq dentro são locais
    a = b * b
    return a

a = 10 # variavel global

e(a) # 100
e(a) # 100
print(e(a)) # 100