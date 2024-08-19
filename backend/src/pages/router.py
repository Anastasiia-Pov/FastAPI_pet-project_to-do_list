from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/pages',
    tags=["Pages"]
)

templates = Jinja2Templates(directory='templates')


@router.get('/base')
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {'request': request})


@router.get('/login')
def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {'request': request})


@router.get('/board')
def get_board_page(request: Request):
    return templates.TemplateResponse("board.html", {'request': request})
