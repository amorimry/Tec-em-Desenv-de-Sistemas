# Cire um programa de que recebe uma palavra. Informe se a palavra começa com vogal ou consoante.
palavra = "abacate"
if palavra[0] == "a" or palavra[0] == "e" or palavra[0] == "i" or palavra[0] == "o" or palavra[0] == "u":
    print("Começa com vogal.")
else:
    print("Começa com consoante.")

palavra = "laranja"
if palavra[0] in "aeiouAEIOU": #aqui é usado tipo uma lista de coisas, usando o in: um elemento está dentro de um conjunto/coleção
    print("Começa com vogal.")
else:
    print("Começa com consoante.")

palavra = "abacaxi"
if palavra[0].lower() in "aeiou":
    print("Começa com vogal.")
else:
    print("Começa com consoante.")