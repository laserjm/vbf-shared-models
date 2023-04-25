from typing import Any, List
from pydantic import BaseModel


class ComputeJobResult(BaseModel):
    model_type: str
    data: List[Any]

    class Config:
        schema_extra = {
            "example": {
                "model_type": "StrategicBasicData",
                "data": [
                    {
                        "gates_passed": 2,
                        "weighted_score": 4.0,
                        "symbol": "ABC",
                        "isin": "DE019282HFU",
                        "company_name": "AB Co.",
                        "price": 123.45,
                        "market_cap": 100000000000
                    }
                ]
            }
        }

