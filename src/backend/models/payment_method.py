from sqlalchemy import Column, String

from backend.db import Base


class PaymentMethod(Base):
    __tablename__ = "payment_method"
    __table_args__ = {"schema": "demo01"}

    id = Column(String, unique=True, primary_key=True)
    name = Column(String, unique=True)
