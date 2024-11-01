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
        label_arquivo.config(text=f"Arquivo selecionado: {file_path}")

def traduzir():
    if file_path:
        print("Temos um path -> {}".format(file_path))

        subscription_key = ""  # Insira sua chave de assinatura
        endpoint = "https://api.cognitive.microsofttranslator.com/"  # Insira seu endpoint da API
        location = "westus2"  # Insira a localização da API
        target_lang = "pt-br"  # Idioma de destino

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

        full_translated_text = []

        # Ler o conteúdo do arquivo e traduzir cada linha
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for paragraph in file:
                    translated_text = translator_text(paragraph.strip(), target_lang)
                    full_translated_text.append(translated_text)

            # Exibir o texto traduzido (para teste)
            for line in full_translated_text:
                print(line)

            # Salvar o texto traduzido em um novo arquivo
            translated_file_path = file_path.replace(".txt", "_translated.txt")
            with open(translated_file_path, 'w', encoding='utf-8') as translated_file:
                for line in full_translated_text:
                    translated_file.write(line + "\n")

            print(f"O texto traduzido foi salvo em {translated_file_path}")
            messagebox.showinfo("Sucesso", f"O texto traduzido foi salvo em {translated_file_path}")
        
        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")
            messagebox.showerror("Erro", f"Erro ao processar o arquivo: {e}")

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
