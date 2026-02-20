import hashlib
import os

class Hash:
    def __init__(self):
        if os.path.exists("static/key.txt"):
            file = open("static/key.txt", "r")
            self.key = file.read()
            file.close()
        else:
            print("Can't find key file. Revert to standard!")
            with open("static/key.txt", "w") as file:
                file.write("palm")
                file.close()
            self.key = "palm"

    def hash_pw(self, password):
        hashobj = hashlib.sha256(self.key.encode() + password.encode())
        password_hash = hashobj.hexdigest()
        return password_hash

    def hash_session(self, user):
        hashobj = hashlib.sha256(user.encode() + self.key.encode())
        session_hash = hashobj.hexdigest()
        return session_hash

    def check_pw(self, password, hashed_pw):
        return password == hashed_pw

    def check_session(self, user, log):
        hashobj = hashlib.sha256(user.encode() + self.key.encode())
        return log == hashobj.hexdigest()
