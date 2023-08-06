from .rest_client import HASS_Rest
from .ws_client import HASS_WS

class HASS:
    def __init__(self, address: str, token: str):
        self.address = address
        self.token = token
        self.rest = HASS_Rest(address, token)
        self.ws = HASS_WS(address, token)

VERSION = "0.1.0"