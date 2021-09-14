from flask import Flask,request,session,redirect,url_for,render_template
app=Flask(__name__)
app.secret_key='sss'

@app.route('/')
def index():
    if 'username' in session:
        username=session['username']
        return 'Logged in as '+username+'<br>'+"<a href='/logout'>Logout</a>"
    return 'Not Logged in'+" "+'<br>'+"<a href='/login'>Login</a>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)
