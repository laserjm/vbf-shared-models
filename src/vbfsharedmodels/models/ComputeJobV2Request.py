from typing import Any, Optional
from bson import ObjectId
from pydantic import BaseModel, Field


from vbfsharedmodels.models.ComputeJobBaseV2 import ComputeJobBaseV2
from vbfsharedmodels.models.ComputeJobContext import ComputeJobContext
from vbfsharedmodels.models.ComputeJobResultV2 import ComputeJobResultV2
from vbfsharedmodels.models.JobState import JobState


class ComputeJobV2Request(ComputeJobBaseV2):
    # no further fields

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "start_date_time": "2022-07-30T09:52:50.374Z",
                "compute_job_context": {
                    "strategy": "value",
                    "target_symbols": ["IBM", "AAPL", "GOOG", "BLK", "MMM"],
                    "filter_criteria": {
                        "market_capitalization": 300000000.0,
                        "stock_exchanges": [],
                        "dividend_paid": False,
                        "isin_required": True,
                        "min_dividend_yield": 0.0,
                    },
                },
                "user_id": "000000-0000-0000-000000",
            }
        }
