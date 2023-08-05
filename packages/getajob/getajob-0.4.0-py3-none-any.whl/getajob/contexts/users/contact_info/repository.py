from getajob.abstractions.repository import (
    SingleChildRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import (
    UserContactInformation,
    ContactInformation,
)


entity_models = EntityModels(
    entity=UserContactInformation,
    create=ContactInformation,
)


class ContactInformationRepository(SingleChildRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.USER_CONTACT_INFORMATION.value,
                entity_models,
            ),
            required_parent_keys=[Entity.USERS.value],
        )
