import csv
import os
from typing import Any

import pandas as pd  # type: ignore


def read_file(filename: str) -> Any:
    """Читает csv и xlsx файлы"""
    if os.path.splitext(filename)[1] == ".csv":
        read_file_csv(filename)
    elif os.path.splitext(filename)[1] == ".xlsx":
        read_file_read_excel(filename)


def read_file_csv(filename: str) -> Any:
    df = []
    with open(filename, encoding="utf-8") as file:
        read_csv = csv.DictReader(file, delimiter=";")
        for i in read_csv:
            df.append(i)
    return df


def read_file_read_excel(filename: str) -> Any:
    df = pd.read_excel(filename, index_col=0)
    return df.to_dict("records")
