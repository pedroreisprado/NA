import pyautogui
import pyperclip
import time
import shutil
import os
import random
import string

from functions.logger import logger
from config import DOWNLOAD_PATH,SAVE_PATH

def getBoletos(balancete):
    balancete = str(balancete.replace('/',''))
    print(f'{balancete}')
    time.sleep(20)
    #-- Clica no botão para selecionar todos os boletos
    pyautogui.click(374,729)
    time.sleep(5)
    #-- Preciona tab para ir para a opção de 'Visualizar'
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('space')
    time.sleep(2)
    pyautogui.write(balancete)
    time.sleep(2)
    pyautogui.hotkey('alt',"o")
    time.sleep(5)
    pyautogui.hotkey('alt',"y")
    time.sleep(30)
    pyautogui.hotkey('alt',"c")
    time.sleep(15)
    pyautogui.click(85,218)
    time.sleep(0.5)
    for _ in range(3):
        time.sleep(0.5)
        pyautogui.press('enter')
    time.sleep(3)
    caracteres = string.ascii_letters + string.digits  # Letras e números
    nome_arquivo=  ''.join(random.choice(caracteres) for _ in range(10))
    nome_arquivo = nome_arquivo.lower()
    time.sleep(4)
    pyautogui.write(nome_arquivo)
    logger(f'{nome_arquivo}')
    pyautogui.click(236,236)
    time.sleep(2)
    pyautogui.press('w')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('alt','s')
    time.sleep(1)
    pyautogui.hotkey('alt','y')
    time.sleep(10)
    pyautogui.hotkey('ctrl','w')
    downloaded_files = os.listdir(DOWNLOAD_PATH)
    for file in downloaded_files:
        if nome_arquivo in file:
            # Mova o arquivo para o local desejado
            source_file = os.path.join(DOWNLOAD_PATH, file)
            shutil.move(source_file, SAVE_PATH)
            logger(f"Arquivo movido para {SAVE_PATH}")
            return file
    return nome_arquivo