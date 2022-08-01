from sqlalchemy import true
from libs import *
from src.tools.funcao_val_tipoPes import *
from src.service.template import *
from openpyxl import load_workbook

# teste =cnpj_validate('389.417.574-52')
# print(teste)


def tratativaCliente(bg_tasks: BackgroundTasks):
    info = pd.read_json('dados.json')
    print("Entrando na validação")
    df= pd.DataFrame(info)
    cont=0
    for linha in df['cpf']:
        validCPF=cpf_validate(str(linha))
        validCNPJ=cnpj_validate(str(linha))
        
        if df.loc[cont, 'cpf'] == None:
            df.loc[cont, 'cpf'] = '0'

        if validCPF == True:
            df.loc[cont, 'Validador'] = 'Verdadeiro'

        elif validCNPJ == True:
            df.loc[cont, 'Validador'] = 'Verdadeiro'

        else:
            df.loc[cont, 'Validador'] = 'Falso'
        cont=cont+1

    print('Validação Finalizada')

    #Gerando em um excel
    print('Gerando Excel')
    name = datetime.now().strftime('%Y%m%d%H%M%S')
    nameString = str(name)
    patch = 'src/temp/Validacao_'+nameString+'.xlsx'
    #patch = 'validacao'
    nameFile = 'Validacao_'+nameString+'.xlsx'

    df.to_excel(patch, index=False)
    print('Arquivo convertido em excel')
    df = pd.read_excel(patch)

    bg_tasks.add_task(os.remove, patch)
    return (patch, nameFile)
