from database.models import Product
# from database.engine import Database
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ProductDal:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_product_by_id(self, product_id) -> list[Product]:
        query = select(Product).where(Product.product_id == product_id)
        res = await self.session.scalars(query)
        product_row = res.fetchall()
        if product_row is not None:
            return product_row

    async def get_product_photo_by_id(self, product_id):
        query = select(Product.product_photo_blob).where(Product.product_id == product_id)
        res = await self.session.scalar(query)
        return res

    async def get_products(self) -> list[Product]:
        query = select(Product)
        res = await self.session.execute(query)
        return res.scalars().all()


