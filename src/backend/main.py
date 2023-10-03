import json

from backend.db import SessionLocal
from backend.parser import parse_receipt, parse_receipt_item
from backend.repositories import create_receipt, create_receipts_item

JSON_FILENAME = "07.json"


def main():
    db = SessionLocal()
    with open(f"/input/{JSON_FILENAME}", encoding="utf-8") as input:
        receipt_json = json.loads(input.read())
        receipt_data = parse_receipt(db, receipt_json["Body"])
        create_receipt(db, receipt_data)
        for receipt_item in receipt_json["Body"]["receipt"]:
            receipt_item_schema = parse_receipt_item(db, receipt_item)
            db_receipt = create_receipts_item(db, receipt_item_schema)


if __name__ == "__main__":
    main()
