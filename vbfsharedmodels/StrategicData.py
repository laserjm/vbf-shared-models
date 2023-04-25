from dataclasses import dataclass

@dataclass
class StrategicData:
    gates_passed: int
    weighted_score: float
    symbol: str
    isin: str
    company_name: str 
    exchange: str
    exchange_short_name: str 
    country: str 
    currency: str # new
    price: float 
    discounted_cash_flow: float
    sector: str
    sector_pe_ratio: float
    industry: str
    industry_pe_ratio: float
    market_cap: float
    current_ratio: float
    price_earnings_ratio: float 
    price_to_book_ratio: float
    price_to_cash_flow_ratio: float
    debt_equity_ratio: float
    # revenue_growth: float  # dropped
    net_income_ratio: float
    net_income_t4q_1_q: str
    net_income_t4q_1: float
    net_income_t4q_2_q: str
    net_income_t4q_2: float
    net_income_t4q_3_q: str
    net_income_t4q_3: float
    net_income_t4q_4_q: str
    net_income_t4q_4: float
    net_income_t5y_1_y: str
    net_income_t5y_1: float
    revenue_t5y_1: float
    net_income_t5y_2_y: str
    net_income_t5y_2: float
    revenue_t5y_2: float
    net_income_t5y_3_y: str
    net_income_t5y_3: float
    revenue_t5y_3: float
    net_income_t5y_4_y: str
    net_income_t5y_4: float
    revenue_t5y_4: float
    net_income_t5y_5_y: str
    net_income_t5y_5: float
    revenue_t5y_5: float
    dividend_t5y_1_date: str
    dividend_t5y_1_payout_ratio: float  # payout ratio: Ausschüttungsquote
    dividend_t5y_1_yield: float  # Dividendenrendite
    dividend_t5y_2_date: str
    dividend_t5y_2_payout_ratio: float
    dividend_t5y_2_yield: float
    dividend_t5y_3_date: str
    dividend_t5y_3_payout_ratio: float
    dividend_t5y_3_yield: float
    dividend_t5y_4_date: str
    dividend_t5y_4_payout_ratio: float
    dividend_t5y_4_yield: float
    dividend_t5y_5_date: str
    dividend_t5y_5_payout_ratio: float
    dividend_t5y_5_yield: float
    historical_dividend: float
    dividend_yield: float
    dividend_growth_avg_last_5y: float
    dividend_payout_ratio: float
    max_score: int
    unfillfilled_criterias: str