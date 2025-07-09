#Audio Transcription and Summarization Pipeline
Este projeto é uma aplicação em Python que automatiza o processo de transcrição e resumo de arquivos de áudio. A aplicação utiliza o modelo Whisper da OpenAI para uma conversão de fala para texto (STT) de alta precisão e, em seguida, emprega a API Gemini do Google para gerar um resumo conciso e focado nos tópicos mais importantes do texto transcrito.

O código foi desenvolvido seguindo os princípios SOLID de design de software, resultando em uma arquitetura limpa, modular e extensível.

✨ Features
Transcrição de Áudio para Texto: Converte arquivos de áudio nos formatos .mp3 e .wav em texto.

Resumo Inteligente: Gera um resumo dos pontos-chave do texto transcrito usando um LLM (Gemini).

Conversão Automática: Converte automaticamente arquivos .wav para o formato .mp3 antes do processamento para otimizar a compatibilidade.

Saída Dupla: Gera dois arquivos de texto como saída: um com a transcrição completa e outro com o resumo.

Arquitetura Robusta: Escrito em Python com orientação a objetos e uma estrutura que segue os princípios SOLID.

🏛️ Arquitetura
O projeto é dividido em componentes com responsabilidades únicas, promovendo a manutenibilidade e a escalabilidade:

AudioConverter: Interface e implementação para conversão de formatos de áudio.

Transcriber: Interface e implementação para o serviço de transcrição (Whisper).

Summarizer: Interface e implementação para o serviço de resumo (Gemini).

FileWriter: Classe utilitária para escrita de arquivos.

AudioProcessingPipeline: Classe orquestradora que gerencia o fluxo de trabalho, aplicando o princípio de Inversão de Dependência.

⚙️ Pré-requisitos
Antes de começar, certifique-se de que você tem os seguintes softwares instalados em seu sistema:

Python (versão 3.9 ou superior).

FFmpeg: Uma ferramenta essencial para o processamento de áudio.

macOS (via Homebrew):

Bash

brew install ffmpeg
Debian/Ubuntu:

Bash

sudo apt update && sudo apt install ffmpeg
Windows:
Faça o download dos binários no site oficial do FFmpeg, descompacte-os e adicione a pasta bin ao PATH do seu sistema.

🚀 Instalação e Configuração
Siga estes passos para configurar o ambiente do projeto:

1. Clone o Repositório

Bash

git clone <URL_DO_SEU_REPOSITORIO>
cd audio_processing_app
2. Crie e Ative um Ambiente Virtual

É uma boa prática isolar as dependências do projeto.

Linux/macOS:

Bash

python3 -m venv venv
source venv/bin/activate
Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
3. Instale as Dependências

O arquivo requirements.txt contém todos os pacotes Python necessários. Ele já inclui a correção (pyaudioop) para o problema de compatibilidade com o Python 3.13.

Bash

pip install -r requirements.txt
Conteúdo do requirements.txt:

Plaintext

openai-whisper
google-generativeai
python-dotenv
pydub
pyaudioop
4. Configure sua Chave de API

Você precisará de uma chave de API do Google Gemini.

Obtenha sua chave no Google AI Studio.

Crie um arquivo chamado .env na raiz do projeto (audio_processing_app/).

Adicione sua chave de API ao arquivo da seguinte forma:

Ini, TOML

# .env
GEMINI_API_KEY="SUA_CHAVE_DE_API_DO_GEMINI_AQUI"
▶️ Como Usar
Execute o script main.py a partir da linha de comando, passando o caminho para o arquivo de áudio como argumento.

Exemplo com um arquivo .wav:

Bash

python main.py /caminho/para/seu/audio.wav
Exemplo com um arquivo .mp3:

Bash

python main.py audios/reuniao.mp3
Usando um modelo Whisper diferente (mais preciso, porém mais lento):
Por padrão, o modelo base é utilizado. Você pode especificar outro, como small, medium ou large.

Bash

python main.py seu_audio.wav --model small
📄 Saída (Output)
Após a execução bem-sucedida, dois novos arquivos serão criados no mesmo diretório do arquivo de áudio original:

nome_do_audio_transcription.txt: Contém a transcrição completa do áudio.

nome_do_audio_summary.txt: Contém o resumo dos tópicos principais gerado pela API Gemini.

📝 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.