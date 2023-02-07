from fastapi import APIRouter, HTTPException
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/home",
    tags=["home"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="templates")

@router.get("")
async def home(request: Request):
    """
    displays the home page
    """
    return templates.TemplateResponse("home.html", {"request": request,"somevar": 2})
