import tkinter as tk
import requests
import os
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
        # Remove duplicação de extensão .txt, se houver
        if file_path.endswith(".txt.txt"):
            file_path = file_path[:-4]  # Remove os últimos 4 caracteres (.txt)
        label_arquivo.config(text=f"Arquivo selecionado: {file_path}")

def traduzir():
    if file_path:
        print("Temos um path -> {}".format(file_path))

        subscription_key = "f886c1557d2740ad9a22803188db360a"  # Insira sua chave de assinatura
        endpoint = "https://api.cognitive.microsofttranslator.com/"  # Insira seu endpoint da API
        location = "westus2"  # Insira a localização da API
        target_language = "pt-br"  # Idioma de destino

        # Função de tradução usando a API
        def translator_text(text, target_language="pt-br"):
            path = '/translate'
            constructed_url = endpoint + path 
            headers = {
                'Ocp-Apim-Subscription-Key': subscription_key,
                'Ocp-Apim-Subscription-Region': location,
                'Content-type': 'application/json',
                'X-ClientTraceId': str(os.urandom(16))
            }
            body = [{'text': text}]
            params = {
                'api-version': '3.0',
                'from': 'en',
                'to': target_language
            }
            request = requests.post(constructed_url, params=params, headers=headers, json=body)
            response = request.json()
            return response[0]["translations"][0]["text"]

        # Lê o conteúdo do arquivo .txt original
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Traduz cada linha do arquivo
        translated_lines = [translator_text(line, target_language) for line in lines]

        # Define o caminho para salvar o arquivo traduzido
        path_translated = file_path.replace(".txt", f"_{target_language}.txt")
        with open(path_translated, 'w', encoding='utf-8') as file:
            file.writelines("%s\n" % line for line in translated_lines)

        messagebox.showinfo("Sucesso", f"Arquivo traduzido salvo como: {path_translated}")
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
