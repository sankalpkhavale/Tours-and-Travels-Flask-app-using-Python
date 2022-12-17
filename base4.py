from flask import *
from database import *

app=Flask(__name__)

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome page.html")

@app.route("/details")
def details():
    d=displayrec()
    return render_template("details page.html",elist=d)

@app.route("/mybookedtrips")
def bookedtripsrectoshow():
    fname=request.args.get("fname10")
    xyz=bookedtripsrec(fname)
    return render_template("my booked trips.html",etours=xyz,fname=fname)

@app.route("/register")
def register():
    return render_template("registraion page.html")

#bookpage
@app.route("/bookingpage")
def bookingpage():
    book_trip=request.args.get("email")
    info=onbookpagedisplayinfousing(book_trip)
    return render_template("booking page.html",ebooks=info)


@app.route("/insert",methods=["post"])
def ins():
    fname=request.form["fname"]
    lname=request.form["lname"]
    email=request.form["email"]
    password=request.form["password"]
    contact=request.form["contact"]
    address=request.form["address"]
    t=(fname,lname,email,password,contact,address)
    f=(email,int(contact))
    print(f)
    t2=duplrec(email)
    print(t2)
    if f in t2:
        return redirect("/login")
    else:
        insertrec(t)
        createtable(fname)
        return render_template("congrats.html",fname=fname)
    
@app.route("/login")
def login():
    return render_template("login page.html")

@app.route("/log",methods=["post"])
def log():
    email=request.form["email1"]
    password=request.form["password1"]
    contact=request.form['contact1']
    t=(email,int(contact),password)
    print(t)
    t1=selectrec(email)
    getemail=displayrecemail(email)
    print(t1)
    z=showalltrips()
    if t in t1:
        return render_template("trips page.html",getemail=getemail,etrips=z)
    else:
        return redirect("/login")

@app.route("/delete")
def dele():
    fn=request.args.get("fn")
    am=request.args.get("loc")
    t=(am,)
    t1=t[0]
    #print(fn)
    #print(am)
    #print(type(fn))
    #print(type(fn))
    deleterec2(fn,t1)
    return redirect("/welcome")


@app.route("/alltrips")
def alltrips():
    z=showalltrips()
    return render_template("trips page.html",etrips=z)

@app.route("/logout")
def logout():
    return render_template("welcome page.html")

@app.route("/addingtriptoyourtable",methods=["post"])
def addtrip():
    fname=request.form["fname"]
    location=request.form["location"]
    trip_date=request.form["trip_date"]
    amount=request.form["amount"]    
    t=(location,trip_date,amount)
    addingthistriptoyourtable(fname,t)
    return render_template("congrats.html",fname=fname)

@app.route("/congo")
def congotoyou():
    return render_template("congrats.html")

@app.route("/edityourdetails")
def ed():
    fname=request.args.get('fname11')
    pqr=sel(fname)
    return render_template("edit your details page.html",euser=pqr)

@app.route("/update",methods=["post"])
def up():
    fname=request.form["fname"]
    lname=request.form["lname"]
    email=request.form["email"]
    password=request.form["password1"]
    contact=request.form["contact"]
    address=request.form["address"]
    t5=(lname,email,password,contact,address,fname)
    print(t5)
    updaterec(t5)
    return redirect("/welcome")




if __name__=="__main__":
    app.run(debug=True,port=8888)