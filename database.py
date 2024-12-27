import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def grade_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    complaint_details INTEGER,
                    phone_number TEXT,
                    food_rating TEXT,
                    cleanliness_rating TEXT,
                    extra_comments INTEGER,
                    finish_feedback TEXT
                )
            """)
            conn.commit()

###############
database = Database('db.sqlite3')
database.grade_tables()