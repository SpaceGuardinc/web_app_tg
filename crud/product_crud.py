from typing import List, Type

from sqlalchemy.orm import Session
from database.models import Product
from schemas.product_create import ProductCreate


async def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def get_product(db: Session, product_id: int) -> Type[Product] | None:
    return db.query(Product).filter(Product.product_id == product_id).first()


async def get_products(db: Session, skip: int = 0, limit: int = 10) -> list[Type[Product]]:
    return db.query(Product).offset(skip).limit(limit).all()


async def update_product(db: Session, product_id: int, product: ProductCreate) -> Product:
    db_product = await get_product(db, product_id)
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)


async def delete_product(db: Session, product_id: int) -> Type[Product] | None:
    db_product = await get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        await db.commit()
        return db_product
    return None
