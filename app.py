from flask import Flask, jsonify, redirect, render_template, request

app = Flask(__name__) # turn this file named application.py into a web application

# registered students 
WORDS = []
with open("large", "r") as file:
    for line in file.readlines(): # every line in the file, read it one at a time
        WORDS.append(line.rstrip())  # right strip remove any whitespace from the end of the string

@app.route("/")     # I want to build an app that has a route that's listening for slash inside of that virtual envelope
def index():
    return render_template("index.html")
@app.route("/search")
def search():
    q = request.args.get("q")
    words = [word for word in WORDS if q and word.startswitch(q)]
    # version 1
    #return render_template("search.html", words = words)
    # version 2
    return jsonify(words) # it will show up words in the format of javascrip array wil double quotes braket
    # version 3
