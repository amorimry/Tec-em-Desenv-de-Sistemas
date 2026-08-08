def vericando_nome(var_nome):
    if var_nome == "": # ver se tá vazio ou não
        print("Preencha o campo NOME.")
        op = False
    else:
        op = True

    return op

def verificando_cpf(var_cpf, lista):
    # if var_cpf == "": # ver se tá vazio ou não
    #     print("Preencha o campo CPF.")
    #     op = False
    # else:
    #     op = True

    # if len(var_cpf) == 11: # verificar se tem o tamanho certo de 11 dígitos
        # print("CPF inválido.")
        # op = True
    # else:
    #     print("CPF inválido, digite novamente.")
    #     op = False

    # if not var_cpf.isdigit():# verificar se só é números
    #     print("O CPF deve conter apenas números.")

    if var_cpf == "": # ver se tá vazio ou não
        print("Preencha o campo CPF.")
        op = False
    elif not var_cpf.isdigit(): # verificar se só é números
        print("O CPF deve conter apenas números.")
        op = False
    elif len(var_cpf) != 11: # verificar se tem o tamanho certo de 11 dígitos
        print("CPF com tamanho inválido.")
        op = False
    else:
        op = True
        for dados in lista: # verificar se o cpf já existe
            if dados["cpf"] == var_cpf:
                print("CPF já existente.")
                op = False # existe
            else:
                op = True # não existe

    return op
    

def verificando_salario(var_salario):
    if var_salario == "": # ver se tá vazio ou não
        print("Preencha o campo SALÁRIO.")
        op = False
    elif var_salario <= 0: # verificar se é negativo ou 0
        print("Salário inválido.")
        op = False
    else:
        op = True

    return op


def vericando_cargo(var_cargo):
    if var_cargo == "": # ver se tá vazio ou não
        print("Preencha o campo SALÁRIO.")
        op = False
    else:
        op = True

    return op


def listar_funcionarios(var_funcionario):
    for i, funcionario in enumerate(var_funcionario):
        print(f"{i+1} - {funcionario["nome"]} | {funcionario["cpf"]}")

def verif_existe(oq_foi_digitado, oq_tem_na_lista, var_lista):
    for dados in var_lista:
        if dados[f"{oq_tem_na_lista}"] == oq_foi_digitado:
            opp = False
            continue
        else:
            opp = True

    return opp
        