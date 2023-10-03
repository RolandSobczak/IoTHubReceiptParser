from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SERVER = "cubebidb.database.windows.net"
DATABASE = "topmdatademo"
USERNAME = "sal@cubebidb"
PASSWORD = "H4YbrcXAjQ9L6YSn"
SCHEMA = "demo01"


connection_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
connection_string = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(
    connection_string,
    connect_args={
        "check_same_thread": False,
        "options": "-csearch_path={}".format(SCHEMA),
    },
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
