from google.cloud.firestore_v1.client import Client


class MockFirebaseStorageClient(Client):
    # pylint: disable=super-init-not-called
    def __init__(self, *args, **kwargs):
        ...
