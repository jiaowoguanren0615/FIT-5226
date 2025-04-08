import functools
import logging as log
import os
import sys
import atexit

# 取出运行脚本名（不含路径、不含扩展名）
script_path = sys.argv[0]
script_name = os.path.splitext(os.path.basename(script_path))[0]


os.makedirs('logs', exist_ok=True)


def search_logger(filename: str = None):
    logger = log.getLogger()
    for h in list(logger.handlers):
        logger.removeHandler(h)
    if filename is None:
        logger.disabled = True
        return

    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    fpath = os.path.join('logs', f'{filename}.log')
    f_handler = log.FileHandler(fpath, mode='w', encoding='utf-8')
    f_handler.setLevel(log.INFO)
    f_handler.setFormatter(log.Formatter(log_format))
    logger.addHandler(f_handler)

    logger.setLevel(log.INFO)
    logger.info(f"Logger initialized for script: {filename}")

search_logger(script_name)


def _flush():
    for func_name, msg in log_function.buffer:
        log.getLogger(func_name).info(msg)
    log_function.buffer.clear()

# 注册程序退出时自动 flush
atexit.register(_flush)

def log_function(func: callable):
    if not hasattr(log_function, 'buffer'):
        log_function.buffer = []
        log_function.remaining_log_calls = 1000

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if log_function.remaining_log_calls <= 0:
            return func(*args, **kwargs)

        args_str = ",".join(map(str, args))
        kwargs_str = ",".join(f"{k}={v}" for k, v in kwargs.items())
        in_msg = f"I: {args_str}" + (f", {kwargs_str}" if kwargs_str else "")
        log_function.buffer.append((func.__name__, in_msg))

        result = func(*args, **kwargs)

        log_function.buffer.append((func.__name__, f"O: {result}"))
        log_function.remaining_log_calls -= 1

        _flush()

        return result
    return wrapper
