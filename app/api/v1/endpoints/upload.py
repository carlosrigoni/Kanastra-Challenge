from fastapi import APIRouter, UploadFile, HTTPException
from app.services.processor_service import ProcessorService

class FileUploadAPI:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()
        self.processor_service = ProcessorService()

    def setup_routes(self):
        self.router.post("/upload_file", response_model=dict)(self.upload_file)

    async def upload_file(self, file: UploadFile):
        try:
            contents = await file.read()
            self.processor_service.process_csv(contents)
            return {"message": "File processed successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))