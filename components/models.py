import sqlite3
from sqlite3 import Error
from datetime import datetime 
import os


class Database:    
    def __init__(self):
        self.conn = None
        try:
            # Ensure the directory exists
            path =  os.path.join(os.getcwd(), 'INCHAT')
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory: {e}")
        db_file = "INCHAT/inchat.db"
        try:
            self.conn = sqlite3.connect(db_file, check_same_thread=False)  # Allow access from multiple threads
        except Error as e:
            print(f"Connection error: {e}")

    def create_table(self, sql):
        return self.execute_query(sql)

    def execute_query(self, sql, data=None):
        try:
            c = self.conn.cursor()
            if data:
                c.execute(sql, data)
            else:
                c.execute(sql)
            
            self.conn.commit()  # Commit changes to the database
            return True
        except Error as e:
            print(f"Error: {e}")
            self.conn.rollback()  # Rollback changes on error
            return False

    def fetch_all(self, sql):
        try:
            c = self.conn.cursor()
            c.execute(sql)
            return c.fetchall()
        except Error as e:
            print(f"Error: {e}")
            return None
    def fetch_selected(self, sql, params):
        try:
            c = self.conn.cursor()
            c.execute(sql, params)
            return c.fetchall()
        except Error as e:
            print(f"Error: {e}")
    
    def fetch_selected_one(self, sql, params):
        try:
            c = self.conn.cursor()
            c.execute(sql, params)
            return c.fetchone()
        except Error as e:
            print(f"Error: {e}")
    def close(self):
        if self.conn:
            self.conn.close()
class ChatHandler(Database):
    def __init__(self, name='Chat'):
        super().__init__()
        self.name = name
    
    def __str__(self) -> str:
        print('Chat handler created')
    
    
    
    def insert_data(self, message):
        time = datetime.now().strftime("%H:%M:%S")
        sql = "INSERT INTO chats (name, message, time) VALUES (?, ?, ?)"
        return self.execute_query(sql, (self.name, message, time))
    
    #query for last 10 messages
        # Query for the last 10 messages
    def last_10_messages(self):
        sql = "SELECT * FROM chats ORDER BY id DESC LIMIT 10"
        return self.fetch_all(sql)
    
    def get_previous_10_messages(self, index_no):
        ''' SQL query to fetch the previous 10 messages before the given index'''
        sql = """
        SELECT * FROM chats WHERE id < ? ORDER BY id DESC LIMIT 10;
        """
        
        # Fetch the messages starting from the given index
        messages = self.fetch_selected(sql, params=(index_no,))
        
        return messages
    
    
    def insert_message_to_db(self, message):
        
        success = self.insert_data(message)
        if success:
            print("Message inserted successfully")
            return True
        else:
            print("Failed to insert message")
            return False


    def only_last_one_message(self, index_no):
        query = "SELECT * FROM chats WHERE id < ? ORDER BY id DESC LIMIT 1"
        
        return self.fetch_selected_one(query, (index_no,))
# import asyncio
# from threading import Thread, Lock

# class AsyncDatabaseHandler:
#     def __init__(self):
#         self.conn = None
#         self.lock = Lock()  # Lock for thread safety

#         try:
#             # Ensure the directory exists
#             path = os.path.join(os.getcwd(), 'INCHAT')
#             os.makedirs(path, exist_ok=True)
#         except Exception as e:
#             print(f"Error creating directory: {e}")

#         db_file = "INCHAT/inchat.db"
#         try:
#             self.conn = sqlite3.connect(db_file, check_same_thread=False)  # Allow access from multiple threads
#         except sqlite3.Error as e:
#             print(f"Connection error: {e}")

#     def execute_query(self, sql, data=None):
#         def task():
#             with self.lock:
#                 try:
#                     cursor = self.conn.cursor()
#                     if data:
#                         cursor.execute(sql, data)
#                     else:
#                         cursor.execute(sql)
#                     self.conn.commit()
#                 except sqlite3.Error as e:
#                     print(f"Error: {e}")
#                     self.conn.rollback()

#         thread = Thread(target=task)
#         thread.start()
#         thread.join()  # Wait for the thread to finish

#     def fetch_query(self, sql, data=None):
#         def task():
#             with self.lock:
#                 cursor = self.conn.cursor()
#                 if data:
#                     cursor.execute(sql, data)
#                 else:
#                     cursor.execute(sql)
#                 result = cursor.fetchall()
#             return result

#         loop = asyncio.get_event_loop()
#         future = loop.run_in_executor(None, task)
#         return future

# class AsyncChatHandler:
#     def __init__(self):
#         self.db = AsyncDatabaseHandler()

#     def get_previous_10_messages(self, index_no):
#         sql = "SELECT * FROM chats WHERE id < ? ORDER BY id DESC LIMIT 10"
#         return self.db.fetch_query(sql, (index_no,))
    
if __name__ == "__main__":
    chat = ChatHandler()
    print(chat.only_last_one_message(index_no=7))