import requests
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path='C:/Users/539555318/Desktop/API-NBA/.venv/.env')
token = os.getenv('token_api')


url = 'https://api.football-data.org/v4/competitions'
headers = { 'X-Auth-Token': token,
           'Content-Type': 'application/json'}

contador_requisicao = 0

saida = requests.get(url, headers= headers)
saida = saida.json()

ids = []
for competicao in saida['competitions']:
    contador_requisicao += 1
    id_comp = f'{competicao['id']}'
    ids.append(id_comp)

time.sleep(50)

for i in ids:
    url_campeonatos= f'https://api.football-data.org/v4/competitions/{i}/standings'
    saida = requests.get(url_campeonatos, headers=headers)
    contador_requisicao += 1
    saida = saida.json()
    nome_camp = f'{saida['competition']['name']}'

    print(saida)
    print('')
    time.sleep(1)


print(contador_requisicao)

chaves = []
tabela_brasileira = []
dicionario = {}

# for brasileirao in standings:
#    id_team = {brasileirao['team']['id']}
#    dados_restantes = (f'{brasileirao['team']['name']}'), (f'Partidas: {brasileirao['playedGames']}'), (f'Vitorias: {brasileirao['won']}'), (f'Empates: {brasileirao['draw']}'), (f'Derrotas: {brasileirao['lost']}' )
#    colocao = (f'Posição: {brasileirao['position']}')
#    tabela_brasileira.append(dados_restantes) 
#    chaves.append(colocao)

# # print(tabela_brasileira)
# # print(standings)
# def dados_brasileirao():
#     for i in range(len(chaves)):
#         dicionario[chaves[i]] = tabela_brasileira[i]
