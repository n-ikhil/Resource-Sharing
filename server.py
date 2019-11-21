import os
from flask import Flask, redirect, request, url_for, session
# from flask.ext.session import Session
from flask.helpers import send_from_directory
from flask.templating import render_template
import pymongo
from db import db
app = Flask(__name__)
app.secret_key = "whatisthis"
psql= None
mongo=None

# mydb = mysql.connector.connect(host="localhost",user="postgres",passwd="123",port=5432)


input=None
con=db()





@app.route("/users", methods=['GET'])
def users():
    str=""
    return str

@app.route("/dashboard", methods=['GET'])
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html',name=session['username'])
    else:
        return redirect(url_for("login"))


@app.route("/notein", methods=['GET','POST'])
def notein():
    if 'username' in session:
        qu={"tog":3,"name":session['username']}
        ans=con.get_details(qu)
        return render_template("requestsin.html",prods=ans,len=len(ans),flag1="readonly",default="",
            flag2="readonly",
            flag3="readonly",
            flag4="true",       
            flag5="readonly",
            flag6="readonly",
            flag7="none"            
            )
    else:
        return redirect(url_for("login"))

@app.route("/noteout", methods=['GET','POST'])
def notout():
    if 'username' in session:
        qu={"tog":0,"name":session['username']}
        ans=con.get_details(qu)
        return render_template("requests.html",prods=ans,current=session['username'],len=len(ans),flag1="readonly",default="",
            flag2="readonly",
            flag3="readonly",
            flag4="true",
            flag5="readonly",
            flag6="readonly",
            flag7="none"            
            )
    else:
        return redirect(url_for("login"))

@app.route("/ledged", methods=['GET','POST'])
def ledgedt():
    if 'username' in session:
        qu={"tog":2,"name":session['username']}
        ans=con.get_details(qu)
        return render_template("requests.html",prods=ans,current=session['username'],len=len(ans),flag1="readonly",default="",
            flag2="readonly",
            flag3="readonly",
            flag4="true",
            flag5="readonly",
            flag6="readonly",
            flag7="none"            
            )
    else:
        return redirect(url_for("login"))
    


@app.route("/requests", methods=['GET','POST'])
def crequest():
    if 'username' in session:
        if(request.method=='GET'):        
            #
            return render_template("request.html")
        else:
            input=request.form.to_dict()
            input["tog"]=1
            print(input)
            ans=con.get_details(input)
            return render_template("requests.html",prods=ans,current=session['username'],len=len(ans),flag1="readonly",default="",
            flag2="readonly",
            flag3="readonly",
            flag4="false",
            flag5="readonly",
            flag6="readonly",
            flag7="none"            
            )
    else:
            return redirect(url_for("login"))
    

@app.route("/modify<temp>", methods=['GET','POST'])
def modify(temp):
    if 'username' in session:
        if(request.method=='GET'):
        
            ans=con.get_all(session['username'])
            sample=session['username']
            print(1)
            return render_template("products.html",prods=ans,len=len(ans),flag1="readonly",default=sample,
            flag2="readonly",
            flag3="false",
            flag4="false",
            flag5="false",
            flag6="readonly",
            flag7="false"            
            )

        else:
            
            dict=request.form.to_dict()
            if(temp=="a"):
                print("wanting")
                con.add_product(dict)
                return redirect(url_for("dashboard"))
            else:
                con.update_product(dict)
            return redirect(url_for("dashboard"))
                
    else:
        return redirect(url_for("login"))
    

@app.route("/notification", methods=['GET','POST'])
def notification():
    if(request.method=='GET'):
        if 'username' in session:
            #
            return render_template("request.html")
        else:
            return redirect(url_for("login"))
    else:
        return "wait"


    

# @app.route("/modify", methods=['GET','POST'])
# def request():


# @app.route("/not", methods=['GET','POST'])
# def request():


@app.route("/test", methods=['GET'])
def test():
    temp={"owner":"nikhil","price":"12"}
    li=[]
    li.append(temp)
    return render_template("products.html",len=1,prods=li,flag="true")

@app.route("/authorize", methods=['GET'])
def authorize():
    
    global input
    print(input)
    ans=con.validate_user(input["uid"],input["pwd"])
    if(ans==True):
        session['username']=input["uid"]
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))

@app.route("/register",methods=['POST','GET'])
def register_page():
    if(request.method=="GET"):
        return render_template('register.html')
    else:
        input=request.form.to_dict()
        print(input)
        con.add_user(input)
        session['username']=input["name"]
        return redirect(url_for("dashboard"))

@app.route('/logout',methods=["GET","POST"])
def logout():
    session.pop('username',None)
    return redirect(url_for("login"))


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
    app.run()
    app.run(debug = True)
