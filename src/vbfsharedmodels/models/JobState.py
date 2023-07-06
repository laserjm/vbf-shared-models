from pydantic import BaseModel


class JobState(BaseModel):
    name: str = ""
    message: str = ""