import socket
import pickle
import threading
import time

HOST = '127.0.0.1'
PORT = 8080

M = {
    'A': {'N1': [1, 4, 7],'N2': [2, 5, 8], 'N3': [3, 6, 9]},

    'B': {'N1': [1, 4, 7],'N2': [2, 5, 8], 'N3': [3, 6, 9]}}

R = {}


def send_data(data, HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)


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

    return recvd_data


def call():
    PORT = 8080
    data_1 = pickle.dumps(M['A'])
    for i in M['B']:
        data_2 = pickle.dumps(M['B'][i])
        PORT += 1
        send_data(data_1, '127.0.0.1', PORT)
        time.sleep(1)
        send_data(data_2, '127.0.0.1', PORT)


def listen():
    counter = 0
    while True:
        if counter < 3:
            R.update(back_data())
            counter += 1
        else:
            break
    print(R)


def main():

        thread_1 = threading.Thread(target=listen)
        time.sleep(1)
        thread_2 = threading.Thread(target=call)
        thread_1.start()
        thread_2.start()


if __name__ == '__main__':main()