from app.domain.models.debt import Debt
import pytest
from pydantic import ValidationError
from datetime import date, timedelta
import uuid


def test_debt_creation():
    debt_id = uuid.uuid4()
    debt = Debt(
        name="user",
        governmentId="12345678901",
        email="user@example.com",
        debtAmount=1500.50,
        debtDueDate=date.today() + timedelta(days=30),
        debtId=debt_id
    )
    
    assert debt.name == "user"
    assert debt.governmentId == "12345678901"
    assert debt.email == "user@example.com"
    import math
    assert math.isclose(debt.debtAmount, 1500.50, rel_tol=1e-9, abs_tol=0.0)
    assert debt.debtDueDate == date.today() + timedelta(days=30)
    assert debt.debtId == debt_id

def test_invalid_email():
    with pytest.raises(ValidationError):
        Debt(
            name="user",
            governmentId="12345678901",
            email="user",
            debtAmount=1500.50,
            debtDueDate=date.today() + timedelta(days=30),
            debtId=uuid.uuid4()
        )

# def test_negative_debt_amount():
#     with pytest.raises(ValidationError):
#         Debt(
#             name="User",
#             governmentId="12345678901",
#             email="user@example.com",
#             debtAmount=-100.00,
#             debtDueDate=date.today() + timedelta(days=30),
#             debtId=uuid.uuid4()
#         )

# def test_invalid_date():
#     with pytest.raises(ValidationError):
#         Debt(
#             name="User",
#             governmentId="12345678901",
#             email="user@example.com",
#             debtAmount=1500.50,
#             debtDueDate=date.today() - timedelta(days=1),  # Data no passado
#             debtId=uuid.uuid4()
#         )

