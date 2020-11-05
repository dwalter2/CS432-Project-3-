import pymongo
from pymongo import MongoClient

def da():
    client = MongoClient("mongodb+srv://dwalter2:mongodavid@cluster0.daf4k.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
    db = client["sample_airbnb"]
    db1 = db["listingAndReviews"]
    print(db1.collectionName)
da()
