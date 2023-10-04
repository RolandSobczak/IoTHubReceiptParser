# IoTHubReceiptParser
Simple CLI tool for parsing receipts from IoT HUB to CUBE API format


### Instalation

1. Install docker and docker-compose on your local machine
2. Copy content of `.env.example` to `.env` file and fill it with db MSSQL db credentials
3. Copy all receipt JSON files to `input/` folder
4. Build docker image
    ```shell
    docker-compose build
    ```

5. Run docker container
    ```shell
    docker-compose up
    ```

### Logging config
This tool use builtin python `logging` package.

To set loglevel set `LOG_LEVEL` variable in `.env` file. Here is the list of available options:
   1. **NOTSET**
   2. **DEBUG**
   3. **INFO**
   4. **WARN**
   5. **ERROR**
   6. **CRITICAL**
