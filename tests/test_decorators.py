import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "filename, a, b, expected_result",
    [
        (
            "test_file.txt",
            1,
            0,
            "2024-04-24 18:18:46 my_function error: <integer division or modulo by zero>. Inputs: (1, 0), {}",
        ),
        ("test_file.txt", 1, 4, "2024-04-24 18:18:46 my_function ok"),
        (
            "test_file.txt",
            1,
            "jkd",
            "2024-04-24 18:20:32 my_function error: <unsupported operand type(s) for +: 'int' and "
            "'str'>. Inputs: (1, 'fdg'), {}",
        ),
        (
            None,
            1,
            "dfhh",
            "2024-04-24 18:20:32 my_function error: <unsupported operand type(s) for +: 'int' and "
            "'str'>. Inputs: (1, 'fdg'), {}",
        ),
        (None, 1, 2, "2024-04-24 18:18:46 my_function ok"),
    ],
)
def test_log_filename(filename: str, a: int, b: int, expected_result: str) -> None:
    @log(filename)
    def my_function(a: int, b: int) -> None:
        assert a + b == expected_result
