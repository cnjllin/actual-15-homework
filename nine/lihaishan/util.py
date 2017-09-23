import logging,logging.handlers
def WriteLog(log_name):
    log_filename = "C://Users//HP//PycharmProjects//untitled11//abc.log"
    log_level = logging.DEBUG
    format = logging.Formatter('%(asctime)s %(filename)s - [line:%(lineno)2d] - %(funcName)s  %(levelname)s - %(name)s %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
    streamhandler = logging.StreamHandler()
    handler.setFormatter(format)
    logger = logging.getLogger(log_name)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    logger.removeHandler(streamhandler)
    return logger
