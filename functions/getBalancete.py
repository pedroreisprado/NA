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
    
    # Função para obter a opção selecionada
    def obter_opcao():
        print("Opção selecionada:", opcao_var.get())
        root.destroy()  # Fechar a janela após a seleção

    # Criar uma nova janela
    janela = tk.Toplevel(root)
    janela.title("Escolha uma opção")

    # Variável para armazenar a opção selecionada
    opcao_var = tk.StringVar(value="")

    # Criar botões de rádio para as opções
    opcao1 = tk.Radiobutton(janela, text="Proprietário", variable=opcao_var, value="Proprietário")
    opcao1.pack(anchor='w')
    opcao2 = tk.Radiobutton(janela, text="Inquilino", variable=opcao_var, value="Inquilino")
    opcao2.pack(anchor='w')

    # Botão OK para confirmar a seleção
    botao_ok = tk.Button(janela, text="OK", command=obter_opcao)
    botao_ok.pack()

    # Configurar a janela para aparecer em primeiro plano e centralizada
    janela.lift()  # Abrir a janela em primeiro plano
    largura_janela = 200
    altura_janela = 100
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x_pos = largura_tela // 2 - largura_janela // 2
    y_pos = altura_tela // 2 - altura_janela // 2
    janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

    # Exibir a janela
    janela.mainloop()
    return opcao_var.get()
