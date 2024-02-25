from datetime import datetime
from typing import Literal
from enum import Enum

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

def run(data_store, id: str, date: datetime, cashback: float):
    pass
