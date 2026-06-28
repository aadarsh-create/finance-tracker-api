from pydantic import BaseModel
from typing import Optional

class TrxnCreate(BaseModel):
    amount: int
    note: str

class TrxnUpdate(BaseModel):
    amount: Optional[int] = None
    note: Optional[str] = None

class TrxnResponse(BaseModel):
    uid: int
    amount: int
    note: str