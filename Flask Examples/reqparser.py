from flask import Flask
from flask_restx import Api, Resource, fields
from flask_restx import reqparse

app=Flask(__name__)
api=Api(app)

ns = api.namespace('Details', description='Request Parser')
parser = reqparse.RequestParser()
parser.add_argument('name',required=True, help="Name cannot be blank!")
parser.add_argument('email', type=str, help='Enter email')
parser.add_argument('PhoneNo', type=str,action='append')



@ns.route('/')
class ReqParser(Resource):
    
    @ns.expect(parser)
    def get(self):
        
        args = parser.parse_args()
        return str(args["name"])+" "+str(args["email"])+" "+str(args["PhoneNo"])
        









if __name__ == '__main__':
    app.run(debug=True)
