from fastapi import APIRouter
from src.schema import SimpleResponse
from src.settings import settings

router = APIRouter(prefix='/api')


@router.get('/hello/')
async def hello() -> SimpleResponse:
    '''Return the HELLO_MSG environment variable'''
    msg = settings.HELLO_MSG
    response = SimpleResponse(message=msg)
    return response
