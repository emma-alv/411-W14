import socket
import pickle
import time

HOST = '127.0.0.1'
PORT = 8080

M = {
    'A': {'N1': [1, 4, 7],'N2': [2, 5, 8], 'N3': [3, 6, 9]},

    'B': {'N1': [1, 4, 7],'N2': [2, 5, 8], 'N3': [3, 6, 9]}}

data_1 = pickle.dumps(M['A'])
data_2 = pickle.dumps(M['B']['N1'])

R = None

def send_data(data, HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)
    return

def back_data():
    PORT = 8080
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
                print('Received' + str(recvd_data))

    return


for i in M['B']:
    data_2 = pickle.dumps(M['B'][i])
    PORT += 1
    send_data(data_1, '127.0.0.1', PORT)
    time.sleep(1)
    send_data(data_2, '127.0.0.1', PORT)


counter = 0
while True:
    if counter < 3:
        back_data()
        counter += 1
    else:
        break