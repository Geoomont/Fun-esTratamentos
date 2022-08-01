from libs import *
from itertools import cycle



def cpf_validate(numbers):
    '''Obtém os números do CPF e ignora outros caracteres ('-', '.')'''
    cpf = [int(char) for char in numbers if char.isdigit()]
    # print(cpf)

    '''Verifica se o CPF tem 11 dígitos'''
    if len(cpf) != 11:
        return False

    '''Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    Esses CPFs são considerados inválidos mas todos passam na validação dos dígitos.'''
    if cpf == cpf[::-1]:
        return False

    '''Valida os dois dígitos verificadores'''
    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def cnpj_validate(cnpj: str) -> bool:

    cnpj = [int(char) for char in cnpj if char.isdigit()]
    if len(cnpj) != 14:
        return False

    if cnpj in (c * 14 for c in "1234567890"):
        return False

    for i in range(2, 0, -1):
        cnpj_r = cnpj[::-1]
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])

        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False
    return True

