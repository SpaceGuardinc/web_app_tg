from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/")
async def read_main():
    return "Hi"


# @router.get("/", response_class=HTMLResponse)
# async def read_main():
#     with open("D:/web_app_shop_tg/templates/index.html", encoding="utf-8") as f:
#         html_content = f.read()
#     return html_content
