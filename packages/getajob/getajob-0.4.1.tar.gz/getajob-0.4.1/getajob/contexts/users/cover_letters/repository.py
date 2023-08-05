from getajob.vendor.firestore.repository import FirestoreDB
from getajob.abstractions.repository import (
    MultipleChildrenRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import CoverLetter, CreateCoverLetter, UpdateCoverLetter

entity_models = EntityModels(
    entity=CoverLetter,
    create=CreateCoverLetter,
    update=UpdateCoverLetter,
)


class CoverLetterRepository(MultipleChildrenRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.COVER_LETTERS.value,
                entity_models,
            ),
            required_parent_keys=[Entity.USERS.value],
        )
