import logging,logging.handlers

def WriteLog(log_name):
	log_filename = "/tmp/new.log"
	log_level = logging.DEBUG
	format = logging.Formatter('%(asctime)s %(filename)s - [line:%(lineno)2d] - %(funcName)s  %(levelname)s - %(name)s %(message)s')
	handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
	handler.setFormatter(format)
	logger = logging.getLogger(log_name)
	if not logger.handlers:
		logger.addHandler(handler)
		logger.setLevel(log_level)
	return logger

if __name__ == '__main__':
	WriteLog('api').info('123')
