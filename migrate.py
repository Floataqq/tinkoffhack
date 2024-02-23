from bson.objectid import ObjectId
from datetime import datetime
import pandas as pd
import db

df = pd.read_csv('Merch_CB_hack.csv')
companies = {}

for row in df.iterrows():
    s = row[1]
    if s[0] not in companies:
        companies[s[0]] = db.add_partner(s[0], 0)['id']
    if type(s[1]) is str:
        date = s[1].split()[0]
        date = datetime.strptime(date, '%Y-%m-%d')
        db.add_partner_entry(companies[s[0]], {'date': date, 'value': s[3]})

