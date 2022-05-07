import logging
import os

from dotenv import load_dotenv
from masoniteorm.connections import ConnectionResolver

load_dotenv()

DATABASES = dict(
    default="sqlite",
    sqlite=dict(driver="sqlite", database=os.getenv("SQLITE_DB")),
    postgres=dict(
        host="localhost",
        driver="postgres",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT"),
        log_queries=os.getenv("LOG_QUERIES"),
    ),
)

logger = logging.getLogger("masoniteorm.connection.queries")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
logger.addHandler(handler)

DB = ConnectionResolver().set_connection_details(DATABASES)
