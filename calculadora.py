from tkinter import *
from tkinter import ttk

# Cor de fundo da janela
cor1 = "#ffffff"  # cor em hexadecimal 

# Inicializa a janela principal
janela = Tk()
janela.geometry("318x368")
janela.title("Calculadora")
janela.config(background=cor1)

# Cria um frame para a área do display
janela_P = Frame(janela, bg=cor1)
janela_P.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Rótulo para exibir os números clicados
display = Label(janela_P, text="", font=("Helvetica", 20), bg=cor1, fg="black", anchor='e')
display.pack(expand=True, fill='both')

# Cria um frame para os botões
janela_B = Frame(janela, bg=cor1)
janela_B.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Função para capturar o clique dos botões
def botao_clicado(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = display.cget("text")
            result = eval(expression)  # Avalia a expressão
            display.config(text=str(result))
        except Exception as e:
            display.config(text="Erro")
    elif text == "C":
        display.config(text="")
    else:
        display.config(text=display.cget("text") + text)

# Cria botões numerados de 1 a 9
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
row_val = 1
col_val = 0
for numero in numeros:
    btn = ttk.Button(janela_B, text=numero)
    btn.grid(row=row_val, column=col_val, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", botao_clicado)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

# Cria outros botões (0, +, -, *, /, =, C)
outros_botoes = ['0', '+', '-', '*', '/', '=', 'C']
for i, botao in enumerate(outros_botoes):
    btn = ttk.Button(janela_B, text=botao)
    btn.grid(row=row_val, column=i % 3, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", botao_clicado)
    if i % 3 == 2:
        row_val += 1

# Configuração do redimensionamento da janela
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=3)

# Loop principal da interface gráfica
janela.mainloop()

#FALTA TERMINAR ------------------------------
