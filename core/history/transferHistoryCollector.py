import pymongo
from pymongo import MongoClient


class TransferHistoryCollector:

    def __init__(self):
        client = MongoClient()
        fut_db = client.futTrader
        stat_collection = fut_db.transferHistory

