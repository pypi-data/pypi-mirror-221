import typing as t

from getajob.vendor.kafka.repository import KafkaProducerRepository
from getajob.vendor.kafka.models import KafkaEventConfig, KafkaTopic
from getajob.abstractions.repository import ParentRepository, RepositoryDependencies
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import (
    ClerkUser,
    ClerkUserWebhookEvent,
    ClerkUserWebhookType,
    ClerkWebhookUserDeleted,
    ClerkWebhookUserUpdated,
)

entity_models = EntityModels(entity=ClerkUser, update=ClerkWebhookUserUpdated)


class WebhookUserRepository(ParentRepository):
    def __init__(
        self,
        request_scope: UserAndDatabaseConnection,
        kafka: t.Optional[KafkaProducerRepository] = None,
    ):
        kafka_event_config = KafkaEventConfig(
            topic=KafkaTopic.users,
            create=True,
            update=True,
            delete=True,
        )
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.USERS.value,
                entity_models,
                kafka,
                kafka_event_config,
            )
        )

    def handle_webhook_event(self, event: ClerkUserWebhookEvent):
        event_dict = {
            ClerkUserWebhookType.user_created: self.create_user,
            ClerkUserWebhookType.user_updated: self.update_user,
            ClerkUserWebhookType.user_deleted: self.delete_user,
        }
        return event_dict[event.type](event)

    def create_user(self, event: ClerkUserWebhookEvent):
        create_event = ClerkUser(**event.data)
        return self.create(data=create_event, provided_id=create_event.id)

    def update_user(self, event: ClerkUserWebhookEvent):
        update_event = ClerkWebhookUserUpdated(**event.data)
        return self.update(doc_id=update_event.id, data=update_event)

    def delete_user(self, event: ClerkUserWebhookEvent):
        delete_event = ClerkWebhookUserDeleted(**event.data)
        return self.delete(doc_id=delete_event.id)
