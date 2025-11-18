from fastapi import APIRouter, Depends, HTTPException, status


order_router = APIRouter(
    prefix="/orders",
    tags = ["Orders"]
)

@order_router.get("/")
async def hello():
    return {"message": "Hello from orders router"}