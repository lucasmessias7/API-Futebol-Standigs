import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='C:/Users/539555318/Desktop/API-NBA/.venv/.env')
token = os.getenv('token')

token = 'a4c4340c7fef4c3dbaae344d7118d771'

url = 'https://api.football-data.org/v4/competitions'
headers = { 'X-Auth-Token': token,
           'Content-Type': 'application/json'}


saida = requests.get(url, headers= headers)
saida = saida.json()


for competicao in saida['competitions']:
    id_comp = f'{competicao['id']}, nome da competição: {competicao['name']}'
    emblema= {competicao['emblem']}
    

url_champions_league = 'https://api.football-data.org/v4/competitions/2013/standings'

saida_champions = requests.get(url_champions_league, headers=headers)
saida_champions = saida_champions.json()

print(saida_champions)

# for brasileirao in saida['teams']:
#     times_brasileiros = ''