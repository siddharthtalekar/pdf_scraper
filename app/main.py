import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.routes import router

os.environ["GOOGLE_API_KEY"] = "AIzaSyDXaEq7rvGLJLfpF8usnxB4nrD3uUdCjjI"

app = FastAPI()
app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
