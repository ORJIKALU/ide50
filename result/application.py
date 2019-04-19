import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
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



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

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
    return render_template("classView.html", schoolInfo = schoolrow, classData = classrow, caData = carow, testData = testrow, examData = examrow, subjectData = subjectrow, teachersData = teachersrow,class_list = classlistrow, mastersheet = mastersheet_rows, subject_position = subject_position_row)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM school WHERE username = :username",username=request.form.get("var1").lower())
        # Remember which user has logged in
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("var2")):
            return "fail"
        session["user_id"] = rows[0]["id"]
        schoolId = rows[0]["id"]
        tables = database(str(0))
        schoolClass = tables["classes"]
        classRows = db.execute("SELECT * FROM :classes ",classes = schoolClass)
        # return render portfolio
        return render_template("portfolio.html", schoolInfo = rows, clas = classRows)
    else:
        try:
            session["user_id"]
        except KeyError:
            return render_template("login.html")
        else:
            schoolId = session['user_id']
            tables = database(str(0))
            schoolClass = tables["classes"]
            schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = schoolId)
            classRows = db.execute("SELECT * FROM :classes ",classes = schoolClass)
            # return render portfolio
            return render_template("portfolio.html", schoolInfo = schoolrow, clas = classRows)




@app.route("/")
def index():
    return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return render_template("/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure schoolname was submitted
        if not request.form.get("schoolname"):
            message = "you must provide school name"
            return render_template("register.html", message = message)
        # Ensure schoolname was submitted
        if not request.form.get("surname"):
            message = "you must provide your surname"
            return render_template("register.html", message = message)
        # Ensure schoolname was submitted
        if not request.form.get("firstname"):
            message = "you must provide firstname"
            return render_template("register.html", message = message)
        # Ensure schoolname was submitted
        if not request.form.get("othername"):
            message = "you must provide othername"
            return render_template("register.html", message = message)
        # Ensure email was submitted
        if not request.form.get("address"):
            message = "you must provide school address"
            return render_template("register.html", message = message)
        # Ensure email was submitted
        if not request.form.get("motto"):
            message = "you must provide school motto"
            return render_template("register.html", message = message)
        # Ensure email was submitted
        if not request.form.get("phone"):
            message = "you must provide phone"
            return render_template("register.html", message = message)
        # Ensure email was submitted
        if not request.form.get("email"):
            message = "you must provide school email"
            return render_template("register.html", message = message)

        # Ensure email was submitted
        # Ensure username was submitted
        if not request.form.get("username"):
            message = "you must provide username"
            return render_template("register.html", message = message)
        if (db.execute("SELECT * FROM 'school' WHERE 'username' = :username", username = request.form.get("username"))):
            message = "you must another usernname"
            return render_template("register.html", message = message)
        # Ensure password was submitted
        if not request.form.get("password"):
            message = "you must provide password"
            return render_template("register.html", message = message)
        # Ensure confirmation was submitted
        if not request.form.get("confirmation"):
            message = "you must provide confirmation"
            return render_template("register.html", message = message)
        if not request.form.get("admin_password"):
            message = "you must provide admin password"
            return render_template("register.html", message = message)
        if not request.form.get("admin_password_confirmation"):
            message = "you must provide admin password confirmation"
            return render_template("register.html", message = message)
        if not request.form.get("ca_max"):
            message = "you must provide maximum score for ca "
            return render_template("register.html", message = message)
        if not request.form.get("test_max"):
            message = "you must provide max score for test"
            return render_template("register.html", message = message)
        if not request.form.get("exam_max"):
            message = "you must provide max score for exam"
            return render_template("register.html", message = message)

        if (request.form.get("admin_password") != request.form.get("admin_password_confirmation")):
            message = "admin password and confirmation do not match"
            return render_template("register.html", message = message)

        # Ensure password and confirmation match
        if (request.form.get("password") != request.form.get("confirmation")):
            message = "staff password and confirmation do not match"
            return render_template("register.html", message = message)
        db.execute("INSERT INTO school (school_name, email,username, password,phone_number,address,motto,admin_password,surname, firstname, othername,ca_max, test_max, exam_max) VALUES (:schoolname, :email, :username, :hash, :phone, :address, :motto, :adminPassword, :surname, :firstname, :othername, :ca_max, :test_max, :exam_max)", schoolname = request.form.get("schoolname").upper(), email= request.form.get("email").upper(), username = request.form.get("username").lower(), hash = generate_password_hash(request.form.get("password")), phone = request.form.get("phone"), address = request.form.get("address").upper(), motto = request.form.get("motto").upper(), adminPassword = generate_password_hash(request.form.get("admin_password")), surname = request.form.get("surname"), firstname = request.form.get("firstname"), othername = request.form.get("othername"), ca_max = int(request.form.get("ca_max")), test_max = int(request.form.get("test_max")), exam_max = int(request.form.get("exam_max")))
        # Query database for username
        rows = db.execute("SELECT * FROM school WHERE username = :username",username=request.form.get("username").lower())
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        tables = database(str(1))
        classid = tables["classes"]
        db.execute("CREATE TABLE :classes ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT, 'no_of_students' INTEGER,'passmark' INTEGER,'student_pass' INTEGER,'percent_pass' INTEGER,'subject_pass_mark' INTEGER, 'no_of_subjects' INTEGER, 'surname' TEXT,'firstname' TEXT,'othername' TEXT, 'result_status' TEXT,'history' TEXT,'password' TEXT,'username' TEXT)", classes = classid)
        # return render portfolio
        return render_template("portfolio.html", schoolInfo = rows)
    else:
        return render_template("register.html")

@app.route("/createClass", methods=["GET", "POST"])
@login_required
def createClass():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure schoolname was submitted
        if not request.form.get("className"):
            return apology("must provide classname", 403)
        # Ensure email was submitted
        if not request.form.get("surname"):
            return apology("must provide surname", 403)
        if not request.form.get("firstname"):
            return apology("must provide firstname", 403)
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("must provide email", 403)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirmation was submitted
        if not request.form.get("confirmation"):
            return apology("must confirm password", 403)

        # Ensure password and confirmation match
        if (request.form.get("password") != request.form.get("confirmation")):
            return apology("password and confirmation do not match", 403)
        info["surname"] = request.form.get("surname")
        info["firstname"] = request.form.get("firstname")
        info["othername"] = request.form.get("othername")
        info["username"] = request.form.get("username")
        info["className"] = request.form.get("className")
        info["email"] = request.form.get("email")
        info["noOfStudents"] = request.form.get("noOfStudents")
        info["password"] = request.form.get("password")
        schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = session["user_id"])
        return render_template("classListForm.html",n = int(request.form.get("noOfStudents")), schoolInfo = schoolrow )
    else:
        schoolId = session['user_id']
        schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = schoolId)
        return render_template("createClassForm.html",schoolInfo = schoolrow)

@app.route("/classCreated", methods=["POST"])
@login_required
def classCreated():
    tables = database(str(0))
    schoolClass = tables["classes"]
    db.execute("INSERT INTO :classes (surname,firstname,othername, name, no_of_students, password, no_of_subjects) values (:surname,:firstname,:othername,:className,:noOfStudents,:password, 0)",classes = schoolClass,surname =  info["surname"],firstname =  info["firstname"],othername =  info["othername"], className = info["className"],noOfStudents = info["noOfStudents"],password = generate_password_hash(info["password"]))

    classRow = db.execute("SELECT id FROM :classes where name = :className",classes = schoolClass, className = info["className"])
    classId = classRow[0]["id"]
    tables = database(classId)

    schoolId = tables["school_id"]
    classTable = tables["classlist"]
    db.execute("CREATE TABLE :classlist ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'surname' TEXT,'firstname' TEXT,'othername' TEXT,'sex' TEXT, 'pin' TEXT)",classlist = classTable )
    classSubjects = tables["subjects"]
    db.execute("CREATE TABLE :classsubjects ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT,'ca_max' INTEGER, 'test_max' INTEGER,'exam_max' INTEGER,'total_score' INTEGER,'ppass' INTEGER,'class_average' INTEGER,'ca_sheet' TEXT,'test_sheet' TEXT,'exam_sheet' TEXT,'password' TEXT,'result' TEXT)",classsubjects = classSubjects )
    # create  catable
    caTable =  tables["ca"]
    db.execute("CREATE TABLE :catable ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)",catable = caTable )

    # create testtable
    testTable = tables["test"]
    db.execute("CREATE TABLE :testtable ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)",testtable = testTable )

    # create examtable
    examTable = tables["exam"]
    db.execute("CREATE TABLE :examtable ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)",examtable = examTable )

    # create teacherstable
    teachersTable =  tables["teachers"]
    db.execute("CREATE TABLE :teacherstable ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'surname' TEXT,'firstname' TEXT,'othername' TEXT,'subject' TEXT,'email' TEXT, 'initials' TEXT)",teacherstable = teachersTable )

    # create mastersheet
    mastersheet =  tables["mastersheet"]
    db.execute("CREATE TABLE :mastersheet ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'total_score' INTEGER, 'average' INTEGER, 'passed' INTEGER, 'position' INTEGER )",mastersheet = mastersheet )

    # create subject_position
    subject_position =  tables["subject_position"]
    db.execute("CREATE TABLE :subjectposition ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)",subjectposition = subject_position )

    # create result data
    result =  tables["result"]
    db.execute("CREATE TABLE :resultdata ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'form_remark' TEXT, 'principal_remark' TEXT)",resultdata = result )

    sort_names = []
    # fill classlist
    g = int(info["noOfStudents"])
    for i in range(g):
        surname = "s"+str(i)
        firstname = "f"+str(i)
        othername = "o"+str(i)
        sex = "g"+str(i)

        sort_names.append((request.form.get(surname), request.form.get(firstname), request.form.get(othername), request.form.get(sex)))
    sort_names = sorted(sort_names, key=itemgetter(0))
    for name in sort_names:
                db.execute("INSERT INTO :classtable (surname, firstname, othername,sex) VALUES (:surname, :firstname, :othername,:sex) ",classtable = classTable, surname = name[0].upper(),firstname = name[1].upper(),othername = name[2].upper(),sex=name[3])
                db.execute("INSERT INTO :catable DEFAULT VALUES ",catable = caTable)
                db.execute("INSERT INTO :testtable DEFAULT VALUES ",testtable = testTable)
                db.execute("INSERT INTO :examtable DEFAULT VALUES ",examtable = examTable)
                db.execute("INSERT INTO :mastersheet DEFAULT VALUES ",mastersheet = mastersheet)
                db.execute("INSERT INTO :subject_position DEFAULT VALUES ",subject_position = subject_position)
                db.execute("INSERT INTO :result_data DEFAULT VALUES ",result_data = result)

    rows = db.execute("SELECT * FROM school WHERE id = :school_id",school_id=schoolId)
    classRows = db.execute("SELECT * FROM :classes ",classes = schoolClass)


    # return classlist.html
    return render_template("portfolio.html", schoolInfo = rows, clas= classRows)


@app.route("/submit_score", methods =["POST","GET"])
def submit_score():
	if request.method == "POST":
	    if not request.form.get("subject_name"):
	        return apology("must provide subject name", 403)
	    if not request.form.get("the_class"):
	        return apology("must provide class", 403)
	    if not request.form.get("subject_teacher"):
	        return apology("must provide subject teacher", 403)
	    if not request.form.get("password"):
	        return apology("must provide password", 403)
	    if not request.form.get("confirmation"):
	        return apology("must confirm password", 403)
	    subject_info["subject"] = request.form.get("subject_name")
	    subject_info["surname"] = request.form.get("surname")
	    subject_info["firstname"] = request.form.get("firstname")
	    subject_info["othername"] = request.form.get("othername")
	    subject_info["password"] = request.form.get("password")
	    subject_info["subject_teacher"] = request.form.get("subject_teacher")
	    tables = database(request.form.get("the_class"))
	    current_class = tables["class_id"]
	    current_school = session["user_id"]
	    class_id = tables["classes"]
	    class_row = db.execute("select * from :classid where id = :current_class", classid = class_id, current_class= current_class)
	    class_list = tables["classlist"]
	    schoolId = session['user_id']
	    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = schoolId)
	    class_names = db.execute("select * from :thelist ORDER BY surname", thelist = class_list)
	    return render_template("empty_scoresheet.html",schoolInfo = schoolrow, subject_info = subject_info,class_names = class_names ,classinfo = class_row[0])
	else:
	    tables = database(str(0))
	    classes = tables["classes"]
	    classes = db.execute("SELECT * FROM :classes", classes = classes)
	    schoolId = session['user_id']
	    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = schoolId)
	    return render_template("submit_score_form.html",classes = classes, schoolInfo = schoolrow)


@app.route("/submitted", methods=["POST"])
def submitted():
	tables = database(request.form.get("button"))
	classes = tables["classes"]
	class_list = tables["classlist"]
	cascore_table = tables["ca"]
	test_table = tables["test"]
	exam_table = tables["exam"]
	subject_position = tables["subject_position"]
	mastersheet = tables["mastersheet"]
	teachers_table = tables["teachers"]
	subject_table = tables["subjects"]
	db.execute("INSERT INTO :subjects (name) VALUES (:subject) ",subjects = subject_table, subject = subject_info["subject"])
	db.execute("INSERT INTO :teachers (surname, firstname, othername, subject) VALUES (:surname, :firstname, :othername, :subject )",teachers = teachers_table, surname = subject_info["surname"],firstname = subject_info["firstname"],othername = subject_info["othername"], subject = subject_info["subject"])
	db.execute("ALTER TABLE :cascore_table ADD COLUMN :subject TEXT ", cascore_table = cascore_table, subject = subject_info["subject"])
	db.execute("ALTER TABLE :test_table ADD COLUMN :subject TEXT ", test_table = test_table, subject = subject_info["subject"])
	db.execute("ALTER TABLE :exam_table ADD COLUMN :subject TEXT ", exam_table = exam_table, subject = subject_info["subject"])
	db.execute("ALTER TABLE :subject_p ADD COLUMN :subject TEXT", subject_p = subject_position, subject = subject_info["subject"])
	db.execute("ALTER TABLE :mastersheet ADD COLUMN :subject TEXT ", mastersheet = mastersheet, subject = subject_info["subject"])
	db.execute("UPDATE :classes SET no_of_subjects = no_of_subjects + 1 WHERE id = :id", classes = classes, id =tables["class_id"])
	class_list_row = db.execute("SELECT * FROM :classlist", classlist = class_list)
	rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
	for  student in class_list_row:
	    cascore = "cascore"+ str(student["id"])
	    testscore = "testscore"+str(student["id"])
	    examscore = "examscore"+str(student["id"])
	    ca_score = request.form.get(cascore)
	    test_score = request.form.get(testscore)
	    exam_score = request.form.get(examscore)
	    db.execute("UPDATE :catable SET :subject = :score WHERE id =:id", catable = cascore_table, subject = subject_info["subject"],score =ca_score, id = student["id"])
	    db.execute("UPDATE :testtable SET :subject = :score WHERE id =:id", testtable = test_table, subject = subject_info["subject"],score =test_score, id = student["id"])
	    db.execute("UPDATE :examtable SET :subject = :score WHERE id =:id", examtable = exam_table, subject = subject_info["subject"],score =exam_score, id = student["id"])
	rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
	classrows = db.execute("SELECT * FROM :classes ", classes = classes)
	return render_template("portfolio.html", schoolInfo = rows, clas = classrows)



@app.route("/make_result", methods=["POST"])
def make_result():
	class_id = request.form.get("result")
	tables = database(class_id)
	classes = tables["classes"]
	class_list = tables["classlist"]
	cascore_table = tables["ca"]
	test_table = tables["test"]
	exam_table = tables["exam"]
	subject_position =tables["subject_position"]
	master_sheet = tables["mastersheet"]
	teachers_table = tables["teachers"]
	subject_table = tables["subjects"]

	student_position = []
	students = db.execute("SELECT * FROM :classlist", classlist = class_list)
	subjects = db.execute("SELECT * FROM :subject", subject = subject_table)
	classroom = db.execute("SELECT * FROM :classes WHERE id = :class_id", classes = classes, class_id= int(class_id))
	no_0f_subjects = classroom[0]["no_of_subjects"]
	for student in students:
		total_score = 0
		student_average = 0
		ca_row = db.execute("SELECT * FROM :catable WHERE id=:id  ", catable = cascore_table, id = student["id"])
		test_row = db.execute("SELECT * FROM :testtable WHERE id=:id  ", testtable = test_table, id = student["id"])
		exam_row = db.execute("SELECT * FROM :examtable WHERE id=:id ", examtable = exam_table, id = student["id"])
		for subject in subjects:
			sub_total = 0
			if ca_row[0][subject["name"]]:
				sub_total = sub_total + int(ca_row[0][subject["name"]])
			if test_row[0][subject["name"]]:
				sub_total = sub_total + int(test_row[0][subject["name"]])
			if exam_row[0][subject["name"]]:
				sub_total = sub_total + int(exam_row[0][subject["name"]])

			db.execute("UPDATE :mastersheet SET :subject = :sub_total WHERE id = :id ", mastersheet = master_sheet, subject = subject["name"], sub_total =  sub_total, id = student["id"])
			total_score = total_score + sub_total
		db.execute("UPDATE :mastersheet SET total_score = :total_score WHERE id = :id  ", mastersheet = master_sheet, total_score = total_score, id = student["id"])
		student_average = total_score / classroom[0]["no_of_subjects"]
		db.execute("UPDATE :mastersheet SET average = :student_average WHERE id = :id  ", mastersheet = master_sheet, student_average = student_average, id = student["id"])
		student_position.append((student["id"], student_average))

	mastersheet_data = db.execute("SELECT * FROM :master_sheet", master_sheet = master_sheet)
	for subject in subjects:
		sort_subject_position = []
		subject_total = 0
		for student in mastersheet_data:
			total = db.execute("SELECT * FROM :master_shit WHERE id=:id", master_shit = master_sheet, id = student["id"])
			subject_total = subject_total + int(total[0][subject["name"]])
			sort_subject_position.append((student["id"], int(total[0][subject["name"]])))
		sort_subject_position = sorted(sort_subject_position, key = itemgetter(1), reverse=True)
		i = 0
		j = 0
		previous = 101
		for person in sort_subject_position:
		    if previous == person[1]:
			    db.execute("UPDATE :subject_positon SET :subject = :position  WHERE id =:id", subject_positon = subject_position, subject = subject["name"], position = j, id = person[0])
		    else:
			    j = i + 1
			    db.execute("UPDATE :subject_positon SET :subject = :position  WHERE id =:id", subject_positon = subject_position, subject = subject["name"], position = j, id = person[0])
		    i = i + 1
		    previous = person[1]

		subject_average = subject_total / classroom[0]["no_of_students"]
		db.execute("UPDATE :subjects SET class_average = :average WHERE id = :id", subjects = subject_table,  average = subject_average, id = subject["id"] )
	student_position = sorted(student_position, key = itemgetter(1), reverse=True)
	j = 0;
	for person in student_position:
		db.execute("UPDATE :mastersheet SET position = :position  WHERE id =:id", mastersheet = master_sheet,  position = j + 1, id = person[0])
		j = j + 1
	classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
	schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
	carow = db.execute("SELECT * FROM :catable",catable = tables["ca"])
	testrow = db.execute("SELECT * FROM :testtable",testtable = tables["test"])
	examrow = db.execute("SELECT * FROM :examtable",examtable = tables["exam"])
	subjectrow = db.execute("SELECT * FROM :subjecttable",subjecttable = tables["subjects"])
	teachersrow = db.execute("SELECT * FROM :teacherstable",teacherstable = tables["teachers"])
	classlistrow = db.execute("SELECT * FROM :classlist",classlist = tables["classlist"])
	mastersheet_rows = db.execute("SELECT * FROM :mastersheet", mastersheet = tables["mastersheet"])
	subject_position_row = db.execute("SELECT * FROM :subject_position", subject_position = tables["subject_position"])
	return render_template("classView.html", schoolInfo = schoolrow, classData = classrow, caData = carow, testData = testrow, examData = examrow, subjectData = subjectrow, teachersData = teachersrow,class_list = classlistrow, mastersheet = mastersheet_rows, subject_position = subject_position_row)

@app.route("/login_check", methods=["POST"])

def login_check():
    if request.method == "POST":
        # Query database for username
        rows = db.execute("SELECT * FROM school WHERE username = :username",username=request.form.get("username").lower())
        # Remember which user has logged in
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return "fail"
        else:
            return jsonify({"username": request.form.get("username"), "password": request.form.get("password")})




@app.route("/register_check", methods=["POST"])
def register_check():
    if request.method == "POST":
        # Query database for username
        rows = db.execute("SELECT * FROM school WHERE username = :username",username=request.form.get("username").lower())
        if len(rows) == 0:
            return "true"
        else:
            return "false"

@app.route("/result_sheet", methods=["POST"])
def result_sheet():
    array_id = str(request.form.get("result_sheet")).split("_")
    student_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    carow = db.execute("SELECT * FROM :catable where id=:id",catable = tables["ca"], id= student_id)
    testrow = db.execute("SELECT * FROM :testtable where id=:id",testtable = tables["test"], id= student_id)
    examrow = db.execute("SELECT * FROM :examtable where id=:id",examtable = tables["exam"], id= student_id)
    subjectrow = db.execute("SELECT * FROM :subjecttable",subjecttable = tables["subjects"])
    teachersrow = db.execute("SELECT * FROM :teacherstable",teacherstable = tables["teachers"])
    classlistrow = db.execute("SELECT * FROM :classlist where id=:id",classlist = tables["classlist"], id=student_id)
    mastersheet_rows = db.execute("SELECT * FROM :mastersheet where id=:id", mastersheet = tables["mastersheet"], id= student_id)
    subject_position_row = db.execute("SELECT * FROM :subject_position where id=:id", subject_position = tables["subject_position"], id= student_id)
    return render_template("result_sheet.html", schoolInfo = schoolrow, classData = classrow, caData = carow, testData = testrow, examData = examrow, subjectData = subjectrow, teachersData = teachersrow,class_list = classlistrow, mastersheet = mastersheet_rows, subject_position = subject_position_row)

@app.route("/scoresheet", methods=["POST"])
def scoresheet():
    array_id = str(request.form.get("scoresheet")).split("_")
    subject_id = int(array_id[0])
    class_id = int(array_id[1])
    tables=database(class_id)
    student_row = db.execute("SELECT * FROM :classlist", classlist=tables["classlist"])
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    carow = db.execute("SELECT * FROM :catable",catable = tables["ca"])
    testrow = db.execute("SELECT * FROM :testtable",testtable = tables["test"])
    examrow = db.execute("SELECT * FROM :examtable",examtable = tables["exam"])
    subjectrow = db.execute("SELECT * FROM :subjecttable WHERE id=:id",subjecttable = tables["subjects"], id=subject_id)
    teachersrow = db.execute("SELECT * FROM :teacherstable",teacherstable = tables["teachers"])
    classlistrow = db.execute("SELECT * FROM :classlist",classlist = tables["classlist"])
    mastersheet_rows = db.execute("SELECT * FROM :mastersheet", mastersheet = tables["mastersheet"])
    subject_position_row = db.execute("SELECT * FROM :subject_position", subject_position = tables["subject_position"])
    return render_template("scoresheet.html",sub_id=subject_id, schoolInfo = schoolrow, classData = classrow, caData = carow, testData = testrow, examData = examrow, subjectData = subjectrow, teachersData = teachersrow,class_list = classlistrow, mastersheet = mastersheet_rows, subject_position = subject_position_row)


@app.route("/edit_scoresheet", methods=["POST"])
def edit_scoresheet():
    password = request.form.get("password")
    array_id = str(request.form.get("edit_scoresheet")).split("_")
    subject_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    if check_password_hash(classrow[0]["password"], password) or check_password_hash(schoolrow[0]["admin_password"], password ):
        carow = db.execute("SELECT * FROM :catable",catable = tables["ca"])
        testrow = db.execute("SELECT * FROM :testtable",testtable = tables["test"])
        examrow = db.execute("SELECT * FROM :examtable",examtable = tables["exam"])
        subjectrow = db.execute("SELECT * FROM :subjecttable WHERE id=:id",subjecttable = tables["subjects"], id=subject_id)
        teachersrow = db.execute("SELECT * FROM :teacherstable",teacherstable = tables["teachers"])
        classlistrow = db.execute("SELECT * FROM :classlist",classlist = tables["classlist"])
        mastersheet_rows = db.execute("SELECT * FROM :mastersheet", mastersheet = tables["mastersheet"])
        subject_position_row = db.execute("SELECT * FROM :subject_position", subject_position = tables["subject_position"])
        return render_template("edit_scoresheet.html",sub_id=subject_id, schoolInfo = schoolrow, classData = classrow, caData = carow, testData = testrow, examData = examrow, subjectData = subjectrow, teachersData = teachersrow,class_list = classlistrow, mastersheet = mastersheet_rows, subject_position = subject_position_row)
    else:
        classrow = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
        return render_template("portfolio.html", schoolInfo = schoolrow, clas = classrow)






@app.route("/edited_scoresheet", methods=["POST"])
def edited_scoresheet():
    array_id = str(request.form.get("edited_scoresheet")).split("_")
    subject_id = int(array_id[0])
    class_id = int(array_id[1])
    tables = database(class_id)
    classes = tables["classes"]
    class_list = tables["classlist"]
    cascore_table = tables["ca"]
    test_table = tables["test"]
    exam_table = tables["exam"]
    subject_position = tables["subject_position"]
    mastersheet = tables["mastersheet"]
    teachers_table = tables["teachers"]
    subject_table = tables["subjects"]
    class_list_row = db.execute("SELECT * FROM :classlist", classlist = class_list)
    subject_row = db.execute("SELECT * FROM :subjects WHERE id=:id", subjects=subject_table, id=subject_id)

    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])


    for  student in class_list_row:
        cascore = "cascore"+ str(student["id"])
        testscore = "testscore"+str(student["id"])
        examscore = "examscore"+str(student["id"])
        ca_score = request.form.get(cascore)
        test_score = request.form.get(testscore)
        exam_score = request.form.get(examscore)
        db.execute("UPDATE :catable SET :subject = :score WHERE id =:id", catable = cascore_table, subject = subject_row[0]["name"],score =ca_score, id = student["id"])
        db.execute("UPDATE :testtable SET :subject = :score WHERE id =:id", testtable = test_table, subject = subject_row[0]["name"],score =test_score, id = student["id"])
        db.execute("UPDATE :examtable SET :subject = :score WHERE id =:id", examtable = exam_table, subject = subject_row[0]["name"],score =exam_score, id = student["id"])

    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
    classrows = db.execute("SELECT * FROM :classes ", classes = classes)
    return render_template("portfolio.html", schoolInfo = rows, clas = classrows)



@app.route("/delete_scoresheet", methods=["POST"])
def delete_scoresheet():
    array_id = str(request.form.get("delete_scoresheet")).split("_")
    subject_id = int(array_id[0])
    class_id = int(array_id[1])
    tables = database(class_id)
    classes = tables["classes"]
    class_list = tables["classlist"]
    cascore_table = tables["ca"]
    test_table = tables["test"]
    exam_table = tables["exam"]
    subject_position = tables["subject_position"]
    mastersheet = tables["mastersheet"]
    teachers_table = tables["teachers"]
    subject_table = tables["subjects"]
    class_list_row = db.execute("SELECT * FROM :classlist", classlist = class_list)

    subject_row = db.execute("SELECT * FROM :subjects WHERE id=:id", subjects=subject_table, id=subject_id)

    db.execute("ALTER TABLE :cascore DROP COLUMN   :subject_name", cascore=cascore_table, subject_name=subject_row[0]["name"])
    db.execute("ALTER TABLE :testscore DROP COLUMN :subject", testscore=test_table, subject=subject_row[0]["name"] )
    db.execute("ALTER TABLE :examscore DROP COLUMN :subject", examscore=exam_table, subject=subject_row[0]["name"] )
    db.execute("ALTER TABLE :mastersheet DROP COLUMN :subject", mastersheet=mastersheet, subject=subject_row[0]["name"] )
    db.execute("ALTER TABLE :subject_p DROP COLUMN :subject", subject_p=subject_position, subject=subject_row[0]["name"] )
    db.execute("DELETE FROM :teachers WHERE subject=:subject", teachers=teachers_table, subject=subject_row[0]["name"])
    db.execute("DELETE FROM :subject WHERE id=:id", subjects=subject_table, id=subject_row[0]["id"])
    db.execute("UPDATE :classes set no_of_subjects = no_of_subjects - 1 WHERE id=:id", classes=classes, id=class_id)

    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
    classrows = db.execute("SELECT * FROM :classes ", classes = classes)
    return render_template("portfolio.html", schoolInfo = rows, clas = classrows)

@app.route("/verify_scoresheet", methods=["POST"])
def verify_scoresheet():
    array_id = str(request.form.get("edit_scoresheet")).split("_")
    subject_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    subjectrow = db.execute("SELECT * FROM :subjecttable WHERE id=:id",subjecttable = tables["subjects"], id=subject_id)
    return render_template("verify_scoresheet.html",sub_id=subject_id,  classData = classrow, schoolInfo=schoolrow)

@app.route("/verify_teacher", methods=["POST"])
def verify_teacher():
    array_id = str(request.form.get("edit_student")).split("_")
    student_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    classlist = db.execute("SELECT * FROM :classlist WHERE id=:id",classlist = tables["classlist"], id=student_id)
    return render_template("verify_teacher.html",id=student_id,  classData = classrow, schoolInfo=schoolrow)

@app.route("/edit_student", methods=["POST"])
def edit_student():
    password = request.form.get("password")
    array_id = str(request.form.get("edit_student")).split("_")
    student_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    if check_password_hash(classrow[0]["password"], password) or check_password_hash(schoolrow[0]["admin_password"], password ):
        studentrow = db.execute("SELECT * FROM :classlist WHERE id=:id", classlist=tables["classlist"], id=student_id)
        return render_template("edit_student.html",id=student_id, schoolInfo = schoolrow, classData=classrow,student=studentrow[0])
    else:
        classrow = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
        return render_template("portfolio.html", schoolInfo = schoolrow, clas = classrow)


@app.route("/edited_student", methods=["POST"])
def edited_student():
    array_id = str(request.form.get("edit_student")).split("_")
    student_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    surname = "s"+str(student_id)
    firstname = "f"+str(student_id)
    othername = "o"+str(student_id)
    sex = "g"+str(student_id)
    db.execute("UPDATE :classlist SET surname = :surname, firstname=:firstname, othername=:othername, sex=:sex WHERE id =:student_id", classlist = tables["classlist"], surname = request.form.get(surname).upper(),firstname =request.form.get(firstname).upper(), othername = request.form.get(othername).upper(), sex=request.form.get(sex), student_id= student_id)
    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
    classrows = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
    return render_template("portfolio.html", schoolInfo = rows, clas = classrows)

@app.route("/unregister_student", methods=["POST"])
def unregister_student():
    array_id = str(request.form.get("unregister_student")).split("_")
    student_id = int(array_id[0])
    class_id = int(array_id[1])
    tables= database(class_id)
    db.execute("DELETE  FROM :ca where id=:id", ca = tables["ca"], id=student_id)
    db.execute("DELETE  FROM :test where id=:id", test = tables["test"], id=student_id)
    db.execute("DELETE  FROM :exam where id=:id", exam = tables["exam"], id=student_id)
    db.execute("DELETE  FROM :mastersheet where id=:id", mastersheet = tables["mastersheet"], id=student_id)
    db.execute("DELETE  FROM :subject_position where id=:id", subject_position = tables["subject_position"], id=student_id)
    db.execute("DELETE  FROM :result where id=:id", result= tables["result"], id=student_id)
    db.execute("DELETE  FROM :classlist where id=:id", classlist = tables["classlist"], id=student_id)
    db.execute("UPDATE :classes SET no_of_students= no_of_students - 1 where id=:id",classes = tables["classes"], id=class_id)



    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
    classrows = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
    return render_template("portfolio.html", schoolInfo = rows, clas = classrows)

@app.route("/verify_add_student", methods=["POST"])
def verify_add_student():
   class_id = str(request.form.get("add_student"))
   tables= database(class_id)
   classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
   schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
   return render_template("verify_add_student.html", classData = classrow, schoolInfo=schoolrow)


@app.route("/verified_add_student", methods=["POST"])
def verified_add_student():
    password = request.form.get("password")
    class_id = request.form.get("verify_add_student")
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    if check_password_hash(classrow[0]["password"], password) or check_password_hash(schoolrow[0]["admin_password"], password ):
        return render_template("add_student.html", schoolInfo = schoolrow, classData=classrow)
    else:
        classrow = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
        return render_template("portfolio.html", schoolInfo = schoolrow, classData = classrow)

@app.route("/student_added", methods=["POST"])
def student_added():
    class_id = request.form.get("class_id")
    tables= database(class_id)
    db.execute("INSERT INTO :classlist (surname, firstname, othername, sex) VALUES (:surname, :firstname, :othername, :sex)", classlist=tables["classlist"], surname= request.form.get("surname").upper(), firstname=request.form.get("firstname").upper(), othername=request.form.get("othername").upper(), sex=request.form.get("sex"))
    db.execute("INSERT INTO :catable DEFAULT VALUES ",catable = tables["ca"])
    db.execute("INSERT INTO :testtable DEFAULT VALUES ",testtable = tables["test"])
    db.execute("INSERT INTO :examtable DEFAULT VALUES ",examtable = tables["exam"])
    db.execute("INSERT INTO :mastersheet DEFAULT VALUES ",mastersheet = tables["mastersheet"])
    db.execute("INSERT INTO :subject_position DEFAULT VALUES ",subject_position = tables["subject_position"])
    db.execute("INSERT INTO :result_data DEFAULT VALUES ",result_data = tables["result"])
    db.execute("UPDATE :classes SET no_of_students = no_of_students + 1", classes =tables["classes"])
    rows = db.execute("SELECT * FROM school WHERE id = :school_id",school_id=tables["school_id"])
    classRows = db.execute("SELECT * FROM :classes ",classes = tables["classes"])


    # return classlist.html
    return render_template("portfolio.html", schoolInfo = rows, clas= classRows)

@app.route("/edit_class", methods=["POST"])
def edit_class():
   class_id = request.form.get("edit_class")
   tables= database(class_id)
   classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = class_id)
   schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
   return render_template("verify_admin.html", classData = classrow, schoolInfo=schoolrow)


@app.route("/verified_admin", methods=["POST"])
def verified_admin():
    class_id = request.form.get("class_id")
    password = request.form.get("password")
    tables= database(class_id)
    classrow = db.execute("SELECT * FROM :classes WHERE id = :classId", classes = tables["classes"], classId = tables["class_id"])
    schoolrow = db.execute("SELECT * FROM school WHERE id = :schoolId", schoolId = tables["school_id"])
    if check_password_hash(schoolrow[0]["admin_password"], password ):
        return render_template("edit_class.html", schoolInfo = schoolrow, classData=classrow)
    else:
        rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
        classrows = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
        return render_template("portfolio.html", schoolInfo = rows, clas = classrows)

@app.route("/edited_class", methods=["POST"])
def edited_class():
    class_id = request.form.get("id")
    tables= database(class_id)
    if  request.form.get("firstname") != " ":
        db.execute("UPDATE :classes set firstname=:firstname where id=:id", classes = tables["classes"], firstname=request.form.get("firstname").upper(), id = tables["class_id"])
    if(request.form.get("surname") != ""):
        db.execute("UPDATE :classes set surname=:surname where id=:id", classes = tables["classes"], surname=request.form.get("surname").upper(), id = tables["class_id"])
    if(request.form.get("othername") != ""):
        db.execute("UPDATE :classes set othername=:othername where id=:id", classes = tables["classes"], othername=request.form.get("othername").upper(), id = tables["class_id"])
    if(request.form.get("class_name") != ""):
        db.execute("UPDATE :classes set name=:name where id=:id", classes = tables["classes"], name=request.form.get("class_name").upper(), id = tables["class_id"])
    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
    classrows = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
    return render_template("portfolio.html", schoolInfo = rows, clas = classrows)

@app.route("/delete_class", methods=["POST"])
def delete_class():
    class_id = request.form.get("delete_class")
    tables= database(class_id)
    db.execute("DROP TABLE :cascore", cascore= tables["ca"])
    db.execute("DROP TABLE :test", test= tables["test"])
    db.execute("DROP TABLE :exam", exam= tables["exam"])
    db.execute("DROP TABLE :mastersheet", mastersheet= tables["mastersheet"])
    db.execute("DROP TABLE :subject_position", subject_position= tables["subject_position"])
    db.execute("DROP TABLE :result", result= tables["result"])
    db.execute("DROP TABLE :classlist", classlist= tables["classlist"])
    db.execute("DROP TABLE :teachers", teachers= tables["teachers"])
    db.execute("DROP TABLE :subjects", subjects= tables["subjects"])
    db.execute("DELETE  FROM :classes where id=:id", classes= tables["classes"], id=tables["class_id"])
    # db.execute("UPDATE schools set no_of_classes = no_of_classes - 1 where id=:id" id=tables["class_id"])
    rows = db.execute("SELECT * FROM school WHERE id = :school_id ",school_id = session["user_id"])
    classrows = db.execute("SELECT * FROM :classes ", classes = tables["classes"])
    return render_template("portfolio.html", schoolInfo = rows, clas = classrows)





def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:

    app.errorhandler(code)(errorhandler)
