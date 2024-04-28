from pydantic import BaseModel


class NewPartner(BaseModel):
    """A partner model:
    id (str) - a mongodb ObjectId
    name (str) - the company name
    budget (int) - the allocated company budget
    spent_budget (int) - the already spent budget
    """

    id: str
    name: str
    budget: int
    spent_budget: int


class Partner(BaseModel):
    """A model for partners already being stored in the database:
    id (str) - a mongodb ObjectId
    name (str) - compnay name
    budget (int) - the allocated company budget
    spent_budget (int) - the already spent budget
    is_stopped (bool) - a flag indicating whether this partner's deal has been stopped
    """

    id: str
    name: str
    budget: int
    spent_budget: int
    is_stopped: bool


class Nothing(BaseModel): ...
