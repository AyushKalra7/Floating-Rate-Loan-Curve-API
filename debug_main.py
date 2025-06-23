from models import RateRequest
from utils import get_monthly_projection
from db import get_forward_rates

if __name__ == "__main__":

    fake_request = RateRequest(
        maturity_date="2026-05-20",
        reference_rate="SOFR",
        rate_floor=0.02,
        rate_ceiling=0.05,
        rate_spread=0.015
    )

    rates = get_forward_rates(
        reference_rate=fake_request.reference_rate,
        tenor="1M",
        maturity_date=fake_request.maturity_date
    )

    final_rates = get_monthly_projection(rates, fake_request)

    for row in final_rates:
        print(f"{row.date}: {row.rate}")
