"""
Define the stages and data that are used across all applicant tracking for a company's given ATS
"""


from pydantic import BaseModel

from getajob.abstractions.models import BaseDataModel


class SetATSConfig(BaseModel):
    available_statuses_and_order: dict[int, str]


class ATSConfig(SetATSConfig, BaseDataModel):
    ...
