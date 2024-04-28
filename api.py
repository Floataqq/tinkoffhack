from fastapi import FastAPI, HTTPException, APIRouter
from models import NewPartner, Partner, Nothing
from analysis import run, Category
from datetime import datetime
import db

app = FastAPI(
    docs_url="/",
    redoc_url=None,
    title="Pen is pie",
    version="1.0.0",
)
router = APIRouter()


@router.post("/api/partners", tags=["Endpoints"], response_model=NewPartner)
async def new_partner(name: str, budget: int, category: Category = None):
    """Add a new partner to the database"""
    try:
        id = db.add_partner(name, budget, category)
        return {
            "id": id["id"],
            "name": name,
            "budget": budget,
            "spent_budget": 0,
        }
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@router.get("/api/partners/{id}", tags=["Endpoints"], response_model=Partner)
async def get_partner_data(id: str):
    """Get data about a partner by partnerId"""
    try:
        return db.get_partner(id)
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@router.put("/api/partners/{id}/cashback", tags=["Endpoints"], response_model=Nothing)
async def update_partner_data(id: str, date: datetime, name: str, cashback: float):
    '''Add a cashback to the corresponding partner'''
    try:
        db.add_partner_entry(id, {"date": date, "value": cashback})
    except Exception as e:
        raise HTTPException(500, detail=str(e))


app.include_router(
    router,
    responses={
        500: {
            "content": {
                "application/json": {
                    "example": {"detail": "Could not connect to the database"}
                }
            }
        }
    },
)
