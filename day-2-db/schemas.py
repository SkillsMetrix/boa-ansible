from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    uname:str
    email:str
    city: Optional[str]=None