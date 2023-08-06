class HASSException(Exception):
    def __init__(self, status_code: int, status_text: str, error_data: str, *args: object) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.status_text = status_text
        self.error_data = error_data
    
    def __str__(self) -> str:
        return f"HASS Error {self.status_code} ({self.status_text}): {self.error_data}\n\t{super().__str__()}"