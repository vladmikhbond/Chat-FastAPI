# створення і налаштування об'єкта додатку app

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from .data_alch import do_test_db
from .routers import items_router


app = FastAPI()

# папки static і templates повинні знаходитися в кореневому каталозі пакета
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(items_router.router, prefix="", tags=["auth"])

do_test_db()