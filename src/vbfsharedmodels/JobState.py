from enum import Enum
from pydantic import BaseModel

class JobState(BaseModel):
    name: str = ""
    message: str = ""