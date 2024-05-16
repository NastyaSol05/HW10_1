import datetime
from typing import Any, Callable, Union


def log(filename: Union[str, None] = None) -> Callable:
    """Внутренняя функция, которая записывает в файл логи выполнения функций"""
    def inner(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return_value = None
            result = f"{'{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())} {func.__name__}"
            try:
                return_value = func(*args, **kwargs)
                result += " ok"
            except Exception as err:
                result += f" error: <{err.args[0]}>. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, "a") as f:
                    f.write(result + "\n")
            else:
                print(result)
            return return_value

        return wrapper

    return inner
