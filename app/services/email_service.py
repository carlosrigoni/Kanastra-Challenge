import logging

class EmailService:
    def send_email(self, email, message):
        logging.info(f"Sending email to {email}: {message}")
