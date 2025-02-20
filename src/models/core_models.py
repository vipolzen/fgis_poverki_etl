from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class True_suitability(Base):
    __tablename__ = 'true_suitability'

    id = Column(Integer, primary_key=True)
    reg_num_mi = Column(String)
    type_name_mi = Column(String)
    type_mi = Column(String)
    modification_mi = Column(String)
    serial_num = Column(String)
    date_verification = Column(String)
    verification_end_date = Column(String)
    certificate_of_verification_num = Column(String)

class False_suitability(Base):
    __tablename__ = 'false_suitability'

    id = Column(Integer, primary_key=True)
    reg_num_mi = Column(String)
    type_name_mi = Column(String)
    type_mi = Column(String)
    modification_mi = Column(String)
    serial_num = Column(String)
    date_verification = Column(String)
    unsuitability_notice_num = Column(String)