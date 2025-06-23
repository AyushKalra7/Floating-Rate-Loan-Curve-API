import pandas as pd
import sqlite3
import time
import requests
from io import BytesIO
from config import EXCEL_URL
from constants import DB_PATH, TABLE_NAME, RATE_TYPE, TENOR

def download_with_retries(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            if response.ok:
                return response
        except Exception:
            time.sleep(delay)
    raise Exception("Failed to download data")

def extract_and_store():
    response = download_with_retries(EXCEL_URL)
    xls = pd.ExcelFile(BytesIO(response.content))
    df = pd.read_excel(xls, sheet_name="Forward Curve", skiprows=4, usecols="G:H", nrows=125)
    df.columns = ['date', 'rate']
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    df['rate'] = df['rate'].astype(float)
    df['rate_type'] = RATE_TYPE
    df['tenor'] = TENOR

    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    extract_and_store()