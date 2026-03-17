# Bibliotecas que rodam o scheduler em 2° plano
import threading
import time
from spotify import get_kpop_charts
from database import save_tracks

# Função que atualiza os charts em loop infinito
def update_charts():
    while True:
        try:
            print("Atualizando charts...")
            tracks = get_kpop_charts()
            save_tracks(tracks)
            print(f"{len(tracks)} músicas salvas com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar: {e}")

        # Atualiza a cada 1 hora
        time.sleep(3600)

# Inicia o scheduler em uma thread separada(não bloqueia o servidor)
def start_scheduler():
    thread = threading.Thread(target=update_charts, daemon=True)
    thread.start()