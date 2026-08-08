# aqui pode ficar sendo guardado as coisas utilitárias
# se não tiver variável global, dá pra colocar aq nessa biblioteca

def coletar_cpf():
    while True:
        novo_cpf = input("Digite seu CPF: ")
        if len(novo_cpf) == 11:
            print("CPF válido.")
            return novo_cpf # ou coloca o break e fora do while lá no final da função vc joga o return
        else:
            print("CPF inválido.")
            continue