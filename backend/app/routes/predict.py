from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
def predict():
    return {
        "filename": "test.jpg",
        "image_width": 1280,
        "image_height": 720,
        "detections": [
            {
                "class_name": "smoke",
                "confidence": 0.86,
                "bbox": [120, 80, 420, 300]
            },
            {
                "class_name": "fire",
                "confidence": 0.78,
                "bbox": [650, 200, 820, 420]
            }
        ],
        "risk_level": "high",
        "summary": {
            "smoke_count": 1,
            "fire_count": 1,
            "max_confidence": 0.86
        }
    }