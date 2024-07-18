from typing import List
import logging

from app.domain.models.debt import Debt
from app.infrastructure.repositories.debt_repository import DebtRepository
from app.services.email_service import EmailService

class BillingService:
    def __init__(self):
        self.processed_ids = set()
        self.debt_repository = DebtRepository()
        self.email_service = EmailService()
        
    def process_debt(self, debt: Debt):
        try:
            if self.is_processed(debt["debtId"]):
                logging.info(f"Skipping debt with ID {debt['debtId']}")
                return
            self.create_invoice(debt["debtId"])
            self.mark_as_processed(debt["debtId"])
            self.debt_repository.save(debt["debtId"])
            self.email_service.send_email(debt["email"], "Invoice created successfully")
        except Exception as e:
            logging.error(f"Error processing debt {str(e)}")
            

    def is_processed(self, debt_id):
        return debt_id in self.processed_ids

    def create_invoice(self, debt_id):
        logging.info(f"Creating invoice with ID {debt_id}")

    def mark_as_processed(self, debt_id):
        self.processed_ids.add(debt_id)
