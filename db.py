from bson.objectid import ObjectId
from typing import List, Optional
from pymongo import MongoClient
from analysis import run

client = MongoClient("mongodb://localhost:27017")
db = client.dbass
data_store = db.partners


def add_partner(name: str, budget: int, category: Optional[str]) -> str:
    """Add a partner to the database:
    name (str) - the company name
    budget (int) - the allocated budget
    category (optional str) - one of the valid categories from `analisys`; adding a category helps get results faster and makes hem more accurate.
    """
    empty: List[dict] = []
    return {
        "id": str(
            data_store.insert_one(
                {
                    "name": name,
                    "budget": budget,
                    "spent_budget": 0,
                    "cashbacks": empty,
                    "is_stopped": False,
                    "category": category,
                }
            ).inserted_id
        ),
        "name": name,
        "budget": budget,
        "spent_budget": 0,
    }


def get_partner(id: str) -> dict:
    """Get a partner from the database:
    id (str) - partner id (mongodb ObjectId)
    """
    res = data_store.find_one({"_id": ObjectId(id)})
    return {
        "id": str(res["_id"]),
        "name": res["name"],
        "budget": res["budget"],
        "spent_budget": res["spent_budget"],
        "is_stopped": res["is_stopped"],
    }


def add_partner_entry(o_id: str, entry: dict):
    """Add a cashback to some partner data:
    o_id (str) - partner id (mongodb ObjectId)
    """
    data_store.update_one({"_id": ObjectId(o_id)}, {"$push": {"cashbacks": entry}})
    obj = data_store.find_one({"_id": ObjectId(o_id)})
    recent = [i["value"] for i in obj["cashbacks"]]
    branch = obj["category"] or None
    budget = obj["budget"]
    data_store.update_one(
        {"_id": ObjectId(o_id)},
        {
            "$set": {
                "is_stopped": run(recent, entry["value"], branch, budget),
                "spent_budget": obj["spent_budget"] - entry["value"],
            }
        },
    )
