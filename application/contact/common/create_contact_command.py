from pydantic import BaseModel


class CreateContactRequest(BaseModel):
    """
    CreateContactRequest is a pydantic model that represents the request body for creating a contact.
    """

    name: str
    email: str | None = None
    phone_number: str
