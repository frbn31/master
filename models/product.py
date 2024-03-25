from sqlmodel import Field, SQLModel
from typing import Optional, Any, Self, Type

class ProductCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    code: str
    category_id: int | None = Field(default=None, foreign_key="productcategory.id")