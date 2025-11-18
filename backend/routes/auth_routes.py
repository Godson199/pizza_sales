from fastapi import APIRouter, Depends, HTTPException, status


auth_router = APIRouter(
    prefix="/auth",
    tags = ["auth"]
)

@auth_router.get("/")
async def hello():
    return {"message": "Hello from auth router"}