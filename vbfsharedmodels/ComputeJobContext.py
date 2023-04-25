from typing import List
from pydantic import BaseModel

from vbfsharedmodels.Strategy import Strategy
from vbfsharedmodels.FilterCriteria import FilterCriteria


class ComputeJobContext(BaseModel):
    strategy: Strategy
    target_symbols: List[str]
    filter_criteria: FilterCriteria

    class Config:
        schema_extra = {
            "example": {
                "strategy": f"{Strategy.value_title}",
                "target_symbols": [
                    "all"
                ],
                "filter_criteria": {
                    "market_capitalization": 300000000.0,
                    "stock_exchanges": ["NYSE","NASDAQ","AMEX","EURONEXT","XETRA","LSE"],
                    "dividend_paid": True,
                    "isin_required": True,
                    "min_dividend_yield": 3.0
                    # "pre_checks": False,
                    # "pre_check_criterias": [
                    #     "financial_ratio.current_ratio",
                    #     "financial_ratio.debt_equity_ratio",
                    #     "financial_ratio.price_to_cash_flow_ratio",
                    #     "cash_flow.dividend_paid"
                    # ]
                },
            }
        }

