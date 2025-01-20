from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from datetime import timezone
from infrastructure.data.database import Base

"""
    TODO: Encontrar la forma de aislar la entidad de la infraestructura
"""


class Contact(Base):
    """
    Entidad de Contacto
    params:
    - id
    - name
    - email
    - phone_number
    - create_date
    """

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    create_date = Column(DateTime, default=datetime.now(timezone.utc))
