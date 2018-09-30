"""
测试 SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# https://docs.sqlalchemy.org/en/latest/core/engines.html#mysql
engine = create_engine('mysql://root:woaiwojia.@localhost:3306/news') # 创建连接
Base = declarative_base() # 创建基类


