from parser.models import PaymentMethod, Receipt, ReceiptItem, TaxRate
from parser.schemas import ReceiptItemSchema, ReceiptSchema

from sqlalchemy.orm import Session


def fetch_payment_method(db: Session, payment_method_name: str) -> PaymentMethod | None:
    return (
        db.query(PaymentMethod)
        .filter(PaymentMethod.name == payment_method_name)
        .first()
    )


def fetch_tax_rate(db: Session, tax_id: str) -> TaxRate | None:
    return (
        db.query(TaxRate)
        .filter(TaxRate.id == tax_id, TaxRate.status == "ACTIVE")
        .first()
    )


def create_receipt(db: Session, receipt_schema: ReceiptSchema) -> Receipt:
    receipt = Receipt(**receipt_schema.model_dump())
    db.add(receipt)
    db.commit()
    db.refresh(receipt)
    return receipt


def create_receipts_item(db: Session, receipt_schema: ReceiptItemSchema) -> ReceiptItem:
    receipt_item = ReceiptItem(**receipt_schema.model_dump())
    db.add(receipt_item)
    db.commit()
    db.refresh(receipt_item)
    return receipt_item
