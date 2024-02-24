from pydantic import BaseModel

class NewPartner(BaseModel):
    id: str
    name: str
    budget: int
    spent_budget: int

class Partner(BaseModel):
    id: str
    name: str
    budget: int
    spent_budget: int
    is_stopped: bool

class Nothing(BaseModel):
    ...

