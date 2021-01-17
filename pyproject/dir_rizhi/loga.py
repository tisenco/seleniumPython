import logging
import os
import time

shijian=time.strftime('%Y-%m-%d')
file_path='C:\\pyproject\\rizhiwenjian\\2021-01-09.log'
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler(file_path)
a=logging.Formatter('%(levelname)s--> %(lineno)d--> %(asctime)s   %(message)s')

def add_log():
    file_handler.setFormatter(a)
    logger.addHandler(file_handler)
    return logger
def close_handler():
    file_handler.close()
    logger.removeHandler(file_handler)
