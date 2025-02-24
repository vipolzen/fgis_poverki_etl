from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class RawData(Base):
    __tablename__ = 'raw_data'

    id = Column(Integer, primary_key = True)
    organization_verifier = Column(String(50), nullable=False)
    reg_num_mi = Column(String(30), nullable=False)
    type_name_mi = Column(String(50), nullable=False)
    type_mi = Column(String(30), nullable=False)
    modification_mi = Column(String(30), nullable=False)
    serial_num = Column(String(30), nullable=False)
    date_verification = Column(String(10), nullable=False)
    verification_end_date = Column(String(10), nullable=False)
    certificate_of_verification_num = Column(String(30), nullable=False)
    suitability = Column(String(30), nullable=False)

class TrueSuitability(Base):
    __tablename__ = 'true_suitability'

    id = Column(Integer, primary_key=True)
    reg_num_mi = Column(String, nullable=False)
    type_name_mi = Column(String, nullable=False)
    type_mi = Column(String, nullable=False)
    modification_mi = Column(String, nullable=False)
    serial_num = Column(String, nullable=False)
    date_verification = Column(Date, nullable=False)
    verification_end_date = Column(Date, nullable=False)
    certificate_of_verification_num = Column(String, nullable=False)

class FalseSuitability(Base):
    __tablename__ = 'false_suitability'

    id = Column(Integer, primary_key=True)
    reg_num_mi = Column(String, nullable=False)
    type_name_mi = Column(String, nullable=False)
    type_mi = Column(String, nullable=False)
    modification_mi = Column(String, nullable=False)
    serial_num = Column(String, nullable=False)
    date_verification = Column(Date, nullable=False)
    unsuitability_notice_num = Column(String, nullable=False)
