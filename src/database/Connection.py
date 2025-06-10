# import libraries
import psycopg2

class Database:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("Connection to the database established successfully.")
            return self.connection
        except Exception as e:
            print(f"An error occurred while connecting to the database: {e}")
            return None
    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection to the database closed.")