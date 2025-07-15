import json, os
from .models import Item

# файл має знаходитися в кореневому каталозі пакета
DATA_FILE = os.path.join(os.path.dirname(__file__), "items.json")

def read_all() -> list[Item]:
    with open(DATA_FILE, "r") as f:
        return [Item(**item) for item in json.load(f)]

                  
def write_all(items: list[Item]):
    with open(DATA_FILE, "w") as f:
        json.dump([item.__dict__ for item in items], f, ensure_ascii=False, indent=4)


def do_test_db():
    """ Виготовлення тестових даних"""
    return [Item(message=s*4, sign=s, datetime="2025-07-11") for s in ["aaa", "bbb", "ccc"]]

