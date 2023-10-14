import sqlite3

# Connect to the database
conn = sqlite3.connect("budget_tracker.db")
cur = conn.cursor()

# Create a table for transactions
cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               category TEXT,
               type TEXT,
               amount REAL,
               date TEXT)''')

# Commit and close the connection
conn.commit()
conn.close()
