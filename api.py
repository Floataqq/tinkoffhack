from fastapi import FastAPI
import db

app = FastAPI()

@app.post('/api/partners')
async def new_partner(name: str, budget: int):
    id = db.add_partner(name, budget)
    return {
        "id": id,
        "name": name,
        "budget": budget,
        "spent_budget": 0,
    }

@app.get('/api/partners/{id}')
async def get_partner_data(id: str):
    return db.get_partner(id)

@app.put('/api/partners/{id}/cashback')
async def update_partner_data(id: str, date: str, name: str, chashback: float):
    db.add_partner_entry(id, {"date": date, "value": value})

