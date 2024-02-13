from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

dbconn = None
connection = None

def get_db_connection():
    connection = mysql.connector.connect(user=connect.dbuser,
                                         password=connect.dbpass,
                                         host=connect.dbhost,
                                         database=connect.dbname,
                                         autocommit=True)
    return connection

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
def home():
    return redirect(url_for("/currentjobs"))

@app.route("/currentjobs")
def currentjobs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""
    SELECT j.job_id, CONTACT(c.first_name, '', c.family_name) AS customer_name, j.job_date
    FROM job jobList
    JOIN customer c ON j.customer = c.customer_id
    WHERE j.completed = 0;
    "")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    connection = getCursor()
    connection.execute("SELECT job_id,customer,job_date FROM job where completed=0;")
    jobList = connection.fetchall()
    return render_template("currentjoblist.html", job_list = jobList)    



