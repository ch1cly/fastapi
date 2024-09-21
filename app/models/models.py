from pydantic import BaseModel

class User(BaseModel):
    username: str
    message: str
    id: int


class User1(BaseModel):
    username: str
    age: int

class Feedback(BaseModel):
    username: str
    fb_message: str