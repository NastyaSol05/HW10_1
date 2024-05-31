from typing import Any
from unittest.mock import patch

import pandas as pd  # type: ignore

from src.pandas_work import read_file


@patch("pandas.read_csv")
def test_read_csv(read_csv: Any) -> None:
    read_csv.return_value = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    result_csv = read_file("data.csv")
    expected_result = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    assert result_csv.equals(expected_result)


@patch("pandas.read_excel")
def test_read_xlsx(read_xlsx: Any) -> None:
    read_xlsx.return_value = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    result_xlsx = read_file("data.xlsx")
    expected_result = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    assert result_xlsx.equals(expected_result)
