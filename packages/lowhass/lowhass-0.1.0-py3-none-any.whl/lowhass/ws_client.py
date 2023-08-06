from websockets import client, exceptions
import json
from .util import HASSException
import time
import random

class HASS_WS:
    def __init__(self, address: str, token: str) -> None:
        self.ws_addr = ("wss://" if address.startswith("https://") else "ws://") + address.split("://")[1] + "/api/websocket"
        self.token = token
        self.handlers = []
        self.handler_function_map = {}

    def handler_events(self, data: dict):
        if data["type"] == "event":
            if data["event"]["event_type"] == "state_changed":
                eid = data["event"]["data"]["entity_id"]
                for h in self.handlers:
                    if h["type"] == "entity" and eid in h["entities"]:
                        h["function"](data["event"])
                    elif h["type"] == "event" and h["event"] == "state_changed":
                        h["function"](data["event"])
            else:
                for h in self.handlers:
                    if h["type"] == "event" and h["event"] == data["event"]["event_type"]:
                        h["function"](data["event"])

    def handler_triggers(self, data: dict):
        if data["type"] == "event":
            for h in self.handlers:
                if h["type"] == "trigger" and h["id"] == data["id"]:
                    h["function"](data["event"])
    
    async def run(self):
        async for websocket in client.connect(self.ws_addr, open_timeout=5):
            idc = 0
            try:
                await websocket.send(json.dumps({'type': 'auth','access_token': self.token}))
                await websocket.send(json.dumps({'id': (idc := idc + 1), 'type': 'subscribe_events', 'event_type': 'state_changed'}))
                self.handler_function_map[idc] = self.handler_events
                for handler in self.handlers:
                    if handler["type"] == "event" and handler["event"] != "state_changed":
                        await websocket.send(json.dumps({'id': (idc := idc + 1), 'type': 'subscribe_events', 'event_type': 'state_changed'}))
                        self.handler_function_map[idc] = self.handler_events
                    if handler["type"] == "trigger":
                        await websocket.send(json.dumps({'id': handler["id"], 'type': 'subscribe_trigger', 'event_type': 'state_changed'}))
                        self.handler_function_map[handler["id"]] = self.handler_triggers
                while True:
                    message = await websocket.recv()
                    try:
                        decoded = json.loads(message)
                        self.handler_function_map[decoded["id"]](decoded)
                    except:
                        pass
            except KeyboardInterrupt:
                break
            except exceptions.ConnectionClosedOK:
                break
            except exceptions.ConnectionClosedError:
                continue
            except Exception as e:
                raise HASSException(0, "WS ERROR", str(e))

    def handle_event(self, event: str):
        def decorator_handle(func):
            self.handlers.append({
                "type": "event",
                "event": event,
                "function": func
            })
            return func
        return decorator_handle
    
    def handle_entity_update(self, entities: list[str]):
        def decorator_handle(func):
            self.handlers.append({
                "type": "entity",
                "entities": entities,
                "function": func
            })
            return func
        return decorator_handle
    
    def handle_trigger(self, trigger: dict):
        def decorator_handle(func):
            self.handlers.append({
                "type": "trigger",
                "trigger": trigger,
                "function": func,
                "id": round(time.time()) + random.randint(-50000, 50000)
            })
            return func
        return decorator_handle