import random
import time
from pymongo import MongoClient
from core.connector.fut_api import FutApi


class TransferHistoryCollector:

    def __init__(self):
        self.session = FutApi().get_session()

        db = MongoClient()['fut_trader']
        self.auctions = db['auctions']
        self.watched_players = db['watched_players']
        self.requests = db['requests']

    def run(self):
        players_dict = self.session.players
        premier_league = 13

        start = 0
        page_size = 36
        while self.session.get_number_of_requests()['requests'] < 50:
            auctions = self.session.searchAuctions(ctype='player', level='gold', league=premier_league, max_buy=10000, start=start)
            start += page_size;
            interesting_rare = [p for p in auctions if p['rareflag'] == 1 and p['rating'] >= 79]

            for auction in interesting_rare:
                try:
                    asset_id = auction['assetId']
                    player_info = players_dict[asset_id]

                    # insert if not exists only
                    if '_id' not in player_info:
                        player_info['_id'] = player_info['id']
                    self.watched_players.update_one({'_id': player_info['_id']}, {'$setOnInsert': player_info}, upsert=True)
                    # insert or update
                    if '_id' not in auction:
                        auction['_id'] = auction['resourceId']
                    self.auctions.update_one({'_id': auction['_id']}, {'$set': auction}, upsert=True)
                except Exception as exception:
                    print(player_info)
                    print(exception)

            time.sleep(random.randint(1, 3))

        self.requests.insert_one({'count': self.session.get_number_of_requests()['requests']})


collector = TransferHistoryCollector()
collector.run()
