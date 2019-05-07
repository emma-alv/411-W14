from flask import request, json
from requests import get
import numpy as np

M = get("http://85.254.220.223:8081/a")
B = get("http://85.254.220.223:8081/n2")

data = M.json()
N2 = B.json()

X = [data['N1'],data['N2'],data['N3']]

matrix = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

result = np.dot(matrix, N2)

R = {'N2': list(result)}

print (R)