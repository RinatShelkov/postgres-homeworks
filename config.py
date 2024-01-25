from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent
CUSTOMERS_DATA = ROOT_PATH.joinpath("homework-1").joinpath("north_data").joinpath("customers_data.csv")
EMPLOYERS_DATA = ROOT_PATH.joinpath("homework-1").joinpath("north_data").joinpath("employees_data.csv")
ORDERS_DATA = ROOT_PATH.joinpath("homework-1").joinpath("north_data").joinpath("orders_data.csv")
print(EMPLOYERS_DATA)
