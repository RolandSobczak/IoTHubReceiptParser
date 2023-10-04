from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.settings import SETTINGS

connection_string = f"mssql+pyodbc://{SETTINGS.USERNAME}:{SETTINGS.PASSWORD}@{SETTINGS.DB_HOST}:{SETTINGS.PORT}/{SETTINGS.DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(
    connection_string,
    connect_args={
        "check_same_thread": False,
        "options": "-csearch_path={}".format(SETTINGS.SCHEMA),
    },
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
