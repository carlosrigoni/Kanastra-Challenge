import csv
from io import StringIO
import logging
from typing import List

from app.domain.models.debt import Debt
from app.services.billing_service import BillingService

class ProcessorService:
    def __init__(self):
        self.billing_service = BillingService()

    def process_csv(self, content: bytes):
        logging.info("Processing CSV file")
        file = StringIO(content.decode())
        reader = csv.DictReader(file)
        logging.info("CSV file read successfully")
        for row in reader:
            try:
                debt = {
                    "name": row['name'],
                    "governmentId": row['governmentId'],
                    "email": row['email'],
                    "debtAmount": float(row['debtAmount']),
                    "debtDueDate": row['debtDueDate'],
                    "debtId": row['debtId']
                }
                
                self.billing_service.process_debt(debt)
            except KeyError as e:
                logging.error(f"Error processing row {str(e)}")
                continue