from src.parser.main import parse_receipt, parse_receipt_item


def test_parse_receipt(receipt_data):
    receipt_body = receipt_data["Body"]
    parsed_receipt = parse_receipt(receipt_body)
    assert parsed_receipt == {
        "docNumber": "RPI_72",
        "date": "2023-09-01T06:07:20.452748",
        "cube4pos_id": "fa1f3647-0432-4368-a399-b306718944c4",
        "user_id": "2fbb4e9f-a5f3-4ab8-bb92-85b916d71304",
        "discount": "",
        "payment_method_name": "karta",
        "purchaser_tax_id_number": "",
    }


def test_parse_receipt_item(receipt_data):
    receipts = receipt_data["Body"]["receipt"]
    parsed_receipt_items = [
        parse_receipt_item(receipt_item) for receipt_item in receipts
    ]
    assert parsed_receipt_items == [
        {
            "qty": "1",
            "discount": "0",
            "tax_id": "B",
            "unit_name": "",
            "bruttopln": "3,8",
            "name": "PR 2023 FAKT PIŃTEK     B",
            "gross_amount": "3,8",
        },
        {
            "qty": "0",
            "discount": "0",
            "tax_id": "",
            "unit_name": "",
            "bruttopln": "0",
            "name": "",
            "gross_amount": "0,0",
        },
        {
            "qty": "1",
            "discount": "0",
            "tax_id": "A",
            "unit_name": "",
            "bruttopln": "14,99",
            "name": "PALL MALL BLUE MARINE C A",
            "gross_amount": "14,99",
        },
        {
            "qty": "0",
            "discount": "0",
            "tax_id": "",
            "unit_name": "",
            "bruttopln": "0",
            "name": "",
            "gross_amount": "0,0",
        },
    ]
