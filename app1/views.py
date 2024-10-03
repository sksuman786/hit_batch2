from django.shortcuts import render
import mysql.connector as mysql

# Create your views here.

def insertquery():
	qry = 'insert into reg(name,email,pas) values(%s,%s,%s)'
	return qry

def fetchdataqry():
	qry = 'select * from reg where email=%s'
	return qry

def insertdata(n,e,p):
	con = mysql.connect(host='database-2.czcw8cekq1vt.eu-north-1.rds.amazonaws.com',user='admin',password='Amazon123',database='hit2')
	db = con.cursor()

	db.execute(insertquery(),(n,e,p,))
	con.commit()

	db.close()
	con.close()


def fetchcredential(e):
	con = mysql.connect(host='database-2.czcw8cekq1vt.eu-north-1.rds.amazonaws.com',user='admin',password='Amazon123',database='hit2')
	db = con.cursor()

	db.execute(fetchdataqry(),(e,))
	x = db.fetchall()

	db.close()
	con.close()

	return x





def singup(request):

	if request.method == 'POST':
		n = request.POST.get('name')
		e = request.POST.get('email')
		p = request.POST.get('password')

		print(n,e,p)

		if n!=None and e!=None and p!=None:
			insertdata(n,e,p)

	return render(request,'signup.html')


def login(request):
	l = []
	if request.method == 'POST':
		e = request.POST.get('email')
		p = request.POST.get('password')

		print(e,p)

		if e!=None and p!=None:
			d = fetchcredential(e)
			for data in d:
				l.append(data[1])
				l.append(data[3])
			print('list:  ',l)
			if p in l:
				print('login successfull')
				return render(request,'home_page.html',{'name':l[0]})
			else:
				print('Login not successfull')
				return render(request,'login.html',{'msg':'Credential Missmatch'})



	return render(request,'login.html')