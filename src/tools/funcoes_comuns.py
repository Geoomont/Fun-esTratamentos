from libs import *

def tratamento_data(data):
    datastr=str(data)
    print(datastr)
    ano = datastr[6:11]
    print(ano)
    dia = '01'
    mes = datastr[3:5]
    dia = datastr[0:2]
    data_completa = f'{dia}.{mes}.{ano}'
    return data_completa

def tratamento_data_pivo(data):
    dia = data[8:10]
    mes = data[5:7]
    ano = data[2:4]
    data_completa = f'{mes}/{ano}'
    return data_completa

def tratamento_pivo(mes,ano):

    data_completa = '0'
    if mes =='01':
        data_completa = f'jan/{ano}'
    if mes =='02':
        data_completa = f'fev/{ano}'
    if mes =='03':
        data_completa = f'mar/{ano}'
    if mes =='04':
        data_completa = f'abr/{ano}'
    if mes =='05':
        data_completa = f'mai/{ano}'
    if mes =='06':
        data_completa = f'jun/{ano}'
    if mes =='07':
        data_completa = f'jul/{ano}'
    if mes =='08':
        data_completa = f'ago/{ano}'
    if mes =='09':
        data_completa = f'set/{ano}'
    if mes =='10':
        data_completa = f'out/{ano}'
    if mes =='11':
        data_completa = f'nov/{ano}'
    if mes =='12':
        data_completa = f'dez/{ano}'

    return data_completa