"""
测试 SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

# https://docs.sqlalchemy.org/en/latest/core/engines.html#mysql
engine = create_engine('mysql://root:woaiwojia.@localhost:3306/news_test?charset=utf8') # 创建连接
Base = declarative_base() # 创建基类

Session = sessionmaker(bind=engine) # 创建 session 对象 engine 是连接的实例

class News(Base):
    # 表名称
    __tablename__ = 'news'
    # 各个字段
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), )
    author = Column(String(20), )
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

# print(News.__table__)
News.metadata.create_all(engine) # 创建表

# 插入数据
class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        # new_obj = News(
        #     title='title1',
        #     content='content1',
        #     types='type1'
        # )
        new_obj = News(
            title='标题1',
            content='内容',
            types='百家'
        )
        self.session.add(new_obj) # add_all 插入多条
        self.session.commit()
        return new_obj

    def get_one(self):
        """
        查询一条数据 按照 id 查询
        """
        return self.session.query(News).get(1) # 当查询的数据不存在时，不会报错

    def get_more(self):
        # 查询多条数据
        return self.session.query(News).filter_by(is_valid=True)

    def update_data(self, pk):
        """
        更新数据: 查询一条或多条 -> 修改(多条可以循环修改) -> add -> commit
        """
        # 更新一条数据
        # new_obj = self.session.query(News).get(pk)
        # if new_obj:
        #     new_obj.is_valid = 0
        #     self.session.add(new_obj)
        #     self.session.commit()
        #     return True
        # return False
        # 更新多条数据
        data_list = self.session.query(News).filter_by(is_valid = None) # 这里 filter_by 和 filter 有区别，感觉filter_by 只能做 = 操作，拿 key 进行判断。filter 需要使用 News 对象去获取属性
        for data in data_list:
            data.is_valid = 1
            self.session.add(data)
        self.session.commit()

    def delete_data(self, pk):
    # 删除数据
        new_obj = self.session.query(News).get(pk)
        self.session.delete(new_obj)
        self.session.commit()

def main():
    obj = OrmTest()
    # 出现编码错误，由于 new_obj 中插入的有中文，解决办法：在创建 engine 连接的时候指定编码
    # UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-1: ordinal not in range(256)
    # 添加一条数据
    # rest = obj.add_one()
    # print(rest)

    # 查询一条数据
    # rest = obj.get_one()
    # if rest:
    #     print(rest.id, rest.title)
    # else:
    #     print('not exit')

    # 查询多条数据
    # rest = obj.get_more()
    # print(rest.count())
    # for new_obj in rest:
    #     print(new_obj.id, new_obj.title)

    # 更新一条数据
    # print(obj.update_data(3))
    # 更新多条数据
    # obj.update_data(0)

    # 删除一条数据
    obj.delete_data(5)

if __name__ == '__main__':
    main()
