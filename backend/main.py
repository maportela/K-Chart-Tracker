# Frameworks e módulos do backend
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from spotify import get_kpop_charts
from database import init_db, save_tracks, get_latest_tracks
from scheduler import start_scheduler

app = FastAPI()

# Permite que o frontend acesse o backend de um endereço diferente (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa o banco de dados e o scheduler ao subir o servidor
init_db()
start_scheduler()

# Verifica se a API está no ar
@app.get("/")
def root():
    return {"message": "KPop Chart Tracker API funcionando!"}

# Busca as músicas no Spotify e salva no banco de dados
@app.get("/charts")
def get_charts():
    tracks = get_kpop_charts()
    save_tracks(tracks)
    return {"tracks": tracks}

# Retorna o último chart salvo no banco de dados
@app.get("/history")
def get_history():
    tracks = get_latest_tracks()
    return {"tracks": tracks}