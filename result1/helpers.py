import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
    
def database(id):
    tables = {}
    # format class tables names
    classId = id
    tables["class_id"] = id
    tables["school_id"] = session["user_id"]
    schoolId = session["user_id"]
    tables["classes"] = "classes"+"_"+str(tables["school_id"])
    classIdentifier = str(schoolId)+"_"+str(classId)
    tables["ca"]  = "catable"+classIdentifier
    tables["test"] = "testtable"+classIdentifier
    tables["exam"] = "examtable"+classIdentifier
    tables["result"] = "result_data"+classIdentifier
    tables["subjects"] = "subjects"+classIdentifier
    tables["teachers"] = "teacherstable"+classIdentifier
    tables["classlist"] = "classlist"+classIdentifier
    tables["mastersheet"] = "mastersheet"+str(session["user_id"])+"_"+str(classId)
    tables["subject_position"] = "subject_position"+str(session["user_id"])+"_"+str(classId)
    return tables





