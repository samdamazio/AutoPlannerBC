# Processador de Planilhas

Um aplicativo simples para processar arquivos `.csv` e `.xlsx` com uma interface gráfica amigável. O usuário pode selecionar um arquivo, inserir uma etiqueta, e o programa gera uma nova planilha com as modificações especificadas.

## Funcionalidades

- **Interface Gráfica**: Interface de usuário fácil de usar com botões e campos de entrada.
- **Processamento de Arquivos**: Suporte para arquivos `.csv` e `.xlsx`.
- **Etiquetagem Personalizada**: Adiciona uma etiqueta personalizada a cada entrada no arquivo.
- **Gerar Arquivo**: Cria um novo arquivo `.xlsx` com as modificações e salva em um diretório específico.

## Pré-requisitos

- Python 3.8+ instalado no sistema
- Dependências do Python:
  - `tkinter` (geralmente incluído com a instalação do Python)
  - `pandas`
  - `Pillow` (PIL)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script Python principal:
    ```bash
    python main.py
    ```

2. Use a interface para selecionar um arquivo `.csv` ou `.xlsx`, insira uma etiqueta e clique em "Executar" para gerar uma nova planilha.

## Empacotamento para Distribuição

Para criar um executável autônomo para Windows ou macOS, você pode usar o `PyInstaller`:

1. Instale o PyInstaller:
    ```bash
    pip install pyinstaller
    ```

2. Crie o executável:
    ```bash
    pyinstaller --onefile --windowed --add-data "staticfiles/background.png:staticfiles" main.py
    ```

    Isso criará um executável na pasta `dist` que pode ser distribuído aos usuários.

## Notas

- Certifique-se de que todos os arquivos necessários (como `background.png`) estejam incluídos no mesmo diretório ou especificados corretamente nos comandos do `PyInstaller`.
- Teste o executável em diferentes sistemas operacionais para garantir a compatibilidade.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor

- [Seu Nome](https://github.com/seu_usuario)
