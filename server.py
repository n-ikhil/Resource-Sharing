import os
from flask import Flask, redirect, request, url_for
from flask.helpers import send_from_directory
from flask.templating import render_template
import pymongo
from db import db
app = Flask(__name__)
psql= None
mongo=None

# mydb = mysql.connector.connect(host="localhost",user="postgres",passwd="123",port=5432)


input=None
con=db()
session=[]

@app.route("/users", methods=['GET'])
def users():
    global session
    str=""
    for x in session:
        str=str+"\n"+x
    return str



@app.route("/authorize", methods=['GET'])
def authorize():
    global input,session   
    print(input)
    ans=con.validate_user(input["uid"],input["pwd"])
    if(ans==True):
        session.append(input["uid"])
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))

@app.route("/register",methods=['POST','GET'])
def register_page():
    if(request.method=="GET"):
        return render_template('register.html')
    else:
        input=request.form.to_dict()
        psql.insert(data=input)
        return input
        

@app.route('/login',methods=["GET","POST"])
def login():
    global input
    if(request.method=="GET"):
        return render_template('login_page.html')
    else:
        input=request.form.to_dict()
        return redirect(url_for("authorize"))




#os.system("google-chrome /home/nikhil/Desktop/cs301/project/Faculty-Portal/login_page.html")
if __name__ == "__main__":

    app.debug = True
    app.run('10.42.0.1')
    app.run(debug = True)
