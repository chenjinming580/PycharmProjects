# author:JinMing time:2020-05-18
# -*- coding: utf-8 -*-
import logging

"""
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别
    format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s",  # 指定日志格式
            # 时间    产生日志的文件名  产生日志的行号      日志级别        日志正文
    datefmt="%Y-%m-%d %H:%M:%S",  # 指定日期时间格式
    filename="./test.log",  # 指定日志文件的路径
    filemode="a"  # 文件打开方式，在指定了filename参数的时候，
)

logging.debug("这是一条debug信息")
logging.info("这是一条info信息")
logging.warning("这是一条warning信息")
logging.error("这是一条error信息")
logging.critical("这是一条critical信息")
"""

# 创建日志对象
logger = logging.getLogger()
# 创建一个 handler，用于写入日志文件
fh = logging.FileHandler("./test.log")
# 再创建一个 handler，用于屏幕输出
ch = logging.StreamHandler()

# 制定输出格式，相当于 basicConfig 中的 format
formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")

# 将输出格式传入处理器
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 往 logger 中添加输出方式
logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel(logging.DEBUG)

logger.debug("这是一条debug信息")
logger.info("这是一条info信息")
logger.warning("这是一条warning信息")
logger.error("这是一条error信息")
logger.critical("这是一条critical信息")