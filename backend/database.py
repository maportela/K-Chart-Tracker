import sqlite3
from datetime import datetime

DB_PATH = "kpop_charts.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position INTEGER,
            name TEXT,
            artist TEXT,
            album TEXT,
            cover TEXT,
            preview_url TEXT,
            popularity INTEGER,
            spotify_url TEXT,
            saved_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_tracks(tracks):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    saved_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for track in tracks:
        cursor.execute("""
            INSERT INTO tracks (position, name, artist, album, cover, preview_url, popularity, spotify_url, saved_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            track["position"],
            track["name"],
            track["artist"],
            track["album"],
            track["cover"],
            track["preview_url"],
            track["popularity"],
            track["spotify_url"],
            saved_at
        ))

    conn.commit()
    conn.close()

def get_latest_tracks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tracks
        WHERE saved_at = (SELECT MAX(saved_at) FROM tracks)
        ORDER BY position
    """)

    rows = cursor.fetchall()
    conn.close()

    tracks = []
    for row in rows:
        tracks.append({
            "position": row[1],
            "name": row[2],
            "artist": row[3],
            "album": row[4],
            "cover": row[5],
            "preview_url": row[6],
            "popularity": row[7],
            "spotify_url": row[8],
            "saved_at": row[9]
        })

    return tracks