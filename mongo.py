import pymongo
import datetime
import os
import pprint
import csv
import pandas as pd
from pymongo import MongoClient

def da():
    client = MongoClient("mongodb+srv://dwalter2:mongodavid@cluster0.daf4k.mongodb.net/TwitterData?retryWrites=true&w=majority")
    db = client["CovidData"]
    db1 = db["DayTotals"]
    query = { "$max" : "New Cases"}
    #v = db1.find( {"$max" : "$New Cases"})
    v = list(db1.find().sort([("New Cases",-1)]).limit(1))
    print(v[0]["Date"].strftime("%m %d %Y"))
    x = list(db1.find().sort([("New Cases",1)]).limit(1))
    print(x[0]["New Cases"])

da()
