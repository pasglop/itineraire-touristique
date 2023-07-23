from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

from source.databases import connect_db
from source.api.app.app import app