from algoliasearch.search_client import SearchClient

from .client_factory import AlgoliaClientFactory
from .models import AlgoliaIndex, AlgoliaSearchParams, AlgoliaSearchResults


class AlgoliaSearchRepository:
    def __init__(
        self,
        index_name: AlgoliaIndex,
        client: SearchClient = AlgoliaClientFactory().get_client(),
    ):  # type: ignore
        self.index = client.init_index(index_name.value)

    def search(self, query: AlgoliaSearchParams):
        search_params = {
            "query": query.query,
            "page": query.page,
            "hitsPerPage": query.hits_per_page,
        }
        if query.filters:
            search_params["filters"] = query.filters
        if query.facet_filters:
            search_params["facetFilters"] = query.facet_filters
        if query.attributes_to_retrieve:
            search_params["attributesToRetrieve"] = query.attributes_to_retrieve
        res = self.index.search(query.query, search_params)
        return AlgoliaSearchResults(**res)

    def get_object(self, object_id: str):
        return self.index.get_object(object_id)

    def create_object(self, object_id: str, object_data: dict):
        object_data["objectID"] = object_id
        return self.index.save_object(object_data)

    def update_object(self, object_id: str, object_data: dict):
        object_data["objectID"] = object_id
        return self.index.partial_update_object(object_data)

    def replace_all_objects(self, objects: list[dict]):
        return self.index.replace_all_objects(objects)

    # For now we are using soft delete for these search databases so this method is unavailable
    # def delete_object(self, object_id: str):
    #     return self.index.delete_object(object_id)
