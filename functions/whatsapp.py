import pandas as pd
import time
from PyPDF2 import PdfReader, PdfWriter
import os
import re
import requests
import json

from functions.pandas_scripts import getData

from config import NEW_PATH,WHATS_NOAH_KEY,WHATS_NOAH_TOKEN

def noahSendMsgFile(nome, number,condominio ,unidade):
    number = str(number)
    number = number.replace('.0','')
    unidade = str(unidade)
    nome = str(nome)

    MESSAGE = (f'Olá {nome}, segue boleto referente a taxa condominial do Condomínio {condominio}, unidade {unidade}. Por favor, antes de efetivar o pagamento no internet banking, confirme os seguintes dados: valor, vencimento, beneficiário e pagador, CNPJ do beneficiário e CPF/CNPJ do Pagador. Após confirmações, realize o pagamento até a data de vencimento. Em caso de dúvidas, a N&A Condomínios está a disposição pelos telefones (14) 99115-8661 /(14) 3570-1600. Mensagem automatica, favor não responder.')

    url = "https://2rfpapi.bragimulticanal.com.br/v1/api/external/" + str(WHATS_NOAH_KEY)

    payload = {
        'number': str(number),
        'externalKey': WHATS_NOAH_KEY,
        'body': str(MESSAGE)
    }
    pdf_name = (f'{unidade}.pdf')
    pdf_full_path = (f'{NEW_PATH}\\pdf_apartado\\{pdf_name}')
    
    files = {'media': (pdf_name, open(pdf_full_path, 'rb'), 'application/pdf')}


    headers = {
        'Authorization': 'Bearer ' + str(WHATS_NOAH_TOKEN)
    }

    response = requests.post(url, headers=headers, data=payload, files=files)
    print(f"MENSAGEM ENVIADA: "+ str(response.text) + str(number))

    return response.text

def noahSendMsgText(number, message):
    url = "https://2rfpapi.bragimulticanal.com.br/v1/api/external/" + str(WHATS_NOAH_KEY)

    payload = json.dumps({
        "body": str(message),
        "number": str(number),
        "externalKey": WHATS_NOAH_KEY
     })
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(WHATS_NOAH_TOKEN)
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"MENSAGEM ENVIADA: "+ str(response.text) + str(number))

    return response.text


def sendMsg(operacao):
    lista = os.listdir(NEW_PATH)

    for file in lista:
        unidade = file.replace('.pdf',"")
        retorno = (getData(unidade,operacao))
        if not retorno:
            continue
        numero = str(retorno[0])
        numero = numero.replace('-','').replace('(','').replace(')','').replace(' ',"")
        nome = str(retorno[1]).split()
        nome = nome[0]
        print(numero)
        print(nome)

