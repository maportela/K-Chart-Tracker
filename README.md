# K-pop Chart Tracker

Uma aplicação web que busca músicas do gênero k-pop em tempo real pela API Spotify Web e exibe os resultados com capa do álbum, artista e um mini player do M/V oficial que toca automaticamente ao passar o mouse no card. Os M/Vs são buscados automaticamente pela API YouTube Data v3.

---

## Prévia

![Prévia](assets/demo.gif)

---

## Funcionalidades
 
- Busca músicas do gênero k-pop em tempo real pela API Spotify Web
- Exibe capa do álbum, nome da música e artista
- Mini player do M/V oficial do YouTube ao passar o mouse no card
- Botão para ativar/desativar o som do M/V
- Histórico dos charts salvo em banco de dados SQLite
- Atualização automática dos dados a cada 1 hora
 
---

## De onde vêm os dados?
 
Os dados do app vêm de duas APIs externas:
 
### Spotify Web API
O app realiza uma busca direta pela palavra `"kpop"` na API Spotify Web, que retorna as músicas mais relevantes para esse termo no momento. Os resultados são então ordenados pelo **índice de popularidade do Spotify**, um valor calculado pela própria plataforma com base no **número de streams recentes** de cada faixa. Ou seja, não é uma playlist específica, e sim o resultado do algoritmo de busca do Spotify em tempo real.
 
### YouTube Data API v3
Para cada música retornada pelo Spotify, o app faz uma busca automática no YouTube com o nome da música e o artista (ex: `"TWICE What is Love? MV official"`), pegando o vídeo mais relevante para exibir no mini player.
 
---

## Tecnologias utilizadas
 
### Linguagens
- Python
- JavaScript
- HTML + CSS
 
### Framework
- **FastAPI** — framework Python para criação da API backend
 
### Bibliotecas Python
| Biblioteca | Função |
|---|---|
| `spotipy` | Conexão com a API Spotify Web |
| `google-api-python-client` | Conexão com a API YouTube Data v3 |
| `python-dotenv` | Leitura das credenciais do arquivo `.env` |
| `uvicorn` | Servidor que executa o FastAPI |
| `sqlite3` | Banco de dados local (já incluso no Python) |
| `threading` + `time` | Scheduler para atualização automática dos dados |
 
### APIs externas
- [Spotify Web API](https://developer.spotify.com/documentation/web-api)
- [YouTube Data API v3](https://developers.google.com/youtube/v3)
 
### Banco de dados
- **SQLite** — armazena o histórico dos charts localmente
 
---

## Estrutura do projeto
 
```
kpop-chart-tracker/
├── assets/
│   ├── demo.gif         # Prévia do site 
├── backend/        
│   ├── database.py      # Configuração e queries do SQLite
│   ├── main.py          # API com FastAPI e endpoints
│   ├── scheduler.py     # Atualização automática a cada 1 hora 
│   ├── spotify.py       # Conexão e busca na API Spotify We
│   └── youtube.py       # Busca de M/Vs na API YouTube Data
├── frontend/
│   ├── index.html       # Estrutura da página       
│   ├── style.css        # Estilo      
│   └── script.js        # Lógica do frontend e mini player        
├── .env                 # Credenciais das APIs (não está no GitHub)                 
├── .gitignore
├── start.bat            # Iniciar o projeto com dois cliques            
└── README.md
```

---

## Como rodar o projeto
 
### Pré-requisitos
- Python 3.10+
- Conta de desenvolvedor no [Spotify](https://developer.spotify.com)
- Chave de API no [Google Cloud Console](https://console.cloud.google.com) com API YouTube Data v3 ativada
 
### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/kpop-chart-tracker.git
cd kpop-chart-tracker
```
 
### 2. Instale as dependências
```bash
pip install fastapi uvicorn spotipy python-dotenv google-api-python-client
```
 
### 3. Configure as credenciais
Crie um arquivo `.env` na pasta raiz com:
```
SPOTIFY_CLIENT_ID=seu_client_id
SPOTIFY_CLIENT_SECRET=seu_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8000/callback
YOUTUBE_API_KEY=sua_chave_aqui
```
 
### 4. Inicie o projeto
 
**Opção 1 — dois cliques:**
Execute o arquivo `start.bat` diretamente pelo explorador de arquivos.
 
**Opção 2 — terminal:**
 
Terminal 1 (backend):
```bash
cd backend
python -m uvicorn main:app --reload
```
 
Terminal 2 (frontend):
```bash
cd frontend
python -m http.server 3000
```
 
### 5. Acesse no navegador
```
http://localhost:3000
```

---
 
## Endpoints da API
 
| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Verifica se a API está rodando |
| GET | `/charts` | Retorna as músicas k-pop em tempo real |
| GET | `/history` | Retorna o último chart salvo no banco |
 
---
 
## Observação
 
- A cota gratuita da YouTube Data API v3 é de **10.000 unidades por dia** e reseta à meia-noite (horário da Califórnia). Caso seja excedida, os M/Vs não carregarão até o reset.
