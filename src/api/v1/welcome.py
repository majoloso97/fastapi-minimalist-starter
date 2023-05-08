from fastapi import APIRouter
from src.schema import WelcomeRequest, SimpleResponse
from src.settings import settings

router = APIRouter(prefix='/api/v1')


@router.post('/welcome/')
async def welcome(request: WelcomeRequest = None) -> SimpleResponse:
    msg = settings.WELCOME_TEMPLATE
    name = ''
    if request.first_name:
        name += f' {request.first_name}'
    
    if request.last_name:
        name += f' {request.last_name}'
    return SimpleResponse(message=msg.format(name))
