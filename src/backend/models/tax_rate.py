from sqlalchemy import Column, DateTime, Float, String

from backend.db import Base
from backend.settings import SETTINGS


class TaxRate(Base):
    __tablename__ = "tax_rates"
    __table_args__ = {"schema": SETTINGS.SCHEMA}

    id = Column(String)
    tax_rate_id = Column("idTaxRate", String, primary_key=True, unique=True)
    tax_rate = Column(String)
    dateFrom = Column(DateTime)
    name = Column(String)
    status = Column(String)
