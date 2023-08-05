from getajob.vendor.firestore.repository import FirestoreDB
from getajob.abstractions.repository import ParentRepository, RepositoryDependencies
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection
from .models import User


entity_models = EntityModels(entity=User)


class UserRepository(ParentRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.USERS.value,
                entity_models,
            )
        )

    def get_user(self, id: str):
        return super().get(id)

    @staticmethod
    def get_email_from_user(user: User):
        return [
            email
            for email in user.email_addresses
            if email.id == user.primary_email_address_id
        ][0].email_address
