from typing import Optional
from pydantic import BaseModel

from vbfsharedmodels.models.JobState import JobState


class ComputeJobResultSymbol(BaseModel):
    symbol: str
    job_state: JobState
    data: Optional[object]

    class Config:
        schema_extra = {
            "example": {
                "symbol": "AAPL",
                "job_state": {
                    "name": "finished",
                    "message": ""
                },
                "data": {
                    "gates_passed": 8,
                    "weighted_score": 4.0,
                    "symbol": "ABC",
                    "isin": "DE019282HFU",
                    "company_name": "AB Co.",
                    "price": 123.45,
                    "market_cap": 100000000000
                }
            }
        }
