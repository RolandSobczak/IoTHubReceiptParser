import uuid
from datetime import datetime
from parser.db import Base

from sqlalchemy import Column, DateTime, Float, Integer, String


class Receipt(Base):
    __tablename__ = "receipt"
    __table_args__ = {"schema": "demo01"}

    id = Column(
        String(length=36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
    )
    doc_number = Column("docnumber", String)
    date = Column(DateTime)
    gross = Column("sumapln", Float)
    amount_tax = Column(Float)
    discount = Column(Integer)
    user_id = Column(String)
    cube4pos_id = Column(String)
    payment_method_id = Column(String)
    last_modified = Column(DateTime, default=datetime.now)
    purchaser_tax_id_number = Column(String)
    virtual_transaction_number = Column(String)
