# Tradutor de Arquivos de Texto com Interface Gráfica

Este projeto utiliza a API Microsoft Translator para traduzir arquivos de texto de um idioma para outro. Ele permite ao usuário selecionar um arquivo `.txt`, enviar o conteúdo para tradução e salvar o resultado em um novo arquivo traduzido. A interface gráfica é desenvolvida com a biblioteca `tkinter`, tornando o processo de tradução mais acessível e fácil de usar. O projeto possui um notebook com o conteúdo passado na aula do bootcamp!

## Funcionalidades

- **Carregar Arquivo**: O usuário pode selecionar um arquivo de texto (.txt) para tradução.
- **Traduzir Texto**: O texto carregado é enviado para a API Microsoft Translator e traduzido para o idioma de destino (por padrão, o português).
- **Salvar Tradução**: O texto traduzido é salvo em um novo arquivo `.txt`, no mesmo diretório do arquivo original, com o sufixo `_translated` no nome do arquivo.

## Estrutura do Código

### Principais Componentes

- **API Microsoft Translator**: A função `translator_text` faz chamadas HTTP para a API, passando o texto a ser traduzido e o idioma de destino. É necessário fornecer uma `subscription_key`, `endpoint` e `location` associados à API.
  
- **Interface Gráfica (Tkinter)**:
  - `carregar_arquivo`: Abre uma janela para selecionar um arquivo `.txt` e armazena o caminho do arquivo.
  - `traduzir`: Lê o conteúdo do arquivo selecionado, envia-o para tradução, exibe o texto traduzido no terminal (opcional) e salva o resultado em um novo arquivo `.txt`.

## Dependências

- **Bibliotecas Python**:
  - `tkinter`: Para a criação da interface gráfica.
  - `requests`: Para fazer requisições HTTP para a API de tradução da Microsoft.
  - `os`: Para manipular o caminho e criar identificadores únicos de solicitação.

Para instalar as bibliotecas necessárias, execute:
```bash
pip install requests
