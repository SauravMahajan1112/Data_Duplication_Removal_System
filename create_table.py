import sqlite3

# Connect to SQLite DB (it will create one if it doesn't exist)
conn = sqlite3.connect('file_data.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY, file_name TEXT, file_hash TEXT)''')

# Save (commit) the changes and close the connection
conn.commit()
conn.close()
