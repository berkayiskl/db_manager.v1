import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()

        
            cur.execute('''
                CREATE TABLE IF NOT EXISTS fifa_rank (
                    country TEXT,
                    rank_date TEXT,
                    rank INTEGER,
                    points REAL
                )
            ''')

            
            cur.execute('''
                CREATE TABLE IF NOT EXISTS matches (
                    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    home_team TEXT,
                    away_team TEXT,
                    home_score INTEGER,
                    away_score INTEGER,
                    tournament TEXT,
                    city TEXT,
                    country TEXT,
                    neutral INTEGER
                )
            ''')

            
            cur.execute('''
                CREATE TABLE IF NOT EXISTS world_cup (
                    year INTEGER PRIMARY KEY,
                    host_country TEXT,
                    winner TEXT,
                    runner_up TEXT,
                    teams INTEGER,
                    matches_played INTEGER,
                    goals_scored INTEGER
                )
            ''')

            conn.commit()

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data=tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()
