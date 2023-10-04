from sqlalchemy.orm import Session

from backend.repositories import fetch_payment_method, fetch_tax_rate
from backend.schemas import ReceiptItemSchema, ReceiptSchema


def parse_receipt(db: Session, receipt_body: dict) -> ReceiptSchema:
    brutto = sum(
        [
            float(receipt["gross-amount"].replace(",", "."))
            for receipt in receipt_body["receipt"]
        ],
    )
    payment_method_name = receipt_body["payment-method"]
    payment_method = fetch_payment_method(db, payment_method_name)
    amount_tax = 0
    if payment_method is None:
        for receipt in receipt_body["receipt"]:
            tax_definition = fetch_tax_rate(db, receipt["tax-id"])
            if tax_definition is not None:
                tax_value = (
                    float(receipt["gross-amount"].replace(",", "."))
                    * tax_definition.tax_rate
                )
                amount_tax += tax_value

    return ReceiptSchema(
        doc_number=receipt_body["docNumber"],
        date=receipt_body["date"],
        cube4pos_id=receipt_body["id-cube4pos"],
        user_id=receipt_body["id-user"],
        discount=receipt_body["discount-receipt"],
        payment_method_id=payment_method.id,
        purchaser_tax_id_number=receipt_body["purchaser-tax-id-number"],
        gross=brutto,
        amount_tax=amount_tax,
    )


def parse_receipt_item(db: Session, receipt_item: dict) -> ReceiptItemSchema:
    gross_amount = float(receipt_item["gross-amount"].replace(",", ""))
    tax_definition = fetch_tax_rate(db, receipt_item["tax-id"])
    amount_tax = 0
    if tax_definition is not None:
        amount_tax = tax_definition.tax_rate * gross_amount
    return ReceiptItemSchema(
        qty=int(receipt_item["qty"].replace(",", "")),
        discount=receipt_item["discount-item"],
        tax_id=receipt_item["tax-id"],
        unit_name=receipt_item["unit-name"],
        gross=float(receipt_item["brutto"].replace(",", "")),
        name=receipt_item["name"],
        gross_amount=gross_amount,
        amount_tax=amount_tax,
    )
