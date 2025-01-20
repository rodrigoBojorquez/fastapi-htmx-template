"""
Excepciones relacionadas a la entidad Contact.

Reflejan las reglas de negocio de la entidad Contact.
"""


class ContactNotFoundError(Exception):
    """
    Ocurre cuando no se encuentra un Contact.
    """

    message = "Contact not found"

    def __str__(self):
        return ContactNotFoundError.message
