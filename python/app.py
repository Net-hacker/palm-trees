from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from database import Database
from hash import Hash

def getKey():
    file = open("static/key.txt", "r")
    key = file.read()
    file.close()
    return key

db = Database()
hash = Hash()
app = Flask(__name__)
app.secret_key = getKey();

@app.route("/api/signup", methods=["POST"])
def api_signup():
    data = request.get_json()

    username = data.get("user_name")
    password = data.get("user_password")
    hashed_pw = hash.hash_pw(password)
    sign = db.create_user(username, hashed_pw)

    if sign == True:
        session["user"] = username
        session["log"] = hash.hash_session(username)
        return jsonify({"sucess": True})
    else:
        return jsonify({"sucess": False}), 401

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()

    username = data.get("user_name")
    password = data.get("user_password")
    hashed_pw = hash.hash_pw(password)
    test = db.login_user(username, hashed_pw)

    if test == True:
        session["user"] = username
        session["log"] = hash.hash_session(username)
        return jsonify({"success": True})
    elif test == "err":
        return jsonify({"success": False}), 401
    else:
        return jsonify({"success": False}), 300

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/login", methods=["GET"])
def login():
    if "user" in session:
        if hash.check_session(session["user"], session["log"]) == True:
            return redirect(url_for("index"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/")
def index():
    if "user" in session:
        if hash.check_session(session["user"], session["log"]) == True:
            return render_template("index.html")
        else:
            return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))
