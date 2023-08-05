import typing as t
from getajob.vendor.kafka.repository import KafkaProducerRepository
from getajob.vendor.kafka.models import KafkaEventConfig, KafkaTopic
from getajob.abstractions.repository import (
    MultipleChildrenRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import CreateJob, UpdateJob, Job, UserCreateJob
from .unit_of_work import JobsUnitOfWork


entity_models = EntityModels(entity=Job, create=CreateJob, update=UpdateJob)


class JobsRepository(MultipleChildrenRepository):
    def __init__(
        self,
        request_scope: UserAndDatabaseConnection,
        kafka: t.Optional[KafkaProducerRepository] = None,
    ):
        kafka_event_config = KafkaEventConfig(
            topic=KafkaTopic.jobs, create=True, update=True, delete=True, get=True
        )
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.JOBS.value,
                entity_models,
                kafka,
                kafka_event_config,
            ),
            required_parent_keys=[Entity.COMPANIES.value],
        )

    def create_job(self, company_id: str, job: UserCreateJob):
        return JobsUnitOfWork(self).create_job(company_id, job)
