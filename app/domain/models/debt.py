from pydantic import BaseModel, EmailStr
from datetime import date
import uuid

class Debt(BaseModel):
    name: str
    governmentId: str
    email: EmailStr
    debtAmount: float
    debtDueDate: date
    debtId: uuid.UUID
