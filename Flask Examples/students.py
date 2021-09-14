from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Student API',
    description='Student Details',
)

ns = api.namespace('students', description='CRUD operations')

student = api.model('Student', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='Name'),
    'rollNo': fields.Integer(required=True, description='RollNo'),
    'email': fields.String(required=True, description='Email'),
    'phoneNo': fields.Integer(required=True, description='PhoneNo')
})



class Students(object):
    def __init__(self):
        self.counter = 0
        self.students = []

    def get(self, id):
        for stu in self.students:
            if stu['id'] == id:
                return stu
        api.abort(404, "Student {} doesn't exist".format(id))

    def create(self, data):
        stu = data
        stu['id'] = self.counter = self.counter + 1
        self.students.append(stu)
        return stu

    def update(self, id, data):
        stu = self.get(id)
        stu.update(data)
        return stu

    def delete(self, id):
        stu = self.get(id)
        self.students.remove(stu)


s = Students()
s.create({'name': 'Aa','rollNo':1,'email':'Aa@gmail.com','phoneNo':981654326})
s.create({'name': 'Bb','rollNo':2,'email':'Bb@gmail.com','phoneNo':881654346})


@ns.route('/')
class StudentList(Resource):
    @ns.doc('list_students')
    @ns.marshal_list_with(student)
    def get(self):
        '''List all students'''
        return s.students

    @ns.doc('Add_student')
    @ns.expect(student)
    @ns.marshal_with(student, code=201)
    def post(self):
        
        return s.create(api.payload), 201

@ns.route('/<int:id>')
@ns.response(404, 'Student not found')
class Student(Resource):
    @ns.doc('get_student')
    @ns.marshal_with(student)
    def get(self, id):
        
        return s.get(id)

    @ns.doc('delete student')
    @ns.response(204, 'Student Removed')
    def delete(self, id):
        
        s.delete(id)
        return '', 204

    @ns.expect(student)
    @ns.marshal_with(student)
    def put(self, id):
        
        return s.update(id, api.payload)



if __name__ == '__main__':
    app.run(debug=True)
