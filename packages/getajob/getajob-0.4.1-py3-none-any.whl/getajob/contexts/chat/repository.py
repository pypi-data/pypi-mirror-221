from getajob.abstractions.models import Entity, EntityModels
from getajob.abstractions.repository import (
    ParentRepository,
    RepositoryDependencies,
)
from getajob.contexts.companies.recruiters.repository import RecruiterRepository
from getajob.contexts.applications.repository import ApplicationRepository
from getajob.contexts.users.repository import UserRepository
from getajob.abstractions.models import UserAndDatabaseConnection

from .models import UserCreateChat, Chat
from .unit_of_work import CreateChatUnitOfWork


entity_models = EntityModels(entity=Chat, create=UserCreateChat)


class ChatRepository(ParentRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.CHAT.value,
                entity_models,
            )
        )
        self.request_scope = request_scope

    def create_new_chat(self, create_chat: UserCreateChat):
        return CreateChatUnitOfWork(
            application_repository=ApplicationRepository(self.request_scope),
            recruiter_repository=RecruiterRepository(self.request_scope),
            user_repository=UserRepository(self.request_scope),
            chat_repository=self,
        ).create_new_chat(create_chat)
