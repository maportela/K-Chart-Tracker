from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from spotify import get_kpop_charts
from database import init_db, save_tracks, get_latest_tracks
from scheduler import start_scheduler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
start_scheduler()

@app.get("/")
def root():
    return {"message": "KPop Chart Tracker API funcionando!"}

@app.get("/charts")
def get_charts():
    tracks = get_kpop_charts()
    save_tracks(tracks)
    return {"tracks": tracks}

@app.get("/history")
def get_history():
    tracks = get_latest_tracks()
    return {"tracks": tracks}