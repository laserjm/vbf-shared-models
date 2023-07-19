from typing import Optional
from pydantic import BaseModel

from vbfsharedmodels.models.ComputeJobContext import ComputeJobContext
from vbfsharedmodels.models.ComputeJobResultV2 import ComputeJobResultV2
from vbfsharedmodels.models.JobStateCountdown import JobStateCountdown


class ComputeJobBaseV2(BaseModel):
    version: int = 3
    start_date_time: str
    end_date_time: Optional[str]
    compute_job_context: ComputeJobContext
    job_state: Optional[JobStateCountdown]
    user_id: str
    compute_job_result: Optional[ComputeJobResultV2]
