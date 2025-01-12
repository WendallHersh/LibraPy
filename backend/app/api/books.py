from fastapi import APIRouter

router = APIRouter()

# Temporary placeholder routes
@router.get("/")
async def list_books():
    return {"message": "List all books"}

@router.post("/")
async def create_book():
    return {"message": "Create a new book"}

@router.get("/{book_id}")
async def get_book(book_id: int):
    return {"message": f"Retrieve book with ID {book_id}"}

@router.put("/{book_id}")
async def update_book(book_id: int):
    return {"message": f"Update book with ID {book_id}"}

@router.delete("/{book_id}")
async def delete_book(book_id: int):
    return {"message": f"Delete book with ID {book_id}"}
