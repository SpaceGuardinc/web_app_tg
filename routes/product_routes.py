from fastapi import APIRouter, HTTPException, Depends, Request
from typing import List
from schemas.product_create import ProductCreate, BlobCreate
from services.product_service import ProductDal
from sqlalchemy.ext.asyncio import AsyncSession
from database.engine import get_db
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response

router = APIRouter()


@router.get("/product/image/{product_id}")
async def get_product_image(product_id: int, session: AsyncSession = Depends(get_db)):
    product_photo_blob = await ProductDal(session).get_product_photo_by_id(product_id)
    if product_photo_blob:
        return Response(content=product_photo_blob, media_type="image/jpeg")
    else:
        return Response(status_code=404)


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def read_main(request: Request, session: AsyncSession = Depends(get_db)):
    products = await ProductDal(session).get_products()
    print(products)  # Отладочный вывод, чтобы убедиться, что данные получены
    return templates.TemplateResponse("products.html", {"request": request, "products": products})


@router.get("/product/", response_model=List[ProductCreate])
async def read_product(product_id: int, session: AsyncSession = Depends(get_db)):
    return await ProductDal(session).get_product_by_id(product_id)


@router.get("/products/", response_model=List[ProductCreate])
async def read_products(session: AsyncSession = Depends(get_db)):
    return await ProductDal(session).get_products()

# products = [
#     {"id": 1, "name": "Nike"},
#     {"id": 2, "name": "Adidas"},
# ]
#
#
# @router.get("/products/{product_id}")
# async def get_product(product_id: int):
#     return [product for product in products if product.get("id") == product_id]
#
#
# products2 = [
#     {"id": 1, "name": "Nike"},
#     {"id": 2, "name": "Adidas"},
# ]
#
#
# @router.post("/products/{product_id}")
# async def change_product(product_id: int, new_name: str):
#     current_product = list(filter(lambda product: product.get("id") == product_id, products2))[0]
#     current_product["name"] = new_name
#     return {"status": 200, "data": current_product}
