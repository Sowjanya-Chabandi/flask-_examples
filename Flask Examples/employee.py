from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Employee(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    email=db.Column(db.String(20))
    phoneNo=db.Column(db.String(20))

    def __repr__(self):
        return f"Employee('{self.name}','{self.email}','{self.phoneNo}')"

    

@app.route('/',methods=['GET','POST'])
def index():
    data=Employee.query.all()
    
    return render_template("insert.html",employees=data)

@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phoneNo=request.form['phoneNo']
        data=Employee(name=name,email=email,phoneNo=phoneNo)
        db.session.add(data)
        db.session.commit()
        #return "Employee Inserted Successfully"
        return redirect(url_for('index'))
    
@app.route('/delete/<id>/',methods=['GET','POST'])
def delete(id):
    data=Employee.query.get(id)
    db.session.delete(data)
    db.session.commit()
        
    return redirect(url_for('index'))

        

if __name__=='__main__':
    app.run(debug=True)
