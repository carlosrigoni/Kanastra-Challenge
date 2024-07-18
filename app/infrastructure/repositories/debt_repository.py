import logging
from app.domain.models.debt import Debt

class DebtRepository:
    def save(self, debt_id):
        logging.info(f"Saving debt record for {debt_id}")