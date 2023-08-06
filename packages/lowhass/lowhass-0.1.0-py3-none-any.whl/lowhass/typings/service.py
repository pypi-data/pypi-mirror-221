from pydantic import BaseModel
from typing import *

class ServiceField(BaseModel):
    description: Optional[str] = None
    example: Any = None
    selector: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    required: Optional[bool] = None

class Service(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    fields: Optional[Dict[str, ServiceField]] = None
    target: Optional[dict[str, list]] = None

class Domain(BaseModel):
    domain: str
    services: dict[str, Service]