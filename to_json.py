from pandas import read_csv
from datetime import datetime
from json import dump

allowed_categories = [
    'Clothes',
    'Education',
    'Food',
    'Goods',
    'Groceries',
    'Health',
    'SkinCare'
    'Software',
    'Techs',
    'Travel'
]
date_format = "%Y-%m-%d %H:%M:%S"

m = read_csv('Merch_CB_hack.csv')
c = read_csv('categories.csv')
res = {}
c_m = {}

for com,cat in zip(*c.to_dict(orient='list').values()):
    if cat in allowed_categories:
        c_m[com] = cat
for i in c_m:
    if c_m[i] not in res:
        res[c_m[i]] = {}
    res[c_m[i]][i] = []

for i in m.iterrows():
    thing = i[1]
    if type(thing['day']) is str:
        name = thing['merchant_name']
        time = (datetime.strptime(thing['day'], date_format) - datetime.strptime("1/1/2022", "%m/%d/%Y")).days
        if name in c_m:
            res[c_m[name]][name].append([thing['cashback'], float(time)])

for cat in res:
    for com in res[cat]:
        try:
            maximum = max(map(lambda x: x[1], res[cat][com]))
            res[cat][com] = list(
                filter(lambda x: x[1] >= maximum - 30, res[cat][com])
            )
        except:
            pass

dump(res, open('res.json', 'w+'))

