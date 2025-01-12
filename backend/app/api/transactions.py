from fastapi import APIRouter

router = APIRouter()

# Temporary placeholder routes
@router.post("/")
async def create_transaction():
    return {"message": "Create a new transaction (borrow/return)"}

@router.get("/{transaction_id}")
async def get_transaction(transaction_id: int):
    return {"message": f"Retrieve transaction with ID {transaction_id}"}
