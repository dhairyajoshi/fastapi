from enum import Enum
from uuid import uuid4
from pydantic import BaseModel


class ChartEnum(Enum):
    New_NPA_Accounts = "New_NPA_Accounts"
    NPA_Accounts_with_recovery = "NPA_Accounts_with_recovery"
    New_SMA_Accounts = "New_SMA_Accounts"


class DataModel(BaseModel):
    id: str = str(uuid4())
    chart_type: ChartEnum
    customer_id: str
    customer_name: str
    days_overdue: int 
    amount_overstanding: float
    recover: float 
    date_created: str 
