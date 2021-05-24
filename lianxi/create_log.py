import logging
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
consle=logging.StreamHandler()
file_handle=logging.FileHandler('C:/Users/Administrator/Desktop/testlog.txt')
a=logging.Formatter('%(asctime)s--%(filename)s'
                  '--%(funcName)s--%(levelno)s--%(message)s')
file_handle.setFormatter(a)
logger.addHandler(consle)
logger.addHandler(file_handle)
logger.debug('tests')
consle.close()
file_handle.close()
logger.removeHandler(consle)
logger.removeHandler(file_handle)


