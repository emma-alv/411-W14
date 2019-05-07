from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import request, json
from requests import get
import numpy as np

app = Flask(__name__)
api = Api(app)


class Server1(Resource):
    def get(self):
        M = get("http://85.254.220.223:8081/a")
        B = get("http://85.254.220.223:8081/n1")

        data = M.json()
        N1 = B.json()

        X = [data['N1'],data['N2'],data['N3']]

        matrix = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

        result = np.dot(matrix, N1)

        R = {'N1': list(result)}

        return R


api.add_resource(Server1,'/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8082')

