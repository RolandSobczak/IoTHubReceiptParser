import uuid

from sqlalchemy import Column, Float, ForeignKey, Integer, String

from backend.db import Base
from backend.settings import SETTINGS


class ReceiptItem(Base):
    __tablename__ = "receipt_item"
    __table_args__ = {"schema": SETTINGS.SCHEMA}

    id = Column(
        String(length=36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
    )
    qty = Column(Integer)
    discount = Column(Integer)
    tax_id = Column(String)
    unit_name = Column(String)
    gross = Column("bruttopln", Integer)
    amount_tax = Column(Float)
    name = Column(String)
    gross_amount = Column(Integer)
    receipt_id = Column(String, ForeignKey("demo01.receipt.id"))
    ean_id = Column(String)
    category_id = Column(String)
