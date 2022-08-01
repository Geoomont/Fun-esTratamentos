
from functools import update_wrapper
from libs import *
from datetime import *
import pandas as pd

'''Formata data tipo 05 de janeiro  2022'''
def formataData(data, mes_str=None, mes_int:str=None):

    '''Se a data houver o mês escrito'''
    if mes_str != None:
        print('Valor mês escrito')
        s = data.replace(mes_str, mes_int)        
        print('Finalizado o replace:', s)

        '''Considera apenas valores numéricos'''
        teste = (int(char) for char in s if char.isdigit())
        date_format = pd.DataFrame(teste)
        date_recived = []
        date_format.apply(lambda x: date_recived.append(x.values))

        '''transfromar valores da lista em uma data'''
        '''pegar apenas os valores do array'''
        date_recived = date_recived[0]

        '''transformar em formato de data'''
        day = str(date_recived[:2])
        month = str(date_recived[2:4])
        year = str(date_recived[4:8])
        date_all = day + '/' + month + '/' + year

        '''retira os espaõsos da stringdate'''
        date_all = date_all.replace('[', '') 
        date_all = date_all.replace(']', '') 
        date_all = date_all.replace(' ', '')
        return date_all

        '''Se a data for em formato de dd/mm/aa or yyyy/mm/dd'''
    else: 
        data = pd.to_datetime(data)
        data_completa = data.strftime('%d/%m/%Y')
        return data_completa
            
'''Irá tranformar a str de mês escrito em número'''
def transform_data(mounth:str):
    data = mounth.upper()
    print('Formatado para Maiúsculo:', data)

    if 'JANEIRO' in data:
        date_return = formataData(data, 'JANEIRO', '01')
        print('data: ' + date_return)
        return date_return

    elif 'FEVEREIRO' in data:
        date_return = formataData(data,'FEVEREIRO', '02')
        print('data: ' + date_return)
        return date_return

    elif 'MARÇO' in data:
        date_return = formataData(data,'MARÇO', '03')
        print('data: ' + date_return)
        return date_return

    elif 'ABRIL' in data:
        date_return = formataData(data,'ABRIL', '04')
        print('data: ' + date_return)
        return date_return

    elif 'MAIO' in data:
        date_return = formataData(data,'MAIO', '05')
        print('data: ' + date_return)
        return date_return

    elif 'JUNHO' in data:
        date_return = formataData(data,'JUNHO', '06')
        print('data: ' + date_return)
        return date_return  

    elif 'JULHO' in data:
        date_return = formataData(data,'JULHO', '07')
        print('data: ' + date_return)
        return date_return                      

    elif 'AGOSTO' in data:
        date_return = formataData(data,'AGOSTO', '08')
        print('data: ' + date_return)
        return date_return 

    elif 'SETEMBRO' in data:
        date_return = formataData(data,'SETEMBRO', '09')
        print('data: ' + date_return)
        return date_return 

    elif 'OUTURBO' in data:
        date_return = formataData(data,'OUTUBRO', '10')
        print('data: ' + date_return)
        return date_return 

    elif 'NOVEMBRO' in data:
        date_return = formataData(data,'NOVEMBRO', '11')
        print('data: ' + date_return)
        return date_return 

    elif 'DEZEMBRO' in data:
        date_return = formataData(data,'DEZEMBRO', '12')
        print('data: ' + date_return)
        return date_return 

    else: 
        date_return = formataData(data)
        print('data: ' + date_return)
        return date_return 
