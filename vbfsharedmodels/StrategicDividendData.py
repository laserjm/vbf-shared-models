from dataclasses import dataclass

from vbfsharedmodels.StrategicBasicData import StrategicBasicData

@dataclass
class StrategicDividendData(StrategicBasicData):
    calc_base_year: str 
    last_dividend: float  # lastDiv of Profile??
    last_dividend_calculated: float  # self calculated
    dividend_yield: float  # Dividendenrendite -- financial_ratio.dividend_yield
    dividend_yield_calculated: float  # self calculated
    dividend_growth_avg_last_5y: float  # Dividendenwachstum -- own calc
    dividend_payout_ratio: float  # Ausschüttungsquote -- 
    dividend_payout_ratio_calc: float  # Ausschüttungsquote -- own calc
    dividend_payout_ratio_cash: float  # Ausschüttungsquote Cash -- 
    dividend_payout_ratio_cash_calc: float  # Ausschüttungsquote Cash -- own calc
    unfillfilled_criterias: str