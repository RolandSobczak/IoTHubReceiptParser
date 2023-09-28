def parse_receipt(receipt_body: dict):
    return {
        "docNumber": receipt_body["docNumber"],
        "date": receipt_body["date"],
        "cube4pos_id": receipt_body["id-cube4pos"],
        "user_id": receipt_body["id-user"],
        "discount": receipt_body["discount-receipt"],
        "payment_method_name": receipt_body["payment-method"],
        "purchaser_tax_id_number": receipt_body["purchaser-tax-id-number"],
    }


def parse_receipt_item(receipt_item: dict):
    return {
        "qty": receipt_item["qty"],
        "discount": receipt_item["discount-item"],
        "tax_id": receipt_item["tax-id"],
        "unit_name": receipt_item["unit-name"],
        "bruttopln": receipt_item["brutto"],
        "name": receipt_item["name"],
        "gross_amount": receipt_item["gross-amount"],
    }
