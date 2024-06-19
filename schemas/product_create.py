from pydantic import BaseModel


class ProductCreate(BaseModel):
    product_name: str
    product_description: str
    product_size: str
    product_brand: str
    product_sex: str
    product_category: str
    product_price: int


class BlobCreate(BaseModel):
    product_photo_blob: bytes
