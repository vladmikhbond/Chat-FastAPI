from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from ..data_alch import read_all_items, add_item


templates = Jinja2Templates(directory="chat/templates")

router = APIRouter()

@router.get("/items")
async def get_items(request: Request):
    items = read_all_items()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@router.post("/items")
async def post_items(request: Request):
    form = await request.form()
    message = form.get("message").strip()
    sign = form.get("sign").strip()
    
    if message != '':    
        add_item(message, sign)

    items = read_all_items()
    return templates.TemplateResponse("items.html", {"request": request, "items": items})


@router.get("/freq")
async def get_freq(request: Request):
    items = read_all_items()
    dict = {}
    for item in items:
        n: int = dict.get(item.sign, 0)
        dict[item.sign] = n + 1
    
    return templates.TemplateResponse("freq.html", {"request": request, "dict": dict})

