from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReceiptSchema(BaseModel):
    id: Optional[str] = None
    doc_number: str
    date: datetime
    cube4pos_id: str
    user_id: str
    discount: str
    payment_method_id: str
    purchaser_tax_id_number: str
    gross: float
    amount_tax: float
