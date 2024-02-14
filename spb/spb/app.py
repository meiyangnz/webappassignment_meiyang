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
    SELECT j.job_id, CONCAT(c.first_name, '', c.family_name) AS customer_name, j.job_date
    FROM job jobList
    JOIN customer c ON j.customer = c.customer_id
    WHERE j.completed = 0;
    "")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("currentjoblist.html", job_list = jobList)    

@app.route("/job/<int:job_id>",methods=['GET','POST'])
def job_details(job_id):
    conn = get_db_connection()
    cursor = con.cursor()
    if request.method == 'POST':
        pass

    cursor.execute("SELECT * FROM job Where job_id = %s", (job_id))
    job = cursor.fetchone()

    #fetch parts and services related to this job

    cursor.close()
    conn.close()
    return render_template("job_details.html", job=job)

# Admin Interface Routes

@app.route ("/addcustomer", methods = ['GET','POST'])

def add_customer():
    if request.method == 'POST':
        # Handle new customer addition
        first_name = request.form['first_name']
        family_name = request.form['family_name']
        email = request.form['email']
        phone = request.form['phone']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customer (first_name, family_name, email, phone) VALUES (%s, %s, %s, %s)",
                       (first_name, family_name, email, phone))
        cursor.close()
        conn.close()
        flash('Customer added successfully!')
        return redirect(url_for('add_customer'))
    return render_template("add_customer.html")

# Add routes for adding services, parts, managing jobs etc. as per your project needs

if __name__ == "__main__":
    app.run(debug=True)

def admin_home():
    return render_template('admin_home.html')


@app.route('/currentjobs')
def current_jobs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT j.job_id, CONCAT(c.first_name, ' ', c.family_name) AS customer_name, j.job_date
        FROM job j
        JOIN customer c ON j.customer_id = c.customer_id
        WHERE j.completed = 0
        ORDER BY j.job_date DESC;
    """)
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('current_jobs.html', current_jobs=jobs)

@app.route('/job/<int:job_id')
def job_details(job_id):
    return render_template('job_details.html', job=job,job_services=job_services,job_parts=job_parts, all_services=all_services, all_parts=all_parts)
