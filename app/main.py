from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# static folder (future use ke liye - css/js/images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def home():
    file_path = "app/templates/index.html"

    # safety check (agar file missing ho to error na aaye)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "index.html not found"}
