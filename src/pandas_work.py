import os
from typing import Any

import pandas as pd  # type: ignore


def read_file(filename: str) -> Any:
    df = {}
    if os.path.splitext(filename)[1] == ".csv":
        df = pd.read_csv(filename, encoding="utf-8")
    elif os.path.splitext(filename)[1] == ".xlsx":
        df = pd.read_excel(filename, index_col=0)
    return df
