from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
import re
import time
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = '0118999881999119725'


# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/results', methods=['POST'])
def ninjas():
	print "hello"
	error=False
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	password = request.form['password']
	confirm_pass=request.form['confirm_pass']
	email=request.form['email']
	birthday=request.form['birthday']


	

	if(len(first_name)==0):
		flash("First Name cannot be empty!")
		return redirect('/')
	elif(not first_name.isalpha()):
		flash("First Name cannot contain numbers")
		return redirect('/')
	if(len(birthday)==0):
		flash("Birthday cannot be empty!")
		return redirect('/')
	else:
		birthday = time.strptime(str(birthday), "%Y-%m-%d")
		date = datetime.date.today()
		date = time.strptime(str(date)	, "%Y-%m-%d")
		if(date < birthday):
			flash("Birthday must be in the past")
			return redirect('/')		
	if(len(last_name)==0):
		flash("Last Name cannot be empty!")
		return redirect('/')
	elif(not last_name.isalpha()):
		flash("Last Name cannot contain numbers")
		return redirect('/')

	if(len(password)==0):
		flash("Password cannot be empty!")
		return redirect('/')
	elif(len(password)<8):
		flash("Password cannot be less than 8 characters!")
		return redirect('/')
	elif(not(any(c.isdigit() for c in password) and any(c.isupper() for c in password))):
		flash("Password must contain upper case letter and number")
		return redirect('/')

	if(len(confirm_pass)==0):
		flash("Confirm your password")
		return redirect('/')
	elif(not password == confirm_pass):
		flash("Passwords dont match")
		return redirect('/')

	if(len(email) < 1):
		flash("Email cannot be empty!")
		return redirect('/')
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")	
		return redirect('/')

	flash("Success")		
	return redirect('/')

app.run(debug=True) # run our server