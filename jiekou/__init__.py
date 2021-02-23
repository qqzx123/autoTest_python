import logging
#配置日志级别，日志格式，输出位置
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='tmp/test.log',
#                     filemode='w')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


# # 创建一个logger
# logger = logging.getLogger()
# # 配置日志级别
# logger.setLevel(level=logging.DEBUG)
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('tmp/test.log',encoding='utf-8')
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# # 定义handler的输出格式formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# # 给logger添加handler
# logger.addHandler(fh)
# logger.addHandler(ch)
# # 记录一条日志
# logger.info("哈哈哈哈哈哈")
# logger.info("sjas加上时间哈")
