from getajob.abstractions.repository import (
    MultipleChildrenRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import Recruiter

entity_models = EntityModels(entity=Recruiter)


class RecruiterRepository(MultipleChildrenRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.RECRUITERS.value,
                entity_models,
            ),
            required_parent_keys=[Entity.COMPANIES.value],
        )
