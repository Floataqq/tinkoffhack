from datetime import datetime
from typing import Literal

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

Category = Literal[*allowed_categories]

def run(data_store, id: str, date: datetime, cashback: float):
    pass
