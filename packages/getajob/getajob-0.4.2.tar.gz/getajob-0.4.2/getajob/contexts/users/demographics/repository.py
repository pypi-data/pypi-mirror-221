from getajob.vendor.firestore.repository import FirestoreDB
from getajob.abstractions.repository import (
    SingleChildRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import UserDemographicData, DemographicData


entity_models = EntityModels(
    entity=UserDemographicData,
    create=DemographicData,
    update=DemographicData,
)


class UserDemographicsRepository(SingleChildRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.USER_DEMOGRAPHICS.value,
                entity_models,
            ),
            required_parent_keys=[Entity.USERS.value],
        )
