from pydantic import BaseModel, Field


class ReceiptItemSchema(BaseModel):
    qty: str = Field(min_length=1)
    discount: str = Field(min_length=1)
    tax_id: str = Field(min_length=1)
    unit_name: str = Field(min_length=1)
    gross: str = Field(min_length=1)
    name: str = Field(min_length=1)
    gross_amount: str = Field(min_length=1)
