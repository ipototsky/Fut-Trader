import json
import fut
import fut.core
import time
import random
from pprint import pprint


class FutTrader:

    def __init__(self):
        self.prices_by_id = {}
        self.init_prices()
        self.players = fut.core.players()

        email = 'pototskyvanya@gmail.com'
        password = 'Kolasa621963'
        secret = 'kolasa'
        platform = 'xbox360'

        self.session = fut.Core(email=email, passwd=password, secret_answer=secret, platform=platform, debug=True)
        time.sleep(random.randint(1, 3))

    def run(self):
        premier_league = 13
        laLiga = 53

        players = self.session.searchAuctions(ctype='player', level='gold', league=premier_league, max_buy=2000)
        rare_players_rating_80 = [p for p in players if p['rareflag'] == 1 and p['rating'] >= 80 ]
        interesting_players = [p for p in players if p['rareflag'] == 1 and p['rating'] >= 80 and p['resourceId'] in self.prices_by_id]

        for rare_player in rare_players_rating_80:
            players_for_compare = []
            self.print_player(rare_player)
            def_id = rare_player['resourceId']
            auctions = self.session.searchAuctions(ctype='player', defId=def_id)
            page = 0
            while auctions:
                page += 1
                players_for_compare.extend(auctions)
                time.sleep(random.randint(1, 2))
                auctions = self.session.searchAuctions(ctype='player', defId=def_id, start=page)

            players_for_compare_by_id = {x['tradeId']: x for x in players_for_compare}
            print("Finish Rare Player")

        print('Hello')

    def print_player(self, player):
        pprint(player)
        pprint(self.players[player['assetId']])

    def test(self, id):
        result = self.session.searchDefinition(id)
        print(result)

    def init_prices(self):
        with open('../help/prices.json') as f:
            prices_by_id = json.load(f)
        for p in prices_by_id['prices']:
            self.prices_by_id[p['id']] = {'id': p['id'],
                                'name': p['name'],
                                'price': p['price']}


trader = FutTrader()
trader.run()
