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
async def get(id: int):
    return db.get_partner(id)

@app.put('/api/partners/{id}/cashback')
async def update(id: int, date: str, name: str, chashback: float):
    db.add_user_entry(id, {"date": date, "value": value})

