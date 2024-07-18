from fastapi import FastAPI
from app.api.v1.endpoints import upload
import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

file_upload_api = upload.FileUploadAPI()

app.include_router(file_upload_api.router, prefix="/api/v1")

logging.info("FastAPI application started")