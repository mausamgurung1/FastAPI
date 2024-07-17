from pydantic import BaseModel


class Blog(BaseModel):
    titel: str
    body: str