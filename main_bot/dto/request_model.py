from pydantic import BaseModel

class RequestSchema(BaseModel):
    user_tg_id : str
    message : str
    answer : str