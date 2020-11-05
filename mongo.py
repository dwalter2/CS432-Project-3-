import pymongo
import datetime
import pprint
from pymongo import MongoClient

def da():
    client = MongoClient("mongodb+srv://dwalter2:mongodavid@cluster0.daf4k.mongodb.net/TwitterData?retryWrites=true&w=majority")
    db = client["TwitterData"]
    db1 = db["trigrams"]
    query = { 'gram' : 'covid 19 pandemic'}
    mydoc = db1.find(query)
    for x in mydoc:
        pprint.pprint(x)
da()
