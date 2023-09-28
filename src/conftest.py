import json

import pytest


@pytest.fixture
def receipt_json():
    return """{
    "EnqueuedTimeUtc": "2023-09-01T04:07:23.3040000Z",
    "Properties": {
        "$$ContentType": "JSON",
        "$$CreationTimeUtc": "2023-09-01T06:07:23.196844",
        "$$MessageSchema": "receipt-generator;v1",
        "eventType": "receipt-demo",
        "iothub-creation-time-utc": "2023-09-01T06:07:23.196810",
        "iothub-message-schema": "receipt-generator;v1"
    },
    "SystemProperties": {
        "connectionDeviceId": "lecedre-c4p-demo-02",
        "connectionDeviceGenerationId": "637309457989605066",
        "contentType": "application/json",
        "contentEncoding": "utf-8",
        "enqueuedTime": "2023-09-01T04:07:23.3040000Z"
    },
    "Body": {
        "eventType": "receipt-demo",
        "receipt": [
            {
                "unit-name": "",
                "gross-amount": "3,8",
                "discount-item": "0",
                "brutto": "3,8",
                "qty": "1",
                "tax-id": "B",
                "name": "PR 2023 FAKT PIŃTEK     B"
            },
            {
                "unit-name": "",
                "gross-amount": "0,0",
                "discount-item": "0",
                "brutto": "0",
                "qty": "0",
                "tax-id": "",
                "name": ""
            },
            {
                "unit-name": "",
                "gross-amount": "14,99",
                "discount-item": "0",
                "brutto": "14,99",
                "qty": "1",
                "tax-id": "A",
                "name": "PALL MALL BLUE MARINE C A"
            },
            {
                "unit-name": "",
                "gross-amount": "0,0",
                "discount-item": "0",
                "brutto": "0",
                "qty": "0",
                "tax-id": "",
                "name": ""
            }
        ],
        "docNumber": "RPI_72",
        "date": "2023-09-01T06:07:20.452748",
        "id-cube4pos": "fa1f3647-0432-4368-a399-b306718944c4",
        "id-user": "2fbb4e9f-a5f3-4ab8-bb92-85b916d71304",
        "ser-cube4Pos": "100000001f773267",
        "discount-receipt": "",
        "payment-method": "karta",
        "purchaser-tax-id-number": ""
    }
}
"""


@pytest.fixture
def receipt_data(receipt_json):
    return json.loads(receipt_json)
