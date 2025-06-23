from pydantic import BaseModel, Field
from datetime import date

class RateRequest(BaseModel):
    maturity_date: date
    reference_rate: str
    rate_floor: float
    rate_ceiling: float
    rate_spread: float

class RateResponse(BaseModel):
    date: date
    rate: float