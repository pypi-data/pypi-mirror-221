from getajob.abstractions.repository import (
    MultipleChildrenRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import RecruiterInvitation

entity_models = EntityModels(entity=RecruiterInvitation)


class RecruiterInvitationsRepository(MultipleChildrenRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.RECRUITER_INVITATIONS.value,
                entity_models,
            ),
            required_parent_keys=[Entity.COMPANIES.value],
        )
