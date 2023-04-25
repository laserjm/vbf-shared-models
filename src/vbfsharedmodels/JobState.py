from enum import Enum
from pydantic import BaseModel

class JobStateNames(str, Enum):
    queued = "queued"
    accepted = "accepted"
    finished = "finished"
    error = "error"

class JobState(BaseModel):
    name: str = ""
    message: str = ""