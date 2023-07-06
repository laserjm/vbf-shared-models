from typing import Any, List
from pydantic import BaseModel

from vbfsharedmodels.models.ComputeJobResultSymbol import ComputeJobResultSymbol


class ComputeJobResultV2(BaseModel):
    model_type: str
    symbols: List[ComputeJobResultSymbol]

    class Config:
        schema_extra = {
            "example": {
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

