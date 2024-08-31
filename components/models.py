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
    # async def get_previous_1_message(self, index_no):
    #     """
    #     Asynchronously retrieves the previous message before the given index_no.
    #     :param index_no: The index or ID of the last known message.
    #     :return: A single message or None if no more messages are found.
    #     """
    #     # Simulate asynchronous I/O operation, such as a database query
    #     # await asyncio.sleep(0.1)  # Simulating an I/O-bound operation

    #     # Example query (you would replace this with your actual database query)
    #     query = "SELECT id, content, timestamp FROM messages WHERE id < ? ORDER BY id DESC LIMIT 1"
        
    #     # Assuming you have a method to execute this query and fetch the result
    #     # The example below assumes an SQLite-like database connection
    #     message = await  self.fetch_selected(query, (index_no,)) 

        
    #     return message  # Returns the fetched message, or None if no message found
# Method to run the database operation in a separate thread

if __name__ == "__main__":
    chat = ChatHandler()
    print(chat.only_last_one_message(index_no=7))