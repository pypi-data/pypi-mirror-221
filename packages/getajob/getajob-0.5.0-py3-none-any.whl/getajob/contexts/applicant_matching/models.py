"""
This module handles scoring all current applicants for a position as well as
candidants that haven't applied yet based on the job requirements.

ML go here

We want all applications to go into Algolia

When an application is submitted it should go through the matching algorithm
So that the stored Algolia value HAS the scored value

Then we can open applicant searching with Algolia to the user instead of 
that gnarly BS you just did

You can stored the user information at the time of submission too
and if the user is detected that they update their information relevant to a job (like most recent job)
you can search and update algolia in the backend to refresh this data

Make sure to store that this data was updated and have an original copy in database that can be queried



"""


from pydantic import BaseModel

from getajob.abstractions.models import BaseDataModel
from getajob.contexts.applications.models import Application
from getajob.contexts.users.details.models import UserDetails


class CreateCandidateScore(BaseModel):
    user_id: str
    application_id: str
    job_id: str
    company_id: str
    score: float
    explanation: dict[str, float]


class CandidateScore(BaseDataModel, CreateCandidateScore):
    ...


class ApplicationAndUserDetails(BaseModel):
    application: Application
    user_details: UserDetails
