from typing import Generator, Iterator
from sqlalchemy.orm.session import Session
from domain.contact import ContractRepositoryInterface, Contact


class ContactRepository(ContractRepositoryInterface):
    """
    Implementación del repositorio de contacto
    """

    # TODO: Implementar asincronía

    def __init__(self, session_factory: Generator[Session, None, None]) -> None:
        self.session_factory = session_factory

    def insert(self, contact: Contact) -> Contact:
        with self.session_factory() as session:
            session.add(contact)
            session.commit()
            session.refresh(contact)
            return contact

    def get(self, id: int) -> Contact | None:
        with self.session_factory() as session:
            return session.query(Contact).where(Contact.id == id).first()

    def list(self, page: int = 1, search: str | None = None) -> Iterator[Contact]:
        with self.session_factory() as session:
            query = session.query(Contact)
            if search:
                query = query.filter(Contact.name.ilike(f"%{search}%"))
            return query.offset((page - 1) * 10).limit(10).all()

    def update(self, contact: Contact) -> Contact:
        with self.session_factory() as session:
            session.merge(contact)
            session.commit()
            session.refresh(contact)
            return contact

    def delete(self, id: int) -> None:
        with self.session_factory() as session:
            session.query(Contact).where(Contact.id == id).delete()
            session.commit()
