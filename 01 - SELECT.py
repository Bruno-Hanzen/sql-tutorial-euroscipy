import sqlite3


db = sqlite3.connect('data/hubway.db')

query = """
SELECT * 
FROM trips;
"""

