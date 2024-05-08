import pandas as pd
from PyPDF2 import PdfReader,PdfWriter
import os 
import re
from config import SAVE_PATH,NEW_PATH,DADOS_PATH


def separar_paginas(pdf_path):
    pdf_path = (f'{SAVE_PATH}\\{pdf_path}.pdf')
    # Crie um diretório para armazenar os PDFs separados

    output_dir = (f'{NEW_PATH}\\pdf_apartado')
    os.makedirs(output_dir, exist_ok=True)

    with open(pdf_path, "rb") as file:
        pdf_reader = PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # Para cada página, crie um PDF separado
        for page_number in range(total_pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader._get_page(page_number))
            page_text = pdf_reader._get_page(page_number).extract_text()

            # Buscar pelo texto "unidade"
            index_unidade = page_text.find("Unidade: ")
            if index_unidade != -1:
                # Pegar os dois caracteres após "unidade"
                codigo_unidade = page_text[index_unidade + len("Unidade: "): index_unidade + len("Unidade: ") + 2]
                print(f"Código da unidade na página {page_number + 1}: {codigo_unidade}")

            # Salvar a página atual como um PDF separado
            output_path = os.path.join(output_dir, f"{codigo_unidade}.pdf")
            with open(output_path, "wb") as output_file:
                pdf_writer.write(output_file)


    files = os.listdir(f'{NEW_PATH}\\pdf_apartado')
    return files

def getData(unidade,operacao):
    unidade = str(unidade)
    df = pd.read_excel(f'{DADOS_PATH}//unidpl01.xls', skiprows= 8)
    # Encontre o índice da linha onde o valor '10' está na coluna 0
    indice = df[df.iloc[:, 0] == unidade].index[0]

    # Encontre o valor na coluna 8 na mesma linha do valor '10'
    if operacao == "Inquilino":
        valor_na_coluna_8 = df.iloc[indice + 3, 6]
        nome = df.iloc[indice + 3, 1]

        if 'Unidade Vazia' in nome:
            valor_na_coluna_8 = df.iloc[indice + 2, 6]
            nome = df.iloc[indice + 2, 1]

        if pd.isna(valor_na_coluna_8):
            print('Não foi possivel localizar o WPP do IQ, passando para o WPP do PP')
            valor_na_coluna_8 = df.iloc[indice + 2, 6]
            nome = df.iloc[indice + 2, 1]
            if pd.isna(valor_na_coluna_8):
                return False
        return [valor_na_coluna_8,nome]

    valor_na_coluna_8 = df.iloc[indice + 2, 6]
    nome = df.iloc[indice + 2, 1]

    if pd.isna(valor_na_coluna_8):
        return False
    return [valor_na_coluna_8,nome]

def deletePDF():
    path = (f'{NEW_PATH}\\pdf_apartado')
    pdfs = os.listdir(path)
    print(pdfs)
    for file in pdfs:
        caminho_arquivo = os.path.join(path, file)
        os.remove(caminho_arquivo)
    return True
