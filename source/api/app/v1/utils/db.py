import os

import psycopg2
import psycopg2.extras


def connect_db():
    """
    This function is used to connect to the postgresql database.
    :return:
    """
    conn = psycopg2.connect(
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"))
    sess = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return conn, sess


def disconnect_db(conn, sess):
    sess.close()
    conn.close()


