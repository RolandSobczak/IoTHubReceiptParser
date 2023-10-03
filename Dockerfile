FROM python:3.11.5-bullseye

WORKDIR /app

COPY src/odbc-installer.sh /app
RUN chmod 777 odbc-installer.sh
RUN ./odbc-installer.sh

COPY poetry.lock pyproject.toml /app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root

COPY src/main.py /app/main.py
CMD ["python", "/app/main.py"]