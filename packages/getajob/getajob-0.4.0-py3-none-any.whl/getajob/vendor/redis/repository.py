import json
from typing import Type
from pydantic import BaseModel
from redis import Redis

from getajob.abstractions.models import Entity

from .client_factory import RedisFactory


class RedisRepository:
    def __init__(self, client: Redis = RedisFactory.get_client()):
        self.client = client

    def _get_cached_id(self, entity: Entity, entity_id: str) -> str:
        return f"{entity.value}:{entity_id}"

    def _convert_to_json(
        self, data: str | int | BaseModel | dict | list[BaseModel] | list[dict]
    ) -> str | int:
        if isinstance(
            data,
            (
                str,
                int,
            ),
        ):
            return data
        if isinstance(data, dict):
            return json.dumps(data)
        if isinstance(data, BaseModel):
            return data.json()
        if isinstance(data, list):
            object_as_list_of_dicts = []
            for item in data:
                if isinstance(item, BaseModel):
                    object_as_list_of_dicts.append(item.dict())
                else:
                    object_as_list_of_dicts.append(item)
        return json.dumps(object_as_list_of_dicts)

    def set(
        self,
        entity: Entity,
        entity_id: str,
        data: str | int | BaseModel | dict | list[BaseModel] | list[dict] | None,
    ):
        if not data:
            return
        self.client.set(
            self._get_cached_id(entity, entity_id), self._convert_to_json(data)
        )

    def get(
        self, entity: Entity, entity_id: str, model: Type[BaseModel] | None = None
    ) -> BaseModel | dict | str | int | list | None:
        res = self.client.get(self._get_cached_id(entity, entity_id))
        if not res:
            return None
        if isinstance(res, int):
            return res
        try:
            loaded_res = json.loads(res)
        except json.decoder.JSONDecodeError:
            return res
        if not model:
            return loaded_res
        if isinstance(loaded_res, list):
            return [model(**item) for item in loaded_res]
        return model(**loaded_res)
