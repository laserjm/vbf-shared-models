from typing import Any, Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from vbfsharedmodels.models.ComputeJobContext import ComputeJobContext
from vbfsharedmodels.models.ComputeJobResultV2 import ComputeJobResultV2
from vbfsharedmodels.models import JobState

# https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class ComputeJobV2(BaseModel):
    version: int = 2
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
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
                "id": "63e400ec57891e82da21f7dd",
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
