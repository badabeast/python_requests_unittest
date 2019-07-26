# coding=utf-8
import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler
from getpathinfo import get_path

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s%(levelname)s-%(message)s')
# logger = logging.getLogger(__name__)  #实例化一个logger对象
# logger.debug("msg1")
# logger.info("msg2")
# logger.warning("msg3")
# logger.error("msg4")
# logger.critical("msg5")
'''
1、创建一个logger

2、设置下logger的日志的等级

3、创建合适的Handler(FileHandler要有路径)

4、设置下每个Handler的日志等级

5、创建下日志的格式

6、向Handler中添加上面创建的格式

7、将上面创建的Handler添加到logger中

8、打印输出logger.debug\logger.info\logger.warning\logger.error\logger.critical
'''
logpath = get_path()
print(logpath)


class LoggingMethod(object):
    # 将日志输出到文件
    def __init__(self, name):
        # 1、创建一个logger
        self.logger = logging.getLogger(name)
        # 2、设置下logger的日志的等级
        self.logger.setLevel(logging.DEBUG)
        # 定义log文件名
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        filename = logpath + '\\LOG\\' + now
        # 创建等级为DEBUG的 的日志文件，默认使用全局的Logger日志等级
        all_handler = logging.handlers.TimedRotatingFileHandler(filename + '_debug.txt', when='D', interval=1,
                                                                backupCount=7, encoding='utf-8')
        all_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        # 创建等级为error的日志文件
        fh_handler = logging.StreamHandler(filename + '_error.txt')
        fh_handler.setLevel(logging.ERROR)
        fh_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        # 7、将上面创建的Handler添加到logger中
        self.logger.addHandler(all_handler)
        self.logger.addHandler(fh_handler)

    def getlogger(self):
        return self.logger


if __name__ == '__main__':
    login = LoggingMethod(__name__)
    logger = login.getlogger()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")
