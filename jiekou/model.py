from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,create_engine,INT
Base = declarative_base()
class mynews_like(Base):
    __tablename__='表名'
    id=Column(String,primary_key=True)
    user_id=Column(String)
    user_name=Column(String)
    remind_user_id=Column(String)
    item_type=Column(INT)
    info_type=Column(INT)
    delete_mark=Column(INT)

class product(Base):
    __tablename__="表名"
    id=Column(String,primary_key=True)
    brand_id=Column(String)
    delete_mark=Column(INT)