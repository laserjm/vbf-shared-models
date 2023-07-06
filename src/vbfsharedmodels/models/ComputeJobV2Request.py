from typing import Any, Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from vbfsharedmodels.models.ComputeJobContext import ComputeJobContext
from vbfsharedmodels.models.ComputeJobResultV2 import ComputeJobResultV2
from vbfsharedmodels.models.JobState import JobState


class ComputeJobV2Request(BaseModel):
    version: int = 3
    start_date_time: str
    end_date_time: str
    compute_job_context: ComputeJobContext
    job_state: JobState
    file_name: str
    user_id: str
    compute_job_result: Optional[ComputeJobResultV2]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "start_date_time": "2022-07-30T09:52:50.374Z",
                "end_date_time": "2022-07-30T09:52:50.374Z",
                "compute_request": {
                    "strategy": "value",
                    "workflow": "optimized",
                    "target_symbols": [
                        "all"
                    ]
                },
                "job_state": {
                    "name": "not started",
                    "message": ""
                },
                "file_name": "./output/vbf_export_2023_01_11_19_38_04.csv",
                "user_id": "000000-0000-0000-000000",
                "compute_job_result": {
                    "model_type": "StrategicBasicData",
                    "symbols": [
                        {
                            "AAPL": {
                                "state": {
                                    "name": "finished",
                                    "message": ""
                                },
                                "data": {
                                    "gates_passed": 2,
                                    "weighted_score": 4.0,
                                    "symbol": "ABC",
                                    "isin": "DE019282HFU",
                                    "company_name": "AB Co.",
                                    "price": 123.45,
                                    "market_cap": 100000000000
                                }
                            }
                        },
                        {
                            "GOOG": {
                                "state": {
                                    "name": "queued",
                                    "message": ""
                                },
                                "data": {}
                            }
                        }
                    ]
                }
            }
        }
