from fastapi import FastAPI
from src.service.dataframe import *
from fastapi.responses import FileResponse
from src.service.template import *

app = FastAPI()
        
@app.get('/ValidadorCPFCNPJ')
def ValidaçãoTipoPessoa(bg_tasks: BackgroundTasks):
    print('Iniciando Aplicação')
    patch, nameFile = tratativaCliente(bg_tasks)
    return formata_excel(patch, nameFile)



