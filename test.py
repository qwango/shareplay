
import string
import pymongo
import sys
import time
import requests
import csv


c = pymongo.Connection()

db = c.db1
companies =db.companies
company = dict(tidm='VOD', name='Vodafone Group PLC', keywords=['Vodafone', 'Group'])
companies.insert(company)
print db.collection_names()
count = 0
skip=0
all_companies = []
t=time.time()
print "Hello"*5
            
