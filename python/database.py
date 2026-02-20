from hash import Hash
import sqlite3
import os

class Database:
    def __init__(self):
        self.hash = Hash()
        if os.path.exists("db/database.db"):
            self.conn = sqlite3.connect("db/database.db", check_same_thread=False)
            self.cursor = self.conn.cursor()
            print("Connected!")
        else:
            os.mkdir("db");
            open("db/database.db", 'a').close()
            self.conn = sqlite3.connect("db/database.db")
            self.cursor = self.conn.cursor()
            tableU = """
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(30) NOT NULL UNIQUE,
                    password VARCHAR(30) NOT NULL
                );
            """
            tableM = """
                CREATE TABLE messages (
                    username VARCHAR(30) NOT NULL,
                    message VARCHAR(256) NOT NULL,
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                );
            """
            tableF = """
                CREATE TABLE friends (
                    follower_id INTEGER NOT NULL,
                    following_id INTEGER NOT NULL,

                    PRIMARY KEY (follower_id, following_id),

                    FOREIGN KEY (follower_id) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY (following_id) REFERENCES users(id) ON DELETE CASCADE
                );
            """
            self.cursor.execute(tableU)
            self.cursor.execute(tableM)
            self.cursor.execute(tableF)
            print("DB Created!")

    def search_user(self, username):
        query = f"SELECT username FROM users WHERE username = '{username}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def create_user(self, username, password):
        try:
            command = f"INSERT OR IGNORE INTO users (username, password) VALUES ('{username}', '{password}')"
            self.cursor.execute(command)
            self.conn.commit()
            return True
        except:
            return False

    def login_user(self, username, password):
        query = f"SELECT password FROM users WHERE username = '{username}'"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return self.hash.check_pw(password, result[0])
        except:
            return "err"

    def remove_user(self, username):
        command = f"DELETE FROM users WHERE username='{username}'"
        self.cursor.execute(command)
        self.conn.commit()

    def disconnect(self):
        self.conn.close()
        print("Disconnected!")
