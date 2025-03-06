import functools
import sys

def log(filename=None):
    """
    Декоратор для логирования выполнения функции
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = (f"{func.__name__} error: {type(e).__name__}. "
                           f"Inputs: {args}, {kwargs}")
                raise
            finally:
                if filename:
                    with open(filename, 'a') as f:
                        f.write(message + '\n')
                else:
                    print(message)
                    if "error" in message:
                        sys.stderr.write(message + '\n')
            return result
        return wrapper
    return decorator
