from typing import Optional

from pydantic import BaseModel, Field


class ReceiptItemSchema(BaseModel):
    qty: int
    discount: str
    tax_id: str = Field(min_length=1, max_length=1)
    name: str = Field(min_length=1)
    gross_amount: float
    gross: float
    unit_name: Optional[str] = None
    amount_tax: float
