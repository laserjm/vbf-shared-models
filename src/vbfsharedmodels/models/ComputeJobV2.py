from typing import Any, Optional
from bson import ObjectId
from pydantic import BaseModel, Field

from vbfsharedmodels.models.ComputeJobBaseV2 import ComputeJobBaseV2
from vbfsharedmodels.models.ComputeJobContext import ComputeJobContext
from vbfsharedmodels.models.ComputeJobResultV2 import ComputeJobResultV2
from vbfsharedmodels.models.JobState import JobState


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


class ComputeJobV2(ComputeJobBaseV2):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "63e400ec57891e82da21f7dd",
                "start_date_time": "2022-07-30T09:52:50.374Z",
                "end_date_time": "2022-07-30T09:57:33.232Z",
                "compute_job_context": {
                    "strategy": "value",
                    "target_symbols": ["all"],
                    "filter_criteria": {
                        "market_capitalization": 300000000.0,
                        "stock_exchanges": [],
                        "dividend_paid": True,
                        "isin_required": True,
                        "min_dividend_yield": 3.0,
                    },
                },
                "job_state": {
                    "name": "not started",
                    "message": "",
                    "jobs_to_compute": 0,
                },
                "user_id": "000000-0000-0000-000000",
                "compute_job_result": {
                    "model_type": "StrategicBasicData",
                    "symbols": [
                        {
                            "symbol": "AAPL",
                            "job_state": {"name": "finished", "message": ""},
                            "data": {
                                "gates_passed": 2,
                                "weighted_score": 4.0,
                                "symbol": "ABC",
                                "isin": "DE019282HFU",
                                "company_name": "AB Co.",
                                "price": 123.45,
                                "market_cap": 100000000000,
                            },
                        },
                        {
                            "symbol": "GOOG",
                            "job_state": {"name": "queued", "message": ""},
                            "data": {},
                        },
                    ],
                },
            }
        }
