import os
import base64
import requests
import urllib.parse
from flask import Flask, redirect, request

app = Flask(__name__)

# ___________________________ https://developer.spotify.com/dashboard ___________________________

CLIENT_ID = os.environ['SPOTIFY_DEV_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_DEV_CLIENT_SECRET']

REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "playlist-read-private user-library-read"

# 1️⃣ Página inicial: redireciona para login Spotify
@app.route("/")
def login():
    auth_url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE
    }
    return redirect(f"{auth_url}?{urllib.parse.urlencode(params)}")

# 2️⃣ Callback: Spotify envia o código aqui
@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Erro: nenhum código recebido"

    # 3️⃣ Trocar código por access_token
    token_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    r = requests.post(token_url, headers=headers, data=data)
    r.raise_for_status()
    tokens = r.json()
    access_token = tokens["access_token"]

    # 4️⃣ Usar access_token para pegar playlists do usuário
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get("https://api.spotify.com/v1/me/playlists", headers=headers)
    playlists = r.json()["items"]

    result = "<h2>Playlists do usuário:</h2><ul>"
    for p in playlists:
        result += f"<li>{p['name']} - <a href='{p['external_urls']['spotify']}'>Abrir no Spotify</a></li>"
    result += "</ul>"
    
    # playlist_id = "37i9dQZEVXbMDoHDwVN2tF"  # Top 50 Global
    # r = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers=headers)
    # r.raise_for_status()

    # data = r.json()

    # for item in data["items"][:10]:  # mostra só os 10 primeiros
    #     track = item['track']
    #     print("\nMúsica:", track["name"])
    #     print("Artista:", track["artists"][0]["name"])
    #     print("Link:", track["external_urls"]["spotify"])
    #     print("-" * 40)
    return result

if __name__ == "__main__":
    app.run(port=8888, debug=True)
