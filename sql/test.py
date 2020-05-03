from MySQLdb import *
#connect ('localhost','user_id','password',[dbname])
conobj = connect('localhost','','')
curobj = conobj.cursor()
curobj.execute('create database python;')
curobj.execute('use python;')
curobj.execute('create table student (regno int,name varchar(30),course varchar (10),address varchar(50));')
curobj.execute('insert into student values(1,"raja das","python","bbsr")')
curobj.execute('select * from student;')
record = curobj.fetchall()
for regno,name,course,address in record :
	print regno,name,course,address
curobj.close()
conobj.close()
