import psycopg2
from config import DB_PARAMS

def connect():
    return psycopg2.connect(**DB_PARAMS)

def save_result(username, score, level):
    conn = connect(); cur = conn.cursor()
    cur.execute("INSERT INTO players(username) VALUES(%s) ON CONFLICT(username) DO NOTHING", (username,))
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    pid = cur.fetchone()[0]

    cur.execute("INSERT INTO game_sessions(player_id, score, level_reached, played_at) VALUES(%s,%s,%s, CURRENT_TIMESTAMP)", 
                (pid, score, level))
    conn.commit(); conn.close()

def top10():
    conn = connect(); cur = conn.cursor()
    cur.execute("""SELECT p.username, g.score, g.level_reached, g.played_at
                   FROM game_sessions g JOIN players p ON g.player_id=p.id
                   ORDER BY g.score DESC LIMIT 10""")
    rows = cur.fetchall(); conn.close()
    return rows


def personal_best(username):
    conn = connect(); cur = conn.cursor()
    cur.execute("""SELECT MAX(score) FROM game_sessions g
                   JOIN players p ON g.player_id=p.id WHERE p.username=%s""", (username,))
    best = cur.fetchone()[0]; conn.close()
    return best or 0
