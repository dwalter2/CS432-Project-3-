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
    p1 = totalAveragePolarity[0]["ave"]
    print("The total average polarity for our dataset is: " + str(p1))
    v = list(db1.find().sort([("New Cases",-1)]).limit(1)) # get worst case date
    firstDate = v[0]["Date"]
    print("The date with the highest amount of new cases was: " + str(firstDate))
    y = list(db2.aggregate([ {"$match" :  { "Date"  : { "$eq" : firstDate }} }, {"$group" : {"_id" : "null" , "averagePol" : { "$avg" : "$Polarity"}}} ])) # get average polartiy
    avpol = y[0]["averagePol"]
    print("The average polarity for that date was: " + str(avpol))
    maxDate = list(db2.find().sort([("Date",-1)]).limit(1)) #find max twitter date
    maximumDate = (maxDate[0]["Date"])
    #secondQuery = list(db1.find( { "$and" : [ { "New Cases"  : { "$eq" : 0 } } , { "7-Day Moving Avg" : { "$gt" : 1700 } }, {"7-Day Moving Avg" : {"$lt" : 2200} }] }).limit(1))
    secondQuery = db1.find( { "$and" : [{ "Date" : { "$lt" : maximumDate}} , {"7-Day Moving Avg" : { "$ne" : 0}}] }).sort([("7-Day Moving Avg",1)]).limit(1) # find min cases without average as 0 before max twitter date
    secondDate = secondQuery[0]["Date"]
    print("The date with the lowest 7-day moving average excluding 0 was: " + str(secondDate))
    secavpol = list(db2.aggregate([ {"$match" :  { "Date"  : { "$eq" : secondDate }} }, {"$group" : {"_id" : "null" , "averagePol" : { "$avg" : "$Polarity"}}} ])) # find average polarity for that date
    p2 = secavpol[0]["averagePol"]
    print("The average polarity for that date was: " + str(p2))

da()
