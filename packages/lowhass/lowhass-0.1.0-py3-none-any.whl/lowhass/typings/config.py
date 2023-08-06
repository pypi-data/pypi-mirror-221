from pydantic import BaseModel
from typing import Union

class ConfigUnits(BaseModel):
    length: str
    accumulated_precipitation: str
    mass: str
    pressure: str
    temperature: str
    volume: str
    wind_speed: str

class Config(BaseModel):
    latitude: float
    longitude: float
    elevation: float
    unit_system: ConfigUnits
    location_name: str
    time_zone: str
    components: list[str]
    config_dir: str
    whitelist_external_dirs: list[str]
    allowlist_external_dirs: list[str]
    allowlist_external_urls: list[str]
    version: str
    config_source: str
    safe_mode: bool
    state: str
    external_url: Union[str, None]
    internal_url: Union[str, None]
    currency: str
    country: str
    language: str

    

