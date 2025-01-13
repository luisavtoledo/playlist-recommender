import requests

print("Informe as músicas que deseja usar para recomendações, separadas por vírgula: ")

input = input("Músicas: ")

input_songs = [song.strip() for song in input.split(',') if song.strip()]

response = requests.post("http://localhost:52048/api/recommend", json={"songs": input_songs})

recommendations = response.json()

print(recommendations)