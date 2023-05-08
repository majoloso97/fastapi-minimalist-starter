from typing import Optional
from pydantic import BaseModel


class SimpleResponse(BaseModel):
    message: str


class WelcomeRequest(BaseModel):
    first_name: Optional[str] = ''
    last_name: Optional[str] = ''
