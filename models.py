from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TrxnType(str, Enum):
    income = "income"
    expense = "expense"

class TrxnCategory(str, Enum):
    food = "food"
    transport = "transport"
    entertainment = "entertainment"
    health = "health"
    education = "education"
    other = "other"

class TrxnCreate(BaseModel):
    amount: int
    type: TrxnType
    category: TrxnCategory
    note: str

class TrxnUpdate(BaseModel):
    amount: Optional[int] = None
    type: Optional[TrxnType] = None
    category: Optional[TrxnCategory] = None
    note: Optional[str] = None

class TrxnResponse(BaseModel):
    uid: int
    amount: int
    type: TrxnType
    category: TrxnCategory
    note: str