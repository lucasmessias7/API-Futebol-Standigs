import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='C:/Users/539555318/Desktop/API-NBA/.venv/.env')
token = os.getenv('token_api')


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

chaves = []
tabela_brasileira = []
dicionario = {}

for brasileirao in standings:
   id_team = {brasileirao['team']['id']}
   dados_restantes = (f'{brasileirao['team']['name']}'), (f'Partidas: {brasileirao['playedGames']}'), (f'Vitorias: {brasileirao['won']}'), (f'Empates: {brasileirao['draw']}'), (f'Derrotas: {brasileirao['lost']}' )
   colocao = (f'Posição: {brasileirao['position']}')
   tabela_brasileira.append(dados_restantes) 
   chaves.append(colocao)

# print(tabela_brasileira)
# print(standings)
def dados_brasileirao():
    for i in range(len(chaves)):
        dicionario[chaves[i]] = tabela_brasileira[i]
    return dicionario

dados_brasileirao()