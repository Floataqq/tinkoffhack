from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import json
import db

app = FastAPI()

@app.get('/', include_in_schema=False)
async def root():
    with open('./static/index.html', 'r') as f:
        content = f.read()
    return HTMLResponse(content=content, status_code=200)

@app.get('/ui.json', include_in_schema=False)
async def ui_json():
    return json.load(open('static/ui.json', 'r'))

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

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Pen is pie",
        version="1.0.0",
        summary="",
        description="",
        routes=app.routes,
    )
    '''
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    '''
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

