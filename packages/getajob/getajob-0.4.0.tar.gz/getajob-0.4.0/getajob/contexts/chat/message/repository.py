from getajob.abstractions.models import Entity, EntityModels
from getajob.abstractions.repository import (
    MultipleChildrenRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import UserAndDatabaseConnection

from .models import UserCreateChatMessage, UpdateChatMessage, ChatMessage


entity_models = EntityModels(
    entity=ChatMessage, create=UserCreateChatMessage, update=UpdateChatMessage
)


class ChatMessageRepository(MultipleChildrenRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.CHAT_MESSAGES.value,
                entity_models,
            ),
            required_parent_keys=[Entity.CHAT.value],
        )
