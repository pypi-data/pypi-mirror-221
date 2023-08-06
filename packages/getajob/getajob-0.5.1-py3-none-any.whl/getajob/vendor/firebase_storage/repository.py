from google.cloud.firestore_v1.client import Client

from firebase_admin import storage

from .client_factory import FirebaseStorageClientFactory


class FirebaseStorageRepository:
    def __init__(self, client: Client = FirebaseStorageClientFactory.get_client()):
        self._client = client
        self._bucket = storage.bucket(app=self._client)

    def upload_bytes(self, file_bytes: bytes, remote_file_path: str) -> str:
        blob = self._bucket.blob(remote_file_path)
        blob.upload_from_string(file_bytes)
        return blob.public_url

    def upload_file(self, local_file_path, remote_file_path) -> str:
        blob = self._bucket.blob(remote_file_path)
        blob.upload_from_filename(local_file_path)
        return blob.public_url

    def download_to_file(self, remote_file_path, local_file_path) -> None:
        blob = self._bucket.blob(remote_file_path)
        blob.download_to_filename(local_file_path)

    def get_file_bytes(self, remote_file_path) -> bytes:
        blob = self._bucket.blob(remote_file_path)
        return blob.download_as_bytes()

    def delete_file(self, remote_file_path) -> None:
        blob = self._bucket.blob(remote_file_path)
        blob.delete()
