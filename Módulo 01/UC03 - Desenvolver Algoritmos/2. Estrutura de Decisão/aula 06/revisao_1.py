# 1. Crie um programa que pergunta se uma pessoa tem reserva para o restaurante. Verifique se a resposta foi especificamente "Sim" e imprima o resultado da verificação:
#Ex: "Entrada Permitida: {True/False}"

print ("=== Reservas do Restaurante XYZ ===")
reserva = input("Cliente tem reserva? (Sim/Não): ")
verif_reserva = reserva == "Sim"
# um = você guarda informação e == você compara informações
# se quiser colocar uma resposta Sim ou sim é só usar o or
#   verif_reserva = reserva == "Sim" or reserva == "sim"
print (f"Entrada permitida: {verif_reserva}")