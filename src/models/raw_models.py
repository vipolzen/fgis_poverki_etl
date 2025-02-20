from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Model = declarative_base()

class Raw_data(Model):
    __tablename__ = 'raw_data'

    id = Column(Integer, primary_key = True)
    organization_verifier = Column(String)
    reg_num_mi = Column(String)
    type_name_mi = Column(String)
    type_mi = Column(String)
    modification_mi = Column(String)
    serial_num = Column(String)
    date_verification = Column(String)
    verification_end_date = Column(String)
    certificate_of_verification_num = Column(String)
    suitability = Column(String)
