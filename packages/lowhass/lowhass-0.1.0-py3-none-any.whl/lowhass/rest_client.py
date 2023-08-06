from requests import Session, Response
from .typings import *
from typing import *
from .util import HASSException

class HASS_Rest:
    def __init__(self, address: str, token: str) -> None:
        self.address = address
        self.token = token
        self.session = Session()
        self.session.headers["Authorization"] = "Bearer " + token
        self.session.headers["Content-Type"] = "appplication/json"
    
    def url(self, endpoint: str) -> str:
        return f"{self.address}/api{endpoint}"
    
    def handle_exc(self, response: Response) -> Any:
        if response.status_code < 400:
            try:
                return response.json()
            except:
                return response.text
        else:
            raise HASSException(response.status_code, response.reason, response.text)
    
    def api_status(self) -> Status:
        return Status(**self.handle_exc(self.session.get(self.url("/"))))
    
    def get_config(self) -> Config:
        return Config(**self.handle_exc(self.session.get(self.url("/config"))))
    
    def get_events(self) -> list[EventListener]:
        return [EventListener(**e) for e in self.handle_exc(self.session.get("/events"))]

    def get_services(self) -> list[Domain]:
        return [Domain(**d) for d in self.handle_exc(self.session.get(self.url("/services")))]

    def get_states(self) -> list[State]:
        return [State(**s) for s in self.handle_exc(self.session.get(self.url("/states")))]
    
    def get_state(self, entity: str) -> State:
        return State(**self.handle_exc(self.session.get(self.url(f"/states/{entity}"))))
    
    def evaluate_template(self, template: str) -> str:
        return self.handle_exc(self.session.post(self.url("/template"), json={"template": template}))
    
    def call_service(self, domain: str, service: str, data: Optional[dict] = {}) -> list[State]:
        return [State(**s) for s in self.handle_exc(self.session.post(self.url(f"/services/{domain}/{service}"), json=data))]
    