import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def create_table(self, sql):
        """
        Creates a table in the database based on the provided SQL query.

        Args:
            sql (str): The SQL query to create the table.

        Returns:
            None
        """
        try:
            c = self.conn.cursor()
            c.execute(sql)
            self.conn.commit()
            print("Table created successfully")
            
            
        except Error as e:
            print(e)
        finally:
            c.close()

    def insert(self, sql, data):
        try:
            c = self.conn.cursor()
            c.execute(sql, data)
            self.conn.commit()
        except Error as e:
            print(e)

    def chat_collection(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM chat")
        return c
