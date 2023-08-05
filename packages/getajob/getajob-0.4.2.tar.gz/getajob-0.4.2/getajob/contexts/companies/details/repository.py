from getajob.abstractions.repository import (
    SingleChildRepository,
    RepositoryDependencies,
)
from getajob.abstractions.models import Entity, EntityModels, UserAndDatabaseConnection

from .models import CreateCompanyDetails, CompanyDetails

entity_models = EntityModels(
    create=CreateCompanyDetails,
    update=CreateCompanyDetails,
    entity=CompanyDetails,
)


class CompanyDetailsRepository(SingleChildRepository):
    def __init__(self, request_scope: UserAndDatabaseConnection):
        super().__init__(
            RepositoryDependencies(
                request_scope.initiating_user_id,
                request_scope.db,
                Entity.COMPANY_DETAILS.value,
                entity_models,
            ),
            required_parent_keys=[Entity.COMPANIES.value],
        )
