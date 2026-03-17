# Bibliotecas conectadas com a API Youtube Data
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

# Cria e retorna o cliente autenticado do YouTube
def get_youtube_client():
    api_key = os.getenv("YOUTUBE_API_KEY")
    return build("youtube", "v3", developerKey=api_key)

# Busca o ID do M/V oficial no YouTube pelo nome da música e do artista
def get_mv_id(song_name, artist):
    youtube = get_youtube_client()

    # Monta a query de busca
    query = f"{artist} {song_name} MV official"

    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1,
        type="video"
    )

    response = request.execute()

    # Retorna o ID do primeiro vídeo encontrado
    if response["items"]:
        return response["items"][0]["id"]["videoId"]
    return None