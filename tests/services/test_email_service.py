import pytest
from unittest.mock import patch
from app.services.email_service import EmailService

@pytest.fixture
def email_service():
    return EmailService()

def test_send_email_logs_correct_info(email_service):
    with patch('logging.info') as mock_log:
        email = "test@example.com"
        message = "Hello, this is a test message!"
        email_service.send_email(email, message)
        mock_log.assert_called_once_with(f"Sending email to {email}: {message}")
