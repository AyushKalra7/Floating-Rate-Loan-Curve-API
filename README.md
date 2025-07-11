# Floating Rate Loan Curve API

## Overview

This project provides a REST API to calculate projected monthly interest rates for floating rate loans using 1-month forward SOFR rates. It consists of two parts:

- **ETL script** that downloads, parses, and stores forward rates from Pensford’s publicly available Excel sheet into an SQLite database.
- **FastAPI-based REST service** that accepts loan parameters (spread, floor, ceiling, maturity) and returns a list of monthly projected rates using the stored data.

---

## Design Decisions

This repo is structured to separate **data ingestion** (ETL) from **rate projection logic**, making it modular and maintainable. Constants (e.g., DB path, rate type) are centralized for configurability. The SQLite backend was chosen for simplicity, and FastAPI was used for its excellent developer experience and built-in Swagger UI.

> To read about design choices, see `explain_design_decisions()` in `explain.py`.

---

## Assumptions & Trade-offs

- **Assumption:** 1-month SOFR rates from Pensford represent realistic forward curves.
- **Assumption:** Loans reset monthly on the current date; we align projection dates accordingly. Also, it is assumed that the data being recieved is dated till 5/20/2035
- **Trade-off:** Chose SQLite over PostgreSQL to simplify setup; in production this would need a scalable RDBMS.
- **Simplification:** We assume forward rate order aligns with monthly projection needs (no interpolation).
- **Improvement area:** Handle missing months or gaps in rate data with fallback logic.

---

## How to Run Locally

### Prerequisites
- Python 3.10+
- `pip install -r requirements.txt`

### 1. Run ETL script
This downloads and stores 1M SOFR forward rates:

```bash
python etl.py

### 2. Start the FastAPI Server
Run the API locally:

```bash
uvicorn main:app --reload
```

Then open your browser at:  
[http://localhost:8000/docs](http://localhost:8000/docs) to test via Swagger UI.

### 3. Example Request

```http
POST /loan-rate-curve
Content-Type: application/json

{
  "maturity_date": "2026-01-01",
  "reference_rate": "SOFR",
  "rate_floor": 0.02,
  "rate_ceiling": 0.05,
  "rate_spread": 0.015
}
```

---

## Time Spent

3.5 hrs

---

## If I Had More Time

- Add automated tests for the ETL layer  
- Introduce logging and better error handling  
- Support multiple tenors and reference rate types

## Snip of success response 
<img width="1692" alt="Screenshot 2025-06-23 at 23 39 45" src="https://github.com/user-attachments/assets/1e5fd693-aa28-4b8c-86db-b09f0b24c769" />
