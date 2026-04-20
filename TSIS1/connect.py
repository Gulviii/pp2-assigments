import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

if __name__ == "__main__":
    conn = get_connection()
    print("Connected to PostgreSQL!")
    conn.close()
