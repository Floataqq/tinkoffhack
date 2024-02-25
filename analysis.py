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

def normalize(y_cashbacks, budget):
    print(y_cashbacks.shape[0])
    if y_cashbacks.shape[0] < 5:
      return pd.DataFrame([[0] * len(y_cashbacks.columns)] * len(y_cashbacks), columns=y_cashbacks.columns)
    ymax = max(max(y_cashbacks['0']), budget)
    y_norm = y_cashbacks['0'] / ymax
    return y_norm

def algo(cash, branch, y_cashbacks, budget):
    x_new = pd.DataFrame([[i/15] for i in range(1, 16)])
    y_cashbacks = y_cashbacks.append({'0': cash}, ignore_index=True)
    y_norm = normalize(y_cashbacks, budget)
    model = load_model(f"models/{branch}_model.h5")

    predicted_cashback = model.predict(x_new.values.reshape(-1, 1, 1))

    res = (predicted_cashback[0][0] >= y_norm.iloc[-1])
    return bool(res)


def algo_branch(cash, branches, y_cashbacks, budget):
    loss_list = []
    x_new = pd.DataFrame([[i/15] for i in range(1, 16)])
    y_norm = normalize(y_cashbacks, budget)

    for branch in branches:
        model = load_model(f"models/{branch}_model.h5")
        loss = model.evaluate(x_new.values.reshape((-1, 1, 1)), 1)
        loss_list.append([branch, loss])

    loss_list.sort(key=lambda x: x[1])
    need_branch = loss_list[0][0]
    
    return algo(cash, need_branch, y_cashbacks, budget)

def run(recent: List[float], cashback: float, 
        branch: Literal[*allowed_categories], budget):
    if branch:
        return algo(cashback, branch, pd.DataFrame({'0': recent or []}), budget)
    else:
        return algo_branch(cashback, allowed_categories, 
                           pd.DataFrame({'0': recent or []}), budget)



