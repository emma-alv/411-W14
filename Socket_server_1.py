import socket
import pickle
import numpy as np
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8081        # Port to listen on (non-privileged ports are > 1023)
A = None
B = None

def get_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                recvd_data = pickle.loads(data)
                #print('Received' + str(recvd_data))

    return recvd_data

def return_data(data):
    HOST = '127.0.0.1'
    PORT = 8080

    data_b = pickle.dumps(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data_b)

    return

while True:
    if not A:
        A = get_data()
        print('I have A as: ' + str(A))
        print(type(A))
    elif not B:
        B = get_data()
        print('I have B as: ' + str(B))
        print(type(B))
        break

X = [A['N1'],A['N2'],A['N3']]

matrix = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

result = np.dot(matrix, B)

R = {'N1': list(result)}

time.sleep(5)

print(R)
return_data(R)


