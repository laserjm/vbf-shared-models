from dataclasses import dataclass

@dataclass
class StrategicBasicData:
    gates_passed: int
    weighted_score: float
    symbol: str
    isin: str
    company_name: str 
    # exchange_short_name: str 
    # country: str 
    # currency: str # new
    price: float 
    # discounted_cash_flow: float
    # sector: str
    # industry: str
    market_cap: float