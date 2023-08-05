from typing import Any
from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class DataModelAndFunction(BaseModel):
    model: Any  # BaseModel
    function: Any  # Callable


class KafkaTopic(str, Enum):
    users = "users"
    jobs = "jobs"
    companies = "companies"
    recruiters = "recruiters"
    recruiters_invitations = "recruiters_invitations"
    applications = "applications"
    candidates = "candidates"
    notifications = "notifications"
    communications = "communications"
    chat = "chat"

    @classmethod
    def get_all_topics(cls):
        return [topic.value for topic in cls]


class KafkaEventConfig(BaseModel):
    topic: KafkaTopic
    get: bool = False
    create: bool = False
    update: bool = False
    delete: bool = False


class KafkaEventType(str, Enum):
    create = "create"
    update = "update"
    delete = "delete"
    get = "get"


class BaseKafkaMessage(BaseModel):
    object_id: str
    requesting_user_id: str
    message_type: str  # This is any of the enum values below, handled by consumer
    company_id: str | None = None
    message_time: datetime = datetime.now()
    data: dict[str, Any] | None = None


class KafkaJobsEnum(str, Enum):
    create_jobs = "create_jobs"
    update_jobs = "update_jobs"
    delete_jobs = "delete_jobs"
    get_jobs = "get_jobs"


class KafkaApplicationsEnum(str, Enum):
    create_applications = "create_applications"
    update_applications = "update_applications"
    delete_applications = "delete_applications"
    get_applications = "get_applications"


class KafkaChatEnum(str, Enum):
    user_create_chat_message = "user_create_chat_message"
    user_update_chat_message = "user_update_chat_message"
    incoming_chat_email = "incoming_chat_email"


class KafkaAuditEnum(str, Enum):
    create_audit = "create_audit"
