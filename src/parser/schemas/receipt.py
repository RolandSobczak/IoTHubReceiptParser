from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReceiptSchema(BaseModel):
    id: Optional[str] = None
    doc_number: str = Field(min_length=1)
    date: datetime
    cube4pos_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    discount: str = Field(min_length=1)
    payment_method_id: str = Field(min_length=1)
    purchaser_tax_id_number: str = Field(min_length=1)
    gross: float
    amount_tax: float
