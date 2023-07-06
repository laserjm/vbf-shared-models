from typing import Any, List
from pydantic import BaseModel

from vbfsharedmodels.models.ComputeJobResultSymbol import ComputeJobResultSymbol


class ComputeJobResultV2(BaseModel):
    model_type: str
    symbols: List[ComputeJobResultSymbol]
