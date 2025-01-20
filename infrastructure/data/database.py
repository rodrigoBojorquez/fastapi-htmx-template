from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from typing import Generator
from sqlalchemy.orm.session import Session
import logging

logger = logging.getLogger(__name__)
Base = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        )

    def create_database(self) -> None:
        Base.metadata.create_all(bind=self._engine)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session: Session = self._session_factory()

        try:
            yield session

        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise

        finally:
            session.close()
