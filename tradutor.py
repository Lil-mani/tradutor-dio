import tkinter as tk
from tkinter import filedialog, messagebox

# Variável global para armazenar o caminho do arquivo
file_path = None

def carregar_arquivo():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        label_arquivo.config(text=f"Arquivo selecionado: {file_path}")

def traduzir():
    if file_path:
        print("temos um path -> {}".format(file_path))
    else:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado para traduzir. Escolha um arquivo do tipo txt!")

# Configuração da janela principal
window = tk.Tk()
window.title("Tradutor_projeto_dio")
window.geometry("700x500")
window.configure(bg='#333333')

# Label principal
label = tk.Label(window, text="Tradutor de Arquivos", bg='#333333', fg='white', font=("Arial", 20))
label.pack(pady=20)

# Label para mostrar o arquivo selecionado
label_arquivo = tk.Label(window, text="Nenhum arquivo selecionado", bg='#333333', fg='white')
label_arquivo.pack(pady=10)

# Botão para carregar arquivo
botao_carregar = tk.Button(window, text="Carregar Arquivo", command=carregar_arquivo, bg='#555555', fg='white')
botao_carregar.pack(pady=10)

# Botão para traduzir
botao_traduzir = tk.Button(window, text="Traduzir", command=traduzir, bg='#555555', fg='white')
botao_traduzir.pack(pady=10)

window.mainloop()
