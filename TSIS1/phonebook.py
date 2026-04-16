import psycopg2
import json
from connect import get_connection

def filter_by_group(group_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group_name,))
    for row in cur.fetchall():
        print(row)
    conn.close()

def search_by_email(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE email ILIKE %s", ('%' + query + '%',))
    for row in cur.fetchall():
        print(row)
    conn.close()

def sort_contacts(by="name"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM contacts ORDER BY {by}")
    for row in cur.fetchall():
        print(row)
    conn.close()

def paginate_contacts(limit=5):
    conn = get_connection()
    cur = conn.cursor()
    offset = 0
    while True:
        cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        if not rows:
            print("No more contacts.")
            break
        for r in rows:
            print(r)
        cmd = input("Next / Prev / Quit: ").lower()
        if cmd == "next":
            offset += limit
        elif cmd == "prev" and offset >= limit:
            offset -= limit
        elif cmd == "quit":
            break
    conn.close()

def export_to_json(filename="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)
    rows = cur.fetchall()
    data = []
    for r in rows:
        data.append({
            "name": r[1],
            "email": r[2],
            "birthday": str(r[3]) if r[3] else None,
            "group": r[4],
            "phone": {"number": r[5], "type": r[6]}
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    conn.close()

def import_from_json(filename="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename) as f:
        data = json.load(f)
    for contact in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (contact["name"],))
        existing = cur.fetchone()
        if existing:
            choice = input(f"Contact {contact['name']} exists. Skip or overwrite? ").lower()
            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("UPDATE contacts SET email=%s, birthday=%s WHERE id=%s",
                            (contact["email"], contact["birthday"], existing[0]))
        else:
            cur.execute("INSERT INTO contacts(name,email,birthday) VALUES (%s,%s,%s) RETURNING id",
                        (contact["name"], contact["email"], contact["birthday"]))
            cid = cur.fetchone()[0]
            if contact["phone"]["number"]:
                cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES (%s,%s,%s)",
                            (cid, contact["phone"]["number"], contact["phone"]["type"]))
    conn.commit()
    conn.close()
