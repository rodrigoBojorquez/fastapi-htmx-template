from infrastructure.repositories import ContactRepository
from ..common import CreateContactRequest, ContactResult
from domain.contact import Contact, ContactNotFoundError


class ContactService:
    def __init__(self, contact_repository: ContactRepository):
        self._contact_repository = contact_repository

    def add_contact(self, request: CreateContactRequest) -> ContactResult:
        contact = Contact(
            name=request.name,
            email=request.email,
            phone_number=request.phone_number,
        )

        result = self._contact_repository.insert(contact)
        return ContactResult(**result.__dict__)

    def update_contact(
        self, contact_id: int, request: CreateContactRequest
    ) -> ContactResult:
        contact = self._contact_repository.get_by_id(contact_id)

        if not contact:
            return ContactNotFoundError()

        contact.name = request.name
        contact.email = request.email
        contact.phone = request.phone

        result = self._contact_repository.update(contact)
        return ContactResult(**result.__dict__)

    def list(self, page: int = 1, search: str = None) -> tuple[ContactResult]:
        contacts = self._contact_repository.list(page, search)

        return tuple(ContactResult(**contact.__dict__) for contact in contacts)

    def get_contact(self, contact_id: int) -> ContactResult:
        contact = self._contact_repository.get(contact_id)

        if not contact:
            return ContactNotFoundError()

        return ContactResult(**contact.__dict__)
    
    def delete_contact(self, contact_id: int) -> None:
        contact = self._contact_repository.get(contact_id)

        if not contact:
            return ContactNotFoundError()

        self._contact_repository.delete(contact_id) 
