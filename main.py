from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "mysecretkey"
users = {'username':'password'}

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username'] 
        if request.form['username'] in users and request.form['password'] == users[request.form['username']]:
            return redirect('/home')
        else:
             return 'Invalid username/password combination'
        return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
     app.run(debug=True)
