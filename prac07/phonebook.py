import psycopg2
import csv

# Дерекқорға қосылу
def connect():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Gg123456)",   # өз пароліңді жаз
        host="localhost",
        port="5432"
    )

# Кесте құру
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# CSV файлдан енгізу
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()

# Консольден енгізу
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

# Жаңарту
def update_user(name=None, phone=None, new_name=None, new_phone=None):
    conn = connect()
    cur = conn.cursor()
    if new_name and name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, name))
    if new_phone and phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))
    conn.commit()
    cur.close()
    conn.close()

# Іздеу
def query_users(filter_name=None, filter_phone=None):
    conn = connect()
    cur = conn.cursor()
    if filter_name:
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (filter_name,))
    elif filter_phone:
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_phone,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    conn.close()

# Жою
def delete_user(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    if name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    create_table()
    # insert_from_csv("phonebook.csv")
    # insert_from_console()
    # update_user(name="Alice", new_phone="999999")
    # query_users()
    # delete_user(name="Bob")
