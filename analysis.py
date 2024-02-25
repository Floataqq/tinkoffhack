from datetime import datetime
from typing import Literal, List
from enum import Enum
from os import listdir, path
from keras.models import load_model
import pandas as pd


allowed_categories = [
    'Clothes',
    'Education',
    'Food',
    'Goods',
    'Groceries',
    'Health',
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

def algo(cash, branch, y_cashbacks):
    x_new = pd.DataFrame([[i/15] for i in range(1, 16)])
    y_cashbacks.append(cash)
    
    model = load_model(f"{branch}_model.h5")

    predicted_cashback = model.predict(x_new.values.reshape((1, 15, 1)))

    return predicted_cashback[0][0] >= cash

def algo_branch(cash, branches, y_cashbacks):
    loss_list = []
    x_new = pd.DataFrame([[i/15] for i in range(1, 16)])
    y_cashbacks.append(cash)

    for branch in branches:
        model = load_model(f"models/{branch}_model.h5")
        loss = model.evaluate(x_new.values.reshape((1, 15, 1)), [cash]*15)  
        loss_list.append([branch, loss])

    loss_list.sort(key=lambda x: x[1])
    need_branch = loss_list[0][0]
    
    return algo(cash, need_branch, y_cashbacks)

def run(recent: List[float], cashback: float, 
        branch: Literal[*allowed_categories]):
    if branch:
        algo(cashback, branch, recent or [])
    else:
        algo_branch(cashback, allowed_categories, recent or [])



