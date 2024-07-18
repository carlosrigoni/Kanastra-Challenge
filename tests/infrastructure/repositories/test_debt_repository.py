import logging
from unittest.mock import patch

import pytest

from app.domain.models.debt import Debt
from app.infrastructure.repositories.debt_repository import DebtRepository

def test_save_debt():
    debt = Debt(
        name="user",
        governmentId="12345678901",
        email="user@example.com",
        debtAmount=1500.50,
        debtDueDate="2024-07-17",
        debtId="123e4567-e89b-12d3-a456-426614174000"
    )
    
    with patch('logging.Logger.info') as mock_log:
        repo = DebtRepository()
        repo.save(debt.debtId)
        
        mock_log.assert_called_with(f"Saving debt record for {debt.debtId}")
