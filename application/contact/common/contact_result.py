from pydantic import BaseModel
from datetime import datetime
from domain.contact import Contact

class ContactResult(BaseModel):
    """
    Representa el resultado de una operacion que involucra un contacto
    """

    id: int
    name: str
    email: str
    phone_number: str
    create_date: datetime

    model_config = {"from_attributes": True}

    @staticmethod
    def to_domain(contact: "ContactResult") -> Contact:
        """
        Convierte un dto en un dominio
        """
        return Contact(
            id=contact.id,
            name=contact.name,
            email=contact.email,
            phone_number=contact.phone_number,
            create_date=contact.create_date,
        )
    
    @staticmethod
    def from_domain(contact: Contact) -> "ContactResult":
        """
        Convierte un dominio en un dto
        """
        return ContactResult(
            id=contact.id,
            name=contact.name,
            email=contact.email,
            phone_number=contact.phone_number,
            create_date=contact.create_date,
        )