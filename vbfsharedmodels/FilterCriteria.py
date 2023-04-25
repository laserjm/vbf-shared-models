from typing import List, Optional
from pydantic import BaseModel


class FilterCriteria(BaseModel):
    market_capitalization: float
    stock_exchanges: List[str] = []
    dividend_paid: bool
    isin_required: Optional[bool]
    min_dividend_yield: Optional[float]