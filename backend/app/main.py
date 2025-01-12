from fastapi import FastAPI
from app.api import books, users, transactions

app = FastAPI(title="LibraPy: Library Catalog System")

# Include API routers
app.include_router(books.router, prefix="/api/books", tags=["Books"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(transactions.router, prefix="/api/transactions", tags=["Transactions"])

@app.get("/")
async def root():
    return {"message": "Welcome to LibraPy!"}
