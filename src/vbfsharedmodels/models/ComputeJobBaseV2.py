from typing import Optional
from pydantic import BaseModel

from vbfsharedmodels.models.ComputeJobContext import ComputeJobContext
from vbfsharedmodels.models.ComputeJobResultV2 import ComputeJobResultV2
from vbfsharedmodels.models.JobState import JobState


class ComputeJobBaseV2(BaseModel):
    version: int = 3
    start_date_time: str
    # end_date_time: str
    compute_job_context: ComputeJobContext
    # job_state: JobState
    # file_name: str
    user_id: str
    compute_job_result: Optional[ComputeJobResultV2]
