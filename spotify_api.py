import os
import base64
import requests

# Soundly
# Rhythmo


# Substitua pelas suas credenciais do Spotify Developer
# ___________________________ https://developer.spotify.com/dashboard ___________________________


CLIENT_ID = os.environ['SPOTIFY_DEV_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_DEV_CLIENT_SECRET']

# 1. Gerar o token de acesso
def get_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

# 2. Usar o token para fazer um GET
def get_artist_info(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_playlist_tracks(playlist_id, token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()



if __name__ == "__main__":
    token = get_token(CLIENT_ID, CLIENT_SECRET)
    print(f"TOKEN: {token}")
    

    # # Exemplo: ID do Daft Punk
    # artist_id = "4tZwfgrHOc3mvqYlEYSvVi"
    # artist_info = get_artist_info(artist_id, token)
    
    # print(artist_info)
    
    # print("Nome:", artist_info["name"])
    # print("Gêneros:", artist_info["genres"])
    # print("Followers:", artist_info["followers"]["total"])
    
    # Top 100 Global
    playlist_id = "0sDahzOkMWOmLXfTMf2N4N"
    data = get_playlist_tracks(playlist_id, token)
    print(data)

    for item in data["items"][:10]:  # mostra só os 10 primeiros
        track = item['track']
        print("\nMúsica:", track["name"])
        print("Artista:", track["artists"][0]["name"])
        print("Link:", track["external_urls"]["spotify"])
        print("-" * 40)

