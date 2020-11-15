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
    db2 = db["TwitterAnalysis"]
    query = { "$max" : "New Cases"}
    #v = db1.find( {"$max" : "$New Cases"})
    totalAveragePolarity = list(db2.aggregate([{"$group" : {"_id" : "null" , "ave" : {"$avg" : "$Polarity"}}}]))
    print(totalAveragePolarity[0]["ave"])
    v = list(db1.find().sort([("New Cases",-1)]).limit(1))
    firstDate = v[0]["Date"]
    print(firstDate)
    y = list(db2.aggregate([ {"$match" :  { "Date"  : { "$eq" : firstDate }} }, {"$group" : {"_id" : "null" , "averagePol" : { "$avg" : "$Polarity"}}} ]))
    avpol = y[0]["averagePol"]
    print(avpol)
    maxDate = list(db2.find().sort([("Date",-1)]).limit(1))
    maximumDate = (maxDate[0]["Date"])
    #secondQuery = list(db1.find( { "$and" : [ { "New Cases"  : { "$eq" : 0 } } , { "7-Day Moving Avg" : { "$gt" : 1700 } }, {"7-Day Moving Avg" : {"$lt" : 2200} }] }).limit(1))
    secondQuery = db1.find( { "$and" : [{ "Date" : { "$lt" : maximumDate}} , {"7-Day Moving Avg" : { "$ne" : 0}}] }).sort([("7-Day Moving Avg",1)]).limit(1)
    secondDate = secondQuery[0]["Date"]
    print(secondDate)
    secavpol = list(db2.aggregate([ {"$match" :  { "Date"  : { "$eq" : secondDate }} }, {"$group" : {"_id" : "null" , "averagePol" : { "$avg" : "$Polarity"}}} ]))
    print(secavpol[0]["averagePol"])

da()
