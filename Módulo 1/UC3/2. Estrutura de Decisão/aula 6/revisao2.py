# 2. Crie um programa que pede um login e senha. Se o login informado for 'admin' e a senha for 'pass' mostre na tela "Acesso Concedido: {True/False}"

print ("=== Login do Usuário ===")
login = input ("Insira seu login: ")
senha = str(input("Insira sua senha: "))

acesso = login == "admin" and senha == "pass"

print (f"Acesso concedido: {acesso}")