from dotenv import load_dotenv
import os

load_dotenv()

FLASK_ENV = os.getenv('FLASK_ENV', 'development')

PG_HOST = os.getenv('PG_HOST')
PG_DB = os.getenv('PG_DB')
PG_USER = os.getenv('PG_USER')
PG_PASS = os.getenv('PG_PASS')
PG_PORT = os.getenv('PG_PORT')

if FLASK_ENV == 'production':
    DB_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}'
else:
    DB_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}'