from algoliasearch.search_client import SearchClient, SearchIndex
from .models import AlgoliaSearchResults


class MockAlgoliaIndex(SearchIndex):
    # pylint: disable=super-init-not-called
    def __init__(self, *args, **kwargs):
        self.local_items = {}

    def search(self, *args, **kwargs):
        return AlgoliaSearchResults(
            hits=list(self.local_items.values()),
            nbHits=0,
            page=0,
            nbPages=0,
            hitsPerPage=0,
            processingTimeMS=0,
            exhaustiveNbHits=False,
            query="",
            params="",
        ).dict()

    def get_object(self, object_id: str, request_options=None):
        return self.local_items[object_id]

    def save_object(self, obj: dict, request_options=None):
        self.local_items[obj["objectID"]] = obj

    def partial_update_object(self, obj: dict, request_options=None):
        self.local_items[obj["objectID"]] = obj

    def delete_object(self, object_id: str, request_options=None):
        del self.local_items[object_id]


class MockAlgoliaClient(SearchClient):
    # pylint: disable=super-init-not-called
    def __init__(self, *args, **kwargs):
        ...

    def init_index(self, *args, **kwargs):
        return MockAlgoliaIndex()
