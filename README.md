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
