import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
import os

from source.utils import get_project_root

load_dotenv()  # take environment variables from .env.

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    dbname='postgres',
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"))

# Allow database creation
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

# Name of the database
dbname = os.getenv("PG_DB")

cur.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(dbname)))
cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))


# Close the cursor and the connection
cur.close()
conn.close()

# Now that we have our database, we connect to it
conn = psycopg2.connect(
    dbname=dbname,
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"))
cur = conn.cursor()


# Function to execute sql file
def execute_sql_file(filename):
    path = f'{get_project_root()}/{filename}'
    with open(path, 'r') as f:
        cur.execute(sql.SQL(f.read()))


cur.execute(sql.SQL("CREATE EXTENSION IF NOT EXISTS pg_trgm;"))
# Execute the sql files
execute_sql_file('artifacts/sql/classes.sql')
execute_sql_file('artifacts/sql/places.sql')

# Commit changes and close
conn.commit()
cur.close()
conn.close()
