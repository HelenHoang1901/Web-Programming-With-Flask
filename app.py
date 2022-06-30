import os
import smtplib    # simple mail transfer protocol
from flask import Flask, redirect, render_template, request
import csv

app = Flask(__name__) # turn this file named application.py into a web application

# registered students 
students = []

@app.route("/")     # I want to build an app that has a route that's listening for slash inside of that virtual envelope
def index():
    #name = request.args.get("name", "world")   # "world" is a default name
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students = students)

@app.route("/register", methods = ["POST"]) # by default if we did not give a method, it will be assumed that it is GET method
def register():
    #name = request.args.get("name") # it is for GET Method
    name = request.form.get("name")
    #email = request.form.get("email")
    #dorm = request.args.get("dorm") # It is for GET Method
    dorm = request.form.get("dorm")
    if not name or not dorm: # or not email:
        return render_template("failure.html")

    # VERSION 1
    # return render_template("success.html")

    # VERSION 2
    # students.append(f"{name} from {dorm}")
    # return redirect("/registrants")

    # VERSION 3
    #message = "You are registered!"
    #server = smtplib.SMTP("smtp.gmail.com", 587)   # help to tell the library what server to use to send email. # 587 - TCP port they use
    #server.starttls()     # the email is encrypted between you and Gmail
    #server.login("helenhoang2512@gmail.com", os.getenv("helen!2000"))
    #server.sendmail("helenhoang2512@gmail.com", email, message)
    #return render_template("success.html")

    # VERSION 4 - save data to hardrive permantly
    file = open("registered.csv", "a")#append - add a row to the file
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("dorm"))) # a tuple format
    file.close()
    return render_template("success.html")

@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
    # file.close()
    return render_template("registered.html", students=students)
