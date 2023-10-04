import json
import logging
import os
from json import JSONDecodeError
from pathlib import Path

from pydantic import ValidationError
from sqlalchemy.orm import Session

from backend.db import SessionLocal
from backend.parser import parse_receipt, parse_receipt_item
from backend.repositories import create_receipt, create_receipts_item

INPUT_FOLDER = "/input"
logging.basicConfig(level=logging.DEBUG)


def get_all_nested_files(root_dir: Path) -> list[str]:
    file_paths = []
    for root, directories, files in os.walk(root_dir):
        for filename in files:
            if filename.split(".")[-1] == "json":
                file_path = os.path.join(root, filename)
                file_paths.append(file_path)
    return file_paths


def insert_receipt_json(db: Session, receipt_json):
    receipt_data = parse_receipt(db, receipt_json["Body"])
    db_receipt = create_receipt(db, receipt_data)
    logging.info(f"Receipt inserted successful [id={db_receipt.id}]")
    for receipt_item in receipt_json["Body"]["receipt"]:
        try:
            receipt_item_schema = parse_receipt_item(db, receipt_item)
            db_receipt_item = create_receipts_item(db, receipt_item_schema)
            logging.info(f"Receipt item inserted successful [id={db_receipt_item.id}]")
        except ValidationError as error_msg:
            logging.info("Incorrect receipt item skipped")


def main():
    file_paths = get_all_nested_files(INPUT_FOLDER)
    db = SessionLocal()
    for file_path in file_paths:
        with open(file_path, encoding="utf-8") as input:
            while file := input.readline():
                try:
                    receipt_json = json.loads(file)
                    insert_receipt_json(db, receipt_json)
                except ValidationError as error_msg:
                    logging.debug(error_msg)
                    logging.info(f"Invalid receipt skipped [path={file_path}]")
                except JSONDecodeError as error_msg:
                    logging.debug(error_msg)
                    logging.info(f"Incorrect JSON format [path={file_path}]")


if __name__ == "__main__":
    main()
