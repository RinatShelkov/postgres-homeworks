"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2

from config import CUSTOMERS_DATA, EMPLOYERS_DATA, ORDERS_DATA
from utils import reading_csv_xlsx_file, get_all_values

customers_data = get_all_values(reading_csv_xlsx_file(CUSTOMERS_DATA))
employees_data = get_all_values(reading_csv_xlsx_file(EMPLOYERS_DATA))
orders_data = get_all_values(reading_csv_xlsx_file(ORDERS_DATA))

# conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="200108")
# try:
#     with conn:
#         with conn.cursor() as cur:
#             cur.executemany("INSERT INTO customers VALUES ( %s, %s, %s)", customers_data)
#
#
# finally:
#     conn.close()

# conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="200108")
# try:
#     with conn:
#         with conn.cursor() as cur:
#             cur.executemany("INSERT INTO employees VALUES ( %s, %s, %s, %s, %s, %s)", employees_data)
#
#
# finally:
#     conn.close()

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="200108")
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES ( %s, %s, %s, %s, %s)", orders_data)


finally:
    conn.close()
