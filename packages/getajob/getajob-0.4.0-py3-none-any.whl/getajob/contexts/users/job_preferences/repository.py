from getajob.abstractions.repository import (
    SingleChildRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import UserJobPreferences, JobPreferences


entity_models = EntityModels(
    entity=UserJobPreferences,
    create=JobPreferences,
    update=JobPreferences,
)


class UserJobPreferencesRepository(SingleChildRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.USER_JOB_PREFERENCES.value,
                entity_models,
            ),
            required_parent_keys=[Entity.USERS.value],
        )
