import typing as t

from getajob.vendor.kafka.repository import KafkaProducerRepository
from getajob.vendor.kafka.models import KafkaEventConfig, KafkaTopic
from getajob.abstractions.repository import ParentRepository, RepositoryDependencies
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import (
    ClerkCompanyWebhookEvent,
    ClerkCompany,
    ClerkCompanyDeleted,
    ClerkCompanyWebhookType,
)

entity_models = EntityModels(entity=ClerkCompany)


class WebhookCompanyRepository(ParentRepository):
    def __init__(
        self,
        request_scope: UserAndDatabaseConnection,
        kafka: t.Optional[KafkaProducerRepository] = None,
    ):
        kafka_event_config = KafkaEventConfig(
            topic=KafkaTopic.companies,
            create=True,
            update=True,
            delete=True,
        )
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.COMPANIES.value,
                entity_models,
                kafka,
                kafka_event_config,
            )
        )

    def handle_webhook_event(self, event: ClerkCompanyWebhookEvent):
        event_dict = {
            ClerkCompanyWebhookType.organization_created: self.create_company,
            ClerkCompanyWebhookType.organization_updated: self.update_company,
            ClerkCompanyWebhookType.organization_deleted: self.delete_company,
        }
        return event_dict[event.type](event)

    def create_company(self, event: ClerkCompanyWebhookEvent):
        create_event = ClerkCompany(**event.data)
        return self.create(data=create_event, provided_id=create_event.id)

    def delete_company(self, event: ClerkCompanyWebhookEvent):
        delete_event = ClerkCompanyDeleted(**event.data)
        return self.delete(doc_id=delete_event.id)

    def update_company(self, event: ClerkCompanyWebhookEvent):
        update_event = ClerkCompany(**event.data)
        return self.update(doc_id=update_event.id, data=update_event)
