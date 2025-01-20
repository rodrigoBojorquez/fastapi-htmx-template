from abc import ABC, abstractmethod


class ContractRepositoryInterface(ABC):
    """
    Interfaz de repository de contactos
    """

    @abstractmethod
    def insert(self, contact):
        """
        Agrega un contacto
        """
        raise NotImplementedError

    @abstractmethod
    def list(self, page: int, search: str):
        """
        Obtiene todos los contactos
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int):
        """
        Elimina un contacto
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, contact):
        """
        Actualiza un contacto
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int):
        """
        Obtiene un contacto
        """
        raise NotImplementedError
