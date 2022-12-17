import pymysql as p

def getconnection():
    return p.connect(host='localhost',user='root',password='',database='flask_project')

#createtable of every register people
def createtable(table_name):
    db=getconnection()
    cr=db.cursor()
    sql=f'create table {table_name} (my_booktrip varchar(40),bookingdate datetime default now(),trip_date date,amount int)'
    cr.execute(sql)
    db.commit()
    db.close()
    print('table created')








#inserting records;
t=('Rushi','shinde','rushi@gmai.com','1234',9875632145,'Ghansoli')
def insertrec(t):
    db=getconnection()
    cr=db.cursor()
    sql='insert into user_table (fname,lname,email,password,contact,address) values(%s,%s,%s,%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()


#showing records
def displayrec():
    db=getconnection()
    cr=db.cursor()
    sql='select * from user_table'
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()  
    return data 

#lets select rec using email
def selectrec(email):
    db=getconnection()
    cr=db.cursor()
    sql='select email,contact,password from user_table where email=%s'
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

#duplicate rec try
def duplrec(email):
    db=getconnection()
    cr=db.cursor()
    sql='select email,contact from user_table where email=%s'
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

#displaying upcoming trip using display trip table
def showalltrips():
    db=getconnection()
    cr=db.cursor()
    sql='select * from trip_table'
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()  
    return data

#on booking page we need details of login user to get that we need this function
def bookingtable_sel(email):
    db=getconnection()
    cr=db.cursor()
    sql="select fname,contact from user_table where email=%s"
    cr.execute(sql,email)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

def displayrecemail(email1):
    db=getconnection()
    cr=db.cursor()
    sql="select * from user_table where email=%s"
    cr.execute(sql,email1)
    data=cr.fetchall()
##    print(data)
#  for tup in data:
 #       print(tup)
    db.commit()
    db.close()
    return data

def onbookpagedisplayinfousing(loaction):
    db=getconnection()
    cr=db.cursor()
    sql="select * from trip_table where trip_location=%s"
    cr.execute(sql,loaction)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0] #data[0] cause it will return us single value tuple

def addingthistriptoyourtable(fname,t):
    db=getconnection()
    cr=db.cursor()
    sql=f'insert into {fname} (my_booktrip,trip_date,amount) values (%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()

#to display your booked trips
def bookedtripsrec(fname):
    db=getconnection()
    cr=db.cursor()
    sql=f'select * from {fname}'
    cr.execute(sql)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data


def sel(fname):
    db=getconnection()
    cr=db.cursor()
    sql="select * from user_table where fname=%s"
    cr.execute(sql,fname)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data[0] #data[0] cause it will return us single value tuple
#lets try to update the usertable using fname;
def updaterec(t1):
    db=getconnection()
    cr=db.cursor()
    sql='update user_table set lname=%s,email=%s,password=%s,contact=%s,address=%s where fname=%s'
    cr.execute(sql,t1)
    db.commit()
    db.close()

#removing booked trips from my booking
def deleterec2(fname,location):
    db=getconnection()
    cr=db.cursor()
    sql=f"delete from {fname} where my_booktrip=%s"
    cr.execute(sql,location)
    db.commit()
    db.close()

