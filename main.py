from fastapi import FastAPI
from models import RateRequest, RateResponse
from utils import get_monthly_projection
from db import get_forward_rates
from constants import API_TITLE

app = FastAPI(title=API_TITLE)

@app.post("/loan-rate-curve", response_model=list[RateResponse])
def loan_rate_curve(request: RateRequest):
    rates = get_forward_rates(request.reference_rate, "1M", request.maturity_date)
    return get_monthly_projection(rates, request)