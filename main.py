from fastapi import FastAPI, File, UploadFile, HTTPException
from transformers import AutoModelForImageClassification, ViTImageProcessor
from PIL import Image
import torch
import os

app = FastAPI()

model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection')

@app.get("/")
def read_root():
    return {"Hello": "World"}

def classify_image(img_path):
    img = Image.open(img_path)
    with torch.no_grad():
        inputs = processor(images=img, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
    predicted_label = logits.argmax(-1).item()
    label = model.config.id2label[predicted_label]
    return label

@app.post("/classify")
async def classify_endpoint(file: UploadFile = File(...)):
    if file.content_type.startswith("image/"):
        file_path = f"temp/{file.filename}"
        
        os.makedirs("temp", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(file.file.read())

        try:
            result = classify_image(file_path)
            if result == 'normal':
                response_message = "Not Censored"
            else:
                response_message = "Censored"
            return {"result": response_message}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            # Удаляем временный файл после обработки
            os.remove(file_path)
    else:
        raise HTTPException(status_code=400, detail="Invalid file format. Please provide an image file.")
