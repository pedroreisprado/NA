import tkinter as tk
from tkinter import simpledialog

def getCondominio():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    
    # Exibir a janela de diálogo
    condominio = simpledialog.askstring("Condominio", "Digite o condominio:")
    
    # Verificar se o usuário preencheu o campo e clicou em OK
    if condominio is not None:
        print("Condominio digitado:", condominio)
        # O código aqui será executado somente se o usuário preencher o campo e clicar em OK

    return condominio

def inputBalancete():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    
    # Exibir a janela de diálogo
    balancete = simpledialog.askstring("Balancete", "Digite o balancete:")
    
    # Verificar se o usuário preencheu o campo e clicou em OK
    if balancete is not None:
        print("Balancete digitado:", balancete)
        # O código aqui será executado somente se o usuário preencher o campo e clicar em OK

    return balancete



def getOperacao():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    
    # Exibir a janela de diálogo
    operacao = simpledialog.askstring("Operacao", "1 - IQ, 2 - PP")
    
    # Verificar se o usuário preencheu o campo e clicou em OK
    if operacao is not None:
        print("Condominio digitado:", operacao)
        # O código aqui será executado somente se o usuário preencher o campo e clicar em OK

    operacao = str(operacao)
    if operacao == '1':
        operacao = 'Inquilino'
        return operacao
    
    operacao = 'Proprietario'
    return operacao