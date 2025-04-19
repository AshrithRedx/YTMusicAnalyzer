import json
import re
import pandas as pd
from ytmusicapi import YTMusic
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ytmusic = YTMusic()

def clean_artist_name(name):
    return name.split(",")[0].split(" and ")[0].strip()

def get_playlist_data(playlist_id):
    playlist = ytmusic.get_playlist(playlist_id)
    song_data = []

    for track in playlist.get("tracks", []):
        song_name = track.get("title", "Unknown Song")
        artists = [clean_artist_name(artist["name"]) for artist in track.get("artists", [])]
        song_data.append({"song": song_name, "artists": artists})

    df = pd.DataFrame(song_data).explode("artists")
    artist_counts = df["artists"].value_counts().reset_index()
    artist_counts.columns = ["Artist", "Song Count"]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.title(f"Artist Frequency in '{playlist['title']}'")
    plt.xticks(rotation=45, ha='right')
    plt.bar(artist_counts["Artist"], artist_counts["Song Count"], color="skyblue")
    plt.tight_layout()
    plt.savefig("artist_frequency.png")

    return {
        "playlist_title": playlist["title"],
        "artist_data": artist_counts.to_dict(orient="records")
    }
