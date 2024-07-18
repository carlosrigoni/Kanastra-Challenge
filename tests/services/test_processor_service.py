import pytest
from io import BytesIO
from unittest.mock import MagicMock, call

from app.services.processor_service import ProcessorService
from app.domain.models.debt import Debt

# Test data
valid_csv_data = b"name,governmentId,email,debtAmount,debtDueDate,debtId\nJohn Doe,1234,john@example.com,1500.00,2023-12-31,123e4567-e89b-12d3-a456-426614174000\nJane Doe,1235,jane@example.com,2000.00,2023-12-30,123e4567-e89b-12d3-a456-426614174001"
missing_columns_csv_data = b"name,email,debtAmount,debtDueDate,debtId\nJohn Doe,john@example.com,1500.00,2023-12-31,123e4567-e89b-12d3-a456-426614174000"
empty_csv_data = b"name,governmentId,email,debtAmount,debtDueDate,debtId"

@pytest.fixture
def processor_service():
    service = ProcessorService()
    service.billing_service = MagicMock()
    return service

def test_process_csv_with_valid_data(processor_service):
    valid_csv_data = b"name,governmentId,email,debtAmount,debtDueDate,debtId\nJohn Doe,1234,john@example.com,1500.00,2023-12-31,123e4567-e89b-12d3-a456-426614174000\nJane Doe,1235,jane@example.com,2000.00,2023-12-30,123e4567-e89b-12d3-a456-426614174001"
    processor_service.process_csv(valid_csv_data)
    
    # Check if process_debt is called exactly twice (once for each row in the CSV)
    assert processor_service.billing_service.process_debt.call_count == 2

    # Check the calls with the expected debt data
    expected_calls = [
        call({
            "name": "John Doe",
            "governmentId": "1234",
            "email": "john@example.com",
            "debtAmount": 1500.00,
            "debtDueDate": "2023-12-31",
            "debtId": "123e4567-e89b-12d3-a456-426614174000"
        }),
        call({
            "name": "Jane Doe",
            "governmentId": "1235",
            "email": "jane@example.com",
            "debtAmount": 2000.00,
            "debtDueDate": "2023-12-30",
            "debtId": "123e4567-e89b-12d3-a456-426614174001"
        })
    ]
    processor_service.billing_service.process_debt.assert_has_calls(expected_calls, any_order=True)

def test_process_csv_with_missing_columns(processor_service):
    processor_service.process_csv(missing_columns_csv_data)
    assert not processor_service.billing_service.process_debt.called

def test_process_csv_with_empty_data(processor_service):
    processor_service.process_csv(empty_csv_data)
    assert not processor_service.billing_service.process_debt.called 
