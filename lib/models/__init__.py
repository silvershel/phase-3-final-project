import sqlite3

CONN = sqlite3.connect('stash.db')
CURSOR = CONN.cursor()
