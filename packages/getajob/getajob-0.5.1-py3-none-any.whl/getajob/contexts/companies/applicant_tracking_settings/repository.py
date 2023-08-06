from getajob.abstractions.repository import (
    SingleChildRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import SetATSConfig, ATSConfig

entity_models = EntityModels(
    create=SetATSConfig,
    update=SetATSConfig,
    entity=ATSConfig,
)


class CompanyATSConfigRepository(SingleChildRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                user_id=request_scope.initiating_user_id,
                db=request_scope.db,
                collection_name=Entity.COMPANY_ATS_CONFIG.value,
                entity_models=entity_models,
            ),
            required_parent_keys=[Entity.COMPANIES.value],
        )
