import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

router = APIRouter()

UPLOAD_DIR = Path("temp_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Check if it's a picture
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "saved_path": str(file_path),
        "message": "File received successfully"
    }