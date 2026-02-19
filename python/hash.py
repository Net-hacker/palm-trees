import hashlib
import os

class Hash:
    def __init__(self):
        if os.path.exists("key.txt"):
            file = open("key.txt", "r")
            self.key = file.read()
            file.close()
        else:
            print("Can't find key file. Revert to standard!")
            with open("key.txt", "w") as file:
                file.write("palm")
                file.close()
            self.key = "palm"

    def hash_pw(self, password):
        hashobj = hashlib.sha256(self.key.encode() + password.encode())
        password_hash = hashobj.hexdigest()
        return password_hash

    def check_hash(self, password, hashed_pw):
        hashobj = hashlib.sha256(self.key.encode() + password.encode())
        password_hash = hashobj.hexdigest()
        return password_hash == hashed_pw
