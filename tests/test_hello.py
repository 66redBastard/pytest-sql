from src.database import get_connection


def test_get_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()
