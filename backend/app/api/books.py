from fastapi import APIRouter, HTTPException
from app.schemas import Book
from app.crud import add_book, get_book

router = APIRouter()

@router.post("/")
async def create_book(book: Book):
    return await add_book(book)

@router.get("/{book_id}")
async def read_book(book_id: int):
    book = await get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
