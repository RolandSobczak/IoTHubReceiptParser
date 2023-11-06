import json
import logging
import os
from json import JSONDecodeError
from pathlib import Path

from pydantic import ValidationError

from backend.db import create_new_connection
from backend.parser import parse_document
from backend.repositories import insert_document
from backend.settings import SETTINGS

INPUT_FOLDER = "/input"
logging.basicConfig(level=SETTINGS.LOG_LEVEL)


def get_all_nested_files(root_dir: Path) -> list[str]:
    file_paths = []
    for root, directories, files in os.walk(root_dir):
        for filename in files:
            if filename.split(".")[-1] == "json":
                file_path = os.path.join(root, filename)
                file_paths.append(file_path)
    return file_paths


def upload_receipt(db, receipt_data: str, file_path: str):
    try:
        receipt_json = json.loads(receipt_data)
        parsed_receipt, parsed_receipt_items = parse_document(db, receipt_json)
        logging.info(f"Successfully parsed receipt [path={file_path}]")
        insert_document(db, parsed_receipt, parsed_receipt_items)
    except ValidationError as error_msg:
        logging.debug(error_msg)
        logging.info(f"Invalid Receipt format. Skipping... [path={file_path}]")
    except JSONDecodeError as error_msg:
        logging.debug(error_msg)
        logging.info(
            f"Receipt doesn't meet Receipt Schema requirements. Skipping... [path={file_path}]",
        )
    except RuntimeError as error_msg:
        logging.debug(error_msg)
        logging.info(
            f"Receipt doesn't meet Receipt Schema requirements. Skipping... [path={file_path}]",
        )
    except Exception as error_msg:
        logging.debug(error_msg)
        logging.info(
            f"Receipt doesn't meet Receipt Schema requirements. Skipping... [path={file_path}]",
        )


def main():
    """Main parser command function. Parse receipt and send it to SQL database.

    :param delete: if it's true removes file from disk after receipt upload
    :type delete: bool
    """
    file_paths = get_all_nested_files(Path(INPUT_FOLDER))
    db = create_new_connection()
    for file_path in file_paths:
        with open(file_path, encoding="utf-8") as input:
            while receipt_json := input.readline():
                upload_receipt(db, receipt_data=receipt_json, file_path=file_path)

        if SETTINGS.DELETE_FILES:
            os.remove(file_path)
            logging.info(f"Receipt file deleted. [path={file_path}]")


if __name__ == "__main__":
    main()
