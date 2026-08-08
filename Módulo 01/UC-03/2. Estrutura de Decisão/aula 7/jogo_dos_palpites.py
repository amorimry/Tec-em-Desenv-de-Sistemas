print ("== Jogo do Palpite ==")

import random
numero_secreto = random.randint(0,10)

print ()

palpite = (int(input("Digite um número secreto entre 0 e 10: ")))
if palpite == numero_secreto:
    print ("Parabéns você acertou!")
else:
    print ("Você errou, tente mais 2 vezes.")
    if palpite < numero_secreto and palpite >= 0:
        print ("Dica: O número que você escolheu é menor que o número secreto.")
    elif palpite > numero_secreto and palpite <=10:
        print ("Dica: O número que você escolheu é maior que o número secreto.")
    else:
        print ("Digite um número válido, tente mais duas vezes.")

    print ()

    palpite = (int(input("Digite novamente um número secreto entre 0 e 10: ")))
    if palpite == numero_secreto:
        print ("Parabéns você acertou!")
    else:
        print ("Você errou, tente mais 2 vezes.")
        if palpite < numero_secreto and palpite >= 0:
            print ("Dica: O número que você escolheu é menor que o número secreto.")
        elif palpite > numero_secreto and palpite <=10:
            print ("Dica: O número que você escolheu é maior que o número secreto.")
        else:
            print ("Digite um número válido, tente mais duas vezes.")

        print ()
        
        palpite = (int(input("Digite um número secreto entre 0 e 10: ")))
        if palpite == numero_secreto:
            print ("Parabéns você acertou!")
        else:
            print ("Não foi dessa vez.")

print (f"O número secreto era: {numero_secreto}")