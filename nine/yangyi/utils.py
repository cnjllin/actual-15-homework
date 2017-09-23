# Author: tailorYang
import logging,sys
import logging.handlers

def writelog(log_name):
    log_file = sys.path[0]+r'/tmp/test.log'
    log_level = logging.DEBUG
    # 定义日志格式
    log_format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)2d]-%(funcName)s  %(levelname)s %(name)s %(message)s')
    fh = logging.handlers.RotatingFileHandler(log_file, mode='a', maxBytes=10*1024*1024, backupCount=5)
    fh.setFormatter(log_format)

    # 实例化日志对象
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)
    # 每调用一次就会添加一个logger.handler，每次就额外多打印一次日志
    if not logger.handlers:
        logger.addHandler(fh)

    return logger


