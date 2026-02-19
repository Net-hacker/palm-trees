import sqlite3
import os

class Database:
    def __init__(self):
        if os.path.exists("db/user.db"):
            self.conn = sqlite3.connect("db/user.db")
            self.cursor = self.conn.cursor()
            print("Connected")
        else:
            os.mkdir("db");
            open("db/user.db", 'a').close()
            self.conn = sqlite3.connect("db/user.db")
            self.cursor = self.conn.cursor()
            table = """
                CREATE TABLE USER (
                    username VARCHAR(30) NOT NULL,
                    password VARCHAR(30) NOT NULL
                );
            """
            self.cursor.execute(table)
            print("DB Created!")

    def search_user(self, username):
        query = f"SELECT '{username}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def create_user(self, username, password):
        command = f"INSERT INTO USER VALUES ('{username}', '{password}')"
        self.cursor.execute(command)
        self.conn.commit()

    def delete_user(self, username):
        command = f"DELETE FROM USER WHERE username='{username}'"
        self.cursor.execute(command)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()
        print("Disconnected!")
