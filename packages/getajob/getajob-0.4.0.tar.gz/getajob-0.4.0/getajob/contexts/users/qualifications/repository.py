from getajob.vendor.firestore.repository import FirestoreDB
from getajob.abstractions.repository import (
    SingleChildRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import Qualifications, UserQualifications


entity_models = EntityModels(
    entity=UserQualifications,
    create=Qualifications,
    update=Qualifications,
)


class UserQualificationsRepository(SingleChildRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.USER_QUALIFICATIONS.value,
                entity_models,
            ),
            required_parent_keys=[Entity.USERS.value],
        )
