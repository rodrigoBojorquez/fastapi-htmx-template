from pydantic import BaseModel


class ListContactsQuery(BaseModel):
    page: int
    search: str | None = None
