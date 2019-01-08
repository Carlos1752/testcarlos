#输出到一个文件的log时只能输出一个level的信息
import logging
logging.basicConfig(level=logging.DEBUG,filename='runlog.log',
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')#打印出时间，行数，信息内容
# logging.basicConfig(level=logging.INFO,filename='runlog.log')

logging.debug('debug info')
logging.info('hello 123456')
logging.warning('warning info')
logging.error('errot info')
logging.critical('cratical info')

logging.debug('debug info')
logging.info('CARLOS')
logging.warning('warning info')
logging.error('errot info')
logging.critical('cratical info')
