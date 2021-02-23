from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
import logging
"""
全局配置（例如连接数据库，redis,日志，登录操作等等）
1.conftest.py文件名字是固定的，不可以做任何修改

2.文件和用例文件在同一个目录下，那么conftest.py作用于整个目录

3.conftest.py文件所在目录必须存在__init__.py文件

4.conftest.py文件不能被其他文件导入

5.所有同目录测试文件运行前都会执行conftest.py文件
"""

# 连接数据库
@pytest.fixture(scope='session')
def get_session():
#创建实例   "mysql://user:password@hostname/dbname?charset=uft8
    try:
        print("开始连接数据库......")
        db = create_engine(
            'mysql+pymysql://数据库地址：端口/数据库名称?charset=utf8')
        #创建会话
        session = sessionmaker(db)
        #打开会话
        db_session = session()
        return db_session
    except Exception:
        print("数据库连接异常........",Exception)

#配置log，既要写入文件，也要在控制台显示
@pytest.fixture(scope='session')
def logger():
    # 创建一个logger
    logger = logging.getLogger()
    # 配置日志级别
    logger.setLevel(level=logging.DEBUG)#低于此等级的不会显示出来
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('tmp/test.log',encoding='utf-8')
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    # 定义handler的输出格式formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
# total = db_session.query(mynews_like).total(mynews_like.remind_user_id == "43222974567417036830")
# total = db_session.query(mynews_like).filter(mynews_like.remind_user_id == "43222974567417036830",mynews_like.info_type=="0",mynews_like.delete_mark=="0",mynews_like.user_id!="43222974567417036830")
# print(total)
# num=0
# for obj in total:
#     print(obj.id,obj.user_id,obj.remind_user_id)
#     num=num+1
# print(num)