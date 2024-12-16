from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')
    
@app.route('/login', methods=['GET','POST'])
def login():
    session.clear()

    if request.method =='POST':
        username = request.form['username'].strip().lower()
        pwd = request.form['password'].strip()

        cur = mysql.connection.cursor()
        cur.execute("SELECT username, password FROM tbl_users WHERE username = %s", (username,))       
        user = cur.fetchone()
        cur.close()
       
        if user:
            stored_username = user[0]
            stored_password_hash = user[1]
            print(f"Stored username from DB: {stored_username}")
            print(f"Stored password hash from DB: {stored_password_hash}")
            password_match = check_password_hash(stored_password_hash, pwd)
            print(f"Password match result: {password_match}")
            
            if password_match:
                print("Login successful!")
                session['username'] = stored_username
                return redirect(url_for('home'))
        
            else:
                print("Password does not match!")
                return render_template('login.html', error='Invalid username or password')
        else:
            print("No user found with that username!")
            return render_template('login.html', error='Invalid username or password')
        
    return render_template('login.html')

@app.route('/test-hash')
def test_hash():
    original_password = '123456789'
    hashed_password = generate_password_hash(original_password)
    print("Original password:", original_password)
    print("Generated hash:", hashed_password)

    check_result = check_password_hash(hashed_password, '123456789')
    print("Password match result:", check_result)
    return "Check your terminal for hash and result"

@app.route('/generate-hash')
def generate_hash():
    password = '123456789'  # The new password you want
    hashed_password = generate_password_hash(password)
    return f"Hashed password for '{password}': {hashed_password}"


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip().lower()
        pwd = request.form['password'].strip() 
        pwd_hash = generate_password_hash(pwd)

        print("Generated hash:", pwd_hash)
        print("Username (in lowercase):", username)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_users (username, password) VALUES (%s, %s)", (username, pwd_hash))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__== '__main__':
    app.run(debug=True)

   

   
