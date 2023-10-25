FROM python:3.11.5-bullseye

WORKDIR /src

COPY src/odbc-installer.sh /src
RUN chmod 777 odbc-installer.sh
RUN ./odbc-installer.sh

COPY src/poetry.lock src/pyproject.toml /src/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-root

COPY ./src /src
RUN poetry install

CMD ["poetry", "run", "receipt-parser"]