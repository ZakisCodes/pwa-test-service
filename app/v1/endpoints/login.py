from fastapi import APIRouter
from pydantic import BaseModel

class USER(BaseModel):
    UserName: str

router = APIRouter()

@router.get("/login")
async def login_info(UserName: str):
    if UserName=="Zakin":
        output = "Zakin Abdul Rahman"
    else:
        output = "Unknown User"

    return {"message": output}


