import random
import time
from pymongo import MongoClient
from core.connector.fut_api import FutApi


class TransferHistoryCollector:

    def __init__(self):
        self.session = FutApi().get_session()

        # client = MongoClient()
        # fut_db = client.futTrader
        # transfer_collection = fut_db.transferHistory
        self.transfer_collection = MongoClient()['fut_trader']['transfers']
        self.watched_list = MongoClient()['fut_trader']['watched_list']

    def run(self):
        players_dict = self.session.players

        premier_league = 13
        auctions = self.session.searchAuctions(ctype='player', level='gold', league=premier_league, max_buy=3000)
        time.sleep(random.randint(1, 3))
        interesting_rare = [p for p in auctions if p['rareflag'] == 1 and p['rating'] >= 76]

        for auction in interesting_rare:
            asset_id = auction['assetId']
            player_info = players_dict[asset_id]
            self.watched_list.insert_one(player_info)


collector = TransferHistoryCollector()
collector.run()
