#!/usr/bin/python
import MySQLdb
import json
import requests
from config import *

db = MySQLdb.connect(host=dbhost,   # your host, usually localhost
                     user=dbuser,   # your username
                     passwd=dbpass, # your password
                     db=dbname)     # name of the data base

cur = db.cursor()
cur.execute("SELECT `email`, `site_id` FROM `guest` WHERE `newsletter` = 0 GROUP BY `email`, `site_id`")

for row in cur.fetchall():
    message = "You have a new guest! Their email address is '" + row[0] + "'"
    data = json.dumps({"bot_id": botid, "text": message})
    response = requests.post(url, data=data, headers=headers)

cur = db.cursor()
cur.execute("UPDATE `guest` SET `newsletter` = 1 WHERE `newsletter` = 0")
db.commit()

db.close()
