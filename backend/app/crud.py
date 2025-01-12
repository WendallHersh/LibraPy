from sqlalchemy.orm import Session
from app.models import Book, User, Transaction
from app.schemas import BookCreate, UserCreate

# Books
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Users
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Transactions
def create_transaction(db: Session, user_id: int, book_id: int, transaction_type: str):
    transaction = Transaction(user_id=user_id, book_id=book_id, transaction_type=transaction_type)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction
