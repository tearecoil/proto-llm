import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError
import time
from app.config import settings

def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host = settings.DATABASE_HOST,
                db = settings.DATABASE_NAME, 
                user = settings.DATABASE_USER,
                password = settings.DATABASE_PASSWORD,
                cursor_factory=RealDictCursor    
            )
            cursor = conn.cursor()
            print("Connection successful")
            break
        except Exception as error:
            print("Failed as: ", error)
            time.sleep(2)
    return conn, cursor 