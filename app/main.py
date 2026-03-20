from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def home():
    file_path = "app/templates/index.html"

    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "index.html not found"}
