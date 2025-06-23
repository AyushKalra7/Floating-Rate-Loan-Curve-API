import sqlite3

def get_forward_rates(reference_rate: str, tenor: str, maturity_date):
    conn = sqlite3.connect("sofr.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT date, rate FROM forward_rates WHERE rate_type = ? AND tenor = ? ORDER BY date ASC",
        (reference_rate, tenor)
    )
    rows = cursor.fetchall()
    conn.close()
    return [r[1] for r in rows]