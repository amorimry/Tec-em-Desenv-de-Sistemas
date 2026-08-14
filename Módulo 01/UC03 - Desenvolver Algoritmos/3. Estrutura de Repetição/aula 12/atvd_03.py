# 3. Faça um programa que recebe um palpite de um usuário e verifica se esse palpite é igual o número secreto (usar um número aleatório). Permita que o jogador tenha até 3 tentativas.
# Bônus: Faça com o que o jogo encerre assim que o jogador acertar o número secreto.
# Bônus: Faça com que o jogo imprima uma mensagem especial para quando o número de tentativas chegar ao final.

# import random
# num_secreto = random.randit(1,10)
num_secreto = 7
tentativas = 3

print(f"""Você terá {tentativas} tentativas para acertar o número secreto.
Dica: números entre 0 e 10.""")

for i in range(3):
    # num_secreto = random.randit(1,10) --> se isso ficar aqui, a cada tentativa vai ser criado um novo número secreto
    num_digitado = int(input((f"Digite sua {i+1}° tentativa: ")))
    tentativas -= 1 #vai diminuindo o tanto de tentativas que foi estabelecido
    

    if num_digitado != num_secreto:
        print("Você errou.")
        print(f"Você tem {tentativas}")
        if tentativas == 0:
            print("Você gastou todas as tentativas.")
        else: 
            print("Você errou.")

    else:
        print("Você acertou.")
        #quit() --> o jogo encerra assim que o jogador acertar mas o PROBLEMA é que o código todo encerra!
        break #comando usado em repetições, justamente para frear/interromper as repetições e o programa continua normalmente depois do for

print(f"Fim de jogo, o número secreto era {num_secreto}!")