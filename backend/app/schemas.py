from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    published_date: Optional[datetime] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    user_id: int
    book_id: int
    transaction_type: str  # e.g., "borrow" or "return"

class Transaction(TransactionBase):
    id: int
    transaction_date: datetime

    class Config:
        orm_mode = True
