from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

def get_youtube_client():
    api_key = os.getenv("YOUTUBE_API_KEY")
    return build("youtube", "v3", developerKey=api_key)

def get_mv_id(song_name, artist):
    youtube = get_youtube_client()

    query = f"{artist} {song_name} MV official"

    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1,
        type="video"
    )

    response = request.execute()

    if response["items"]:
        return response["items"][0]["id"]["videoId"]

    return None