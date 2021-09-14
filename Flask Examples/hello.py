from flask import Flask,render_template,redirect,request

app=Flask(__name__)

@app.route('/')
def hello():
    #return "Hello World"
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

#@app.route('/login')
#def login():
#    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)
