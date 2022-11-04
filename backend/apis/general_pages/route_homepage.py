#route_homepage.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()

#end point or index page
@general_pages_router.get("/")
async def index(request: Request):
	return templates.TemplateResponse("general_pages/index.html",{"request":request})

#endpoint for home page
@general_pages_router.get("/home")
async def home(request: Request):
	return templates.TemplateResponse("general_pages/homepage.html",{"request":request})
	