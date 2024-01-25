from os import PathLike
from typing import Any

import numpy as np
import pandas as pd


def reading_csv_xlsx_file(path: PathLike) -> Any:
    """Функция  с CSV- и XLSX-файлов
    param path: путь к файлу
    return: список словарей с данными
    """
    path_str = str(path)

    if path_str.endswith(".csv"):
        results = pd.read_csv(path, sep=",")

    elif path_str.endswith(".xlsx"):
        results = pd.read_excel(path)

    elif path_str.endswith(".xls"):
        results = pd.read_excel(path)

    else:
        return "Неверное расширение файла, задан неправильный путь"

    results = pd.DataFrame(results).replace({np.nan: None})
    result_list_dict = results.to_dict(orient="records")

    return result_list_dict


def get_all_values(list_dict: list[dict]) -> list[tuple]:
    """Функция преобразования списка словарей в список кортежей dict.values,
    для записи данных в БД"""

    result_list_turple = []

    for dictionary in list_dict:
        values = dictionary.values()
        turple_values = tuple(values)
        result_list_turple.append(turple_values)

    return result_list_turple
