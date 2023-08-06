from typing import Any, Optional
from pydantic import BaseModel
import datetime


class State(BaseModel):
    entity_id: str
    state: str
    attributes: dict[str, Any]
    last_changed: datetime.datetime
    last_updated: Optional[datetime.datetime] = None