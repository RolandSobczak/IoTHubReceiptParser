import logging
from functools import wraps
from time import sleep
from typing import Optional, Sequence

from sqlalchemy.exc import OperationalError

from backend.db import create_new_connection


def countdown(sec: int):
    for counter in range(sec)[::-1]:
        logging.info(f"Waiting. Seconds to next attempt: {counter}")
        sleep(sec)


def with_retry(
    retries_limit: int = 5,
    cooldown: int = 5,
    allowed_exceptions: Optional[Sequence[Exception]] = None,
):
    allowed_exceptions = allowed_exceptions or (OperationalError,)

    def retry(operation):
        @wraps(operation)
        def wrapped(db, *args, **kwargs):
            last_raised = None

            for counter in range(1, retries_limit + 1):
                try:
                    db = create_new_connection()
                    return operation(db, *args, **kwargs)
                except allowed_exceptions as e:
                    logging.warning(f"Reconnecting to database. Attempt {counter}")
                    last_raised = e
                    countdown(cooldown)
            raise last_raised

        return wrapped

    return retry
