from dependency_injector import containers, providers
from infrastructure.data import Database
from infrastructure.repositories import ContactRepository
from application.contact.services import ContactService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["presentation", "infrastructure", "application"]
    )
    config = providers.Configuration(json_files=["config.json"], strict=True)

    db = providers.Singleton(Database, db_url=config.database.url)

    # REPOSITORIES
    contact_repository = providers.Factory(
        ContactRepository, session_factory=db.provided.session
    )

    # SERVICES
    contact_service = providers.Factory(
        ContactService, contact_repository=contact_repository
    )
