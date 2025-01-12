from fastapi import APIRouter

router = APIRouter()

# Temporary placeholder routes
@router.post("/")
async def create_user():
    return {"message": "Register a new user"}

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Retrieve user with ID {user_id}"}
