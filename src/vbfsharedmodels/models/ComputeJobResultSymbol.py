from typing import Any, List
from pydantic import BaseModel

from vbfsharedmodels.models.JobState import JobState


class ComputeJobResultSymbol(BaseModel):
    symbol: str
    job_state: JobState
    data: Any
