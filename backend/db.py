import sqlite3
from datetime import datetime

DB_NAME = "chat.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_reply TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_chat(user_message, bot_reply):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO chat_logs (user_message, bot_reply, timestamp)
        VALUES (?, ?, ?)
    """, (user_message, bot_reply, datetime.now().isoformat()))
    conn.commit()
    conn.close()
