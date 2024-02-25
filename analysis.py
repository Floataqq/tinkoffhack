from datetime import datetime
from typing import Literal
from enum import Enum
from os import listdir, path
from keras.models import load_model

allowed_categories = [
    'Clothes',
    'Education',
    'Food',
    'Goods',
    'Groceries',
    'Health',
    'SkinCare',
    'Software',
    'Techs',
    'Travel'
]

exec(
'''
class Category(str,Enum):
''' +
''.join([
    f'    {i} = "{i}"\n' for i in allowed_categories
])
)

models = {}

for model in listdir('models'):
    models[model.strip('.h5')] = load_model(model)

def run(data_store, id: str, date: datetime, cashback: float):
    pass
