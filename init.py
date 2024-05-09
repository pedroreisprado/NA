import gc
import sys
import time 
import os 
import pyautogui
import pyperclip
from threading import Thread
from pynput.mouse import Controller,Button

from functions.pandas_scripts import separar_paginas,getData,deletePDF,CreateSheet,insertInfo
from functions.getBalancete import inputBalancete,getOperacao,getCondominio
from functions.initConfig import initSplash
from functions.logger import logger
from functions.whatsapp import noahSendMsgFile
from navigator import getBoletos
from config import DOWNLOAD_PATH, NEW_PATH



os.chdir(NEW_PATH)

##--- INIT PROCESS
if __name__ == "__main__":
    app, message_window = initSplash()
    def run_main_program():
        gc.collect()
        mouse = Controller()
        logger(f'Processo Iniciado')
        time.sleep(5)
        logger(f'Aguardando usuário insererir o Balancete')
        balancete = inputBalancete()
        if balancete is None or balancete == "":
            logger(f'Balancete inserido errado ou vazio')
            return
        operacao = getOperacao()
        print(operacao)
        if operacao is None or operacao == "":
            logger(f'Operação selecionada não é valida')
            return
        logger(f'Pedindo condominio que está sendo usado')
        condominio = getCondominio()
        if condominio is None or condominio == "":
            logger(f'Condominio digitado não é valido')
            return
        logger(f'Iniciando coleta de boletos')
        boletos = getBoletos(balancete)
        if not boletos:
            logger(f'Falha ao coletar boletos')
            return
        logger(f'Separando cada unidade em PDF')
        files = separar_paginas(f'{boletos}')
        logger(f'Criando a aba no arquivo de Devolutivas')
        criando_sheet = CreateSheet(condominio,operacao)
        if not criando_sheet:
            logger(f'Erro ao criar as devolutivas, processo vai seguir sem salvar informações')
        logger(f'Para cada cliente, executar o fluxo de coleta de dados e envio do WPP')
        for file in files:
            unidade = str(file.replace('.pdf',''))
            info_cliente = getData(unidade,operacao)
            telefone = str(info_cliente[0])
            nome = str(info_cliente[1]).split()
            telefone = telefone.replace('-','').replace('(','').replace(')','').replace(' ',"")
            nome = nome[0]
            envio_msg = noahSendMsgFile(nome,telefone,condominio,unidade)
            insert_infos = insertInfo(nome,unidade,condominio,telefone,operacao)
            if not insert_infos:
                logger(f'Não foi possivel salvar informações no arquivos de devolutiva, seguindo para o proximo')
                continue

        logger(f'Deletando os PDFs após o envio')
        final = deletePDF()

        logger(f'Final do fluxo')   
main_thread = Thread(target=run_main_program)
main_thread.start()

sys.exit(app.exec_())       