import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import re
from operator import itemgetter, attrgetter

from helpers import apology, login_required, database
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

info = {}
subject_info ={}


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///schools.db")

@app.route("/veiwclass", methods=["post", "get"])
def veiwclass():
    
    # format class tables names
    tables = database(request.form.get("veiw_class"))
    classId = tables["class_id"]
    schoolId = session["user_id"]
    schoolClassTable = tables["classes"]
    catable = tables["ca"]
    testtable = tables["test"]
    examtable = tables["exam"]
    subjecttable = tables["subjects"]
    teacherstable = tables["teachers"]
    classlisttable = tables["classlist"]
    mastersheet = tables["mastersheet"]
    subject_position_table = tables["subject_position"]


    #query database
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = schoolClassTable, classId = classId)
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = schoolId)
    carow = db.execute("SELECT * FROM :catable",catable = catable)
    testrow = db.execute("SELECT * FROM :testtable",testtable = testtable)
    examrow = db.execute("SELECT * FROM :examtable",examtable = examtable)
    subjectrow = db.execute("SELECT * FROM :subjecttable",subjecttable = subjecttable)
    
    teachersrow = db.execute("SELECT * FROM :teacherstable",teacherstable = teacherstable)       
    classlistrow = db.execute("SELECT * FROM :classlist",classlist = classlisttable)
    mastersheet_rows = db.execute("SELECT * FROM :mastersheet", mastersheet = mastersheet)
    subject_position_row = db.execute("SELECT * FROM :subject_position", subject_position = subject_position_table)



    # render class veiw
    return render_template("classView.html", schoolData = schoolrow, classData = classrow, caData = carow, testData = testrow, examData = examrow, subjectData = subjectrow, teachersData = teachersrow,class_list = classlistrow, mastersheet = mastersheet_rows, subject_position = subject_position_row)

@app.route("/login", methods=["POST","GET"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()


    # Ensure username was submitted
    if not request.form.get("username"):
        return apology("must provide username", 403)

    # Ensure password was submitted
    elif not request.form.get("password"):
        return apology("must provide password", 403)

    # Query database for username
    rows = db.execute("SELECT * FROM school WHERE username = :username",username=request.form.get("username").lower())
    # Remember which user has logged in
    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
        return apology("invalid username and/or password", 403)
    session["user_id"] = rows[0]["id"]
    schoolId = rows[0]["id"]
    tables = database(str(0))
    schoolClass = tables["classes"]
    classRows = db.execute("SELECT * FROM :classes ",classes = schoolClass)
    # return render portfolio
    return render_template("portfolio.html", schoolInfo = rows, clas = classRows)

@app.route("/")
def index():
    return render_template("login.html")        
             


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


   

def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
