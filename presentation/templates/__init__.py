from typing import Any
from fastapi import Request
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone 

def datetime_context(request: Request) -> dict[str, Any]:
    return {"datetime": datetime}

templates = Jinja2Templates(directory="presentation/templates", context_processors=[
    datetime_context
])
