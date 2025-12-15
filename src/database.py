import os

import psycopg2
from dotenv import load_dotenv

from utils.logger import (
    log_database_connection_attempt,
    log_database_connection_failure,
    log_database_connection_success,
)

load_dotenv()


def get_connection():
    db_name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    log_database_connection_attempt(db_name, user, host, port)

    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        log_database_connection_success(db_name)
        return conn
    except Exception as exc:
        log_database_connection_failure(db_name, user, host, port, str(exc))
        return None


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    with open("sql/schema.sql", "r") as f:
        schema = f.read()

    cursor.execute(schema)
    conn.commit()
    cursor.close()
    conn.close()
