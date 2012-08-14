
import string
import pymongo
import sys
import time
import requests
import csv


c = pymongo.Connection()

db = c.db1
companies =db.companies
print db.collection_names()
count = 0
skip=0
all_companies = []
t=time.time()
print "Hello"
            
