import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='C:/Users/539555318/Desktop/API-NBA/.venv/.env')
token = os.getenv('token')


url = 'https://api.football-data.org/v4/competitions'
headers = { 'X-Auth-Token': token,
           'Content-Type': 'application/json'}


saida = requests.get(url, headers= headers)
saida = saida.json()


for competicao in saida['competitions']:
    id_comp = f'{competicao['id']}, nome da competição: {competicao['name']}'
    emblema= {competicao['emblem']}
    


url_brasileirao = 'https://api.football-data.org/v4/competitions/2013/standings'

saida_champions = requests.get(url_brasileirao, headers=headers)
saida_champions = saida_champions.json()

standings = saida_champions['standings'][0]['table']


for brasileirao in standings:
    print(f'times: {brasileirao['team']['name']} -- id: {brasileirao['team']['id']} -- {brasileirao['team']['crest']} \n' )

for nra