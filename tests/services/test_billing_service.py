import pytest
from unittest.mock import patch, MagicMock

from app.services.billing_service import BillingService
from app.domain.models.debt import Debt

@pytest.fixture
def debts():
    return [
        Debt(name="User", governmentId="123", email="user@example.com", debtAmount=1000.0, debtDueDate="2024-08-01", debtId="123e4567-e89b-12d3-a456-426614174000"),
        Debt(name="User2", governmentId="456", email="user2@example.com", debtAmount=2000.0, debtDueDate="2024-08-02", debtId="123e4567-e89b-12d3-a456-426614174001")
    ]

@pytest.fixture
def billing_service():
    with patch('app.infrastructure.repositories.debt_repository.DebtRepository') as mock_repo, \
         patch('app.services.email_service.EmailService') as mock_email:
        service = BillingService()
        service.debt_repository = mock_repo
        service.email_service = mock_email
        return service