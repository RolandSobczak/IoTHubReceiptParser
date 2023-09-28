from pydantic import BaseModel, Field


class ReceiptSchema(BaseModel):
    doc_number: str = Field(min_length=1)
    date: str = Field(min_length=1)
    cube4pos_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    discount: str = Field(min_length=1)
    payment_method_name: str = Field(min_length=1)
    purchaser_tax_id_number: str = Field(min_length=1)
