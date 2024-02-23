from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import List
from anal import run

client = MongoClient('mongodb://localhost:27017')
db = client.dbass
data_store = db.partners

def add_partner(name: str, budget: int) -> str:
    empty: List[dict] = []
    return {
        "id" : str(
            data_store.insert_one(
                {
                    "name": name, 
                    "budget": budget,
                    "spent_budget": 0,
                    "cashbacks": empty,
                    "is_stopped": False,
                }
            ).inserted_id
        ),
        "name": name,
        "budget": budget,
        "spent_budget": 0,
    }

def get_partner(id: str) -> dict:
    res = data_store.find_one({'_id': ObjectId(id)})
    return {
        "id": str(res['_id']),
        "name": res["name"],
        "budget": res["budget"],
        "spent_budget": res["spent_budget"],
        "is_stopped": res["is_stopped"]
    }
        
def add_partner_entry(o_id: str, entry: dict):
    data_store.update_one(
        {'_id': ObjectId(o_id)},
        {'$push': {
                'cashbacks': entry
            }
         }
    )
    run(data_store, o_id, entry)


