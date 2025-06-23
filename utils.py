from models import RateRequest, RateResponse
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_monthly_projection(rates, request: RateRequest):
    result = []
    today = datetime.today().date()
    end_date = request.maturity_date

    for i, raw_rate in enumerate(rates):
        curr_date = today + relativedelta(months=i)
        if curr_date >= end_date:
            break
        final = raw_rate + request.rate_spread
        if final < request.rate_floor:
            final = request.rate_floor
        if final > request.rate_ceiling:
            final = request.rate_ceiling
        result.append(RateResponse(date=curr_date, rate=round(final, 4)))
    return result