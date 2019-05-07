
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from requests import get


app = Flask(__name__)
api = Api(app)

M = {
    'A': {'N1': [1, 4, 7],'N2': [2, 5, 8], 'N3': [3, 6, 9]},

    'B': {'N1': [1, 4, 7],'N2': [2, 5, 8], 'N3': [3, 6, 9]}}


class Matrix(Resource):
    def get(self):
        return M


class A(Resource):
    def get(self):
        return M['A']


class N1(Resource):
    def get(self):
        return M['B']['N1']


class N2(Resource):
    def get(self):
        return M['B']['N2']


class N3(Resource):
    def get(self):
        return M['B']['N3']


class Server1(Resource):
    def get(self):
        S1 = get("http://85.254.220.223:8082")

        return S1



api.add_resource(Matrix,'/')
api.add_resource(A,'/a')
api.add_resource(N1,'/n1')
api.add_resource(N2,'/n2')
api.add_resource(N3,'/n3')
api.add_resource(Server1,'/s1')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8081')
