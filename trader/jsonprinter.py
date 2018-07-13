import json
# import fut
# import fut.core
from pprint import pprint


with open('../tests/data/players.json') as f:
    data = json.load(f)

legendPlayers = data['LegendsPlayers']
players = data['Players']


id = 212476
player = [p for p in players if p['id'] == id]
ronaldinho = [p for p in legendPlayers if p['id'] == 238395]

# ps = fut.core.players()
# print(ps)

pprint(ronaldinho)
pprint(player)
# pprint(legendPlayers)