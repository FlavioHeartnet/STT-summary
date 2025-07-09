# Audio Transcription and Summarization Pipeline

Este projeto é uma aplicação em Python que automatiza o processo de transcrição e resumo de arquivos de áudio. A aplicação utiliza o modelo **Whisper** da OpenAI para uma conversão de fala para texto (STT) de alta precisão e, em seguida, emprega a **API Gemini** do Google para gerar um resumo conciso e focado nos tópicos mais importantes do texto transcrito.

O código foi desenvolvido seguindo os princípios **SOLID** de design de software, resultando em uma arquitetura limpa, modular e extensível.

## ✨ Features

- **Transcrição de Áudio para Texto**: Converte arquivos de áudio nos formatos `.mp3` e `.wav` em texto.
- **Resumo Inteligente**: Gera um resumo dos pontos-chave do texto transcrito usando um LLM (Gemini).
- **Conversão Automática**: Converte automaticamente arquivos `.wav` para o formato `.mp3` antes do processamento para otimizar a compatibilidade.
- **Saída Dupla**: Gera dois arquivos de texto como saída: um com a transcrição completa e outro com o resumo.
- **Arquitetura Robusta**: Escrito em Python com orientação a objetos e uma estrutura que segue os princípios SOLID.

## 🏛️ Arquitetura

O projeto é dividido em componentes com responsabilidades únicas, promovendo a manutenibilidade e a escalabilidade:

- **`AudioConverter`**: Interface e implementação para conversão de formatos de áudio.
- **`Transcriber`**: Interface e implementação para o serviço de transcrição (Whisper).
- **`Summarizer`**: Interface e implementação para o serviço de resumo (Gemini).
- **`FileWriter`**: Classe utilitária para escrita de arquivos.
- **`AudioProcessingPipeline`**: Classe orquestradora que gerencia o fluxo de trabalho, aplicando o princípio de Inversão de Dependência.

## ⚙️ Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes softwares instalados em seu sistema:

1.  **Python** (versão 3.9 ou superior).
2.  **FFmpeg**: Uma ferramenta essencial para o processamento de áudio.
    -   **macOS (via Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    -   **Debian/Ubuntu:**
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    -   **Windows:**
        Faça o download dos binários no [site oficial do FFmpeg](https://ffmpeg.org/download.html), descompacte-os e adicione a pasta `bin` ao PATH do seu sistema.

## 🚀 Instalação e Configuração

Siga estes passos para configurar o ambiente do projeto:

**1. Clone o Repositório**

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd audio_processing_app
```

**2. Crie e Ative um Ambiente Virtual**

É uma boa prática isolar as dependências do projeto.

- **Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

**3. Instale as Dependências**

O arquivo `requirements.txt` contém todos os pacotes Python necessários. Ele já inclui a correção (`pyaudioop`) para o problema de compatibilidade com o Python 3.13.

```bash
pip install -r requirements.txt
```

**Conteúdo do `requirements.txt`:**
```txt
openai-whisper
google-generativeai
python-dotenv
pydub
audioop-lts
```

**4. Configure sua Chave de API**

Você precisará de uma chave de API do Google Gemini.

- Obtenha sua chave no [**Google AI Studio**](https://aistudio.google.com/app/apikey).
- Crie um arquivo chamado `.env` na raiz do projeto (`audio_processing_app/`).
- Adicione sua chave de API ao arquivo da seguinte forma:

  ```ini
  # .env
  GEMINI_API_KEY="SUA_CHAVE_DE_API_DO_GEMINI_AQUI"
  ```

## ▶️ Como Usar

Execute o script `main.py` a partir da linha de comando, passando o caminho para o arquivo de áudio como argumento.

**Exemplo com um arquivo `.wav`:**
```bash
python main.py /caminho/para/seu/audio.wav
```

**Exemplo com um arquivo `.mp3`:**
```bash
python main.py audios/reuniao.mp3
```

**Usando um modelo Whisper diferente (mais preciso, porém mais lento):**
Por padrão, o modelo `base` é utilizado. Você pode especificar outro, como `small`, `medium` ou `large`.

```bash
python main.py seu_audio.wav --model small
```

## 📄 Saída (Output)

Após a execução bem-sucedida, dois novos arquivos serão criados no mesmo diretório do arquivo de áudio original:

1.  **`nome_do_audio_transcription.txt`**: Contém a transcrição completa do áudio.
2.  **`nome_do_audio_summary.txt`**: Contém o resumo dos tópicos principais gerado pela API Gemini.

