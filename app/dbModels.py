from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary
from sqlalchemy.orm import relationship
import datetime
from datetime import timedelta

from dbEngin import Base

class CounterMain(Base):
    __tablename__ = "TB_READ_COUNTER_M"

    counter_id = Column(String, primary_key=True, index=True)
    read_count = Column(Integer, index=False)
    create_date = Column(DateTime, index=False, default=datetime.datetime.now)
    update_date = Column(DateTime, index=False, default=datetime.datetime.now)
    create_req_id = Column(String, index=False, default=None)
    update_req_id = Column(String, index=False, default=None)

    def copy_from(self, source):
        print(self)
        self.__dict__.update(source.__dict__)    

class CounterDetail(Base):
    __tablename__ = "TB_READ_COUNTER_D"

    counter_id = Column(String, primary_key=True, index=True)
    detail_id = Column(String, primary_key=True, index=True)
    read_count = Column(Integer, index=False)
    create_date = Column(DateTime, index=False, default=datetime.datetime.now)
    update_date = Column(DateTime, index=False, default=datetime.datetime.now)
    create_req_id = Column(String, index=False, default=None)
    update_req_id = Column(String, index=False, default=None)

    def copy_from(self, source):
        print(self)
        self.__dict__.update(source.__dict__)    


