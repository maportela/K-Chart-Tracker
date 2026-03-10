import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from youtube import get_mv_id
import os

load_dotenv()

def get_spotify_client():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    return spotipy.Spotify(auth_manager=auth_manager)

def get_kpop_charts():
    sp = get_spotify_client()

    results = sp.search(
        q="kpop",
        type="track",
        limit=10
    )

    tracks = []
    for i, item in enumerate(results["tracks"]["items"]):
        name = item.get("name", "")
        artist = item["artists"][0]["name"] if item.get("artists") else ""

        # Busca o MV no YouTube
        youtube_id = get_mv_id(name, artist)

        track = {
            "position": i + 1,
            "name": name,
            "artist": artist,
            "album": item["album"]["name"] if item.get("album") else "",
            "cover": item["album"]["images"][0]["url"] if item.get("album") and item["album"].get("images") else "",
            "preview_url": item.get("preview_url", None),
            "popularity": item.get("popularity", 0),
            "spotify_url": item.get("external_urls", {}).get("spotify", ""),
            "youtube_id": youtube_id
        }
        tracks.append(track)

    tracks.sort(key=lambda x: x["popularity"], reverse=True)

    for i, track in enumerate(tracks):
        track["position"] = i + 1

    return tracks