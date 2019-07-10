from app import db
from sqlalchemy import Column,Integer,String,Float,DateTime;
from datetime import datetime


class Measurement(db.Model) :

    id = Column(Integer,primary_key=True)
    air_quality = Column(Float,nullable=False)
    humidity = Column(Float,nullable=False)
    temperature = Column(Float,nullable=False)
    timestamp =  Column(DateTime, nullable=False,default=datetime.utcnow)
    y = Column(Float,nullable=False)
    z = Column(Float,nullable=False)

p = Column(Float,nullable=False)