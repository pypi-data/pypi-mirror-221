from pydantic import BaseModel


class EventListener(BaseModel):
    event: str
    listener_count: int