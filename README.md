# Matrix operation distributed - 411 Telecommunication Software

## Introduction

As we may know, nowadays big data has become an important part of new researches and with the technology innovations, we are able to analyze big amount data at one time. 

So, a good way to do this analysis is to distribute all of the data among different servers. Doing this we can have a faster time response of our computation and we can optimise the resources of the servers.

The purpose of this script is to create a simple connection among a master server (client) which has all the data to be computed and different servers which are going to receive part of the information work whit it and send back the result of their computation.

The aim of this project is to create a distributed system to analyze data.

## Data structure

As we said before, we are only creating a python script to distribute the data among servers. So, for the purpose of this project, we are going to use dictionaries to handle all data.

For this example, we create a dictionary which is going to work as the matrix

| 1  2  3 |

| 4  5  6 |

| 7  8  9 |

In our data computation, we are going to send to each server the main matrix and one column. So, we create our main dictionary with the two matrices and we organize them by columns using the key identifier in the dictionary as the number of column in the matrix.

```markdown
M = {
    'A': {'N1': [1, 4, 7], 'N2': [2, 5, 8], 'N3': [3, 6, 9]},

    'B': {'N1': [1, 4, 7], 'N2': [2, 5, 8], 'N3': [3, 6, 9]}}
```
Continuous with the data structure we created another two dictionaries, one dictionary is going to save all the results from the servers and the second dictionary we can use to specify the IP and PORT for each server to establish a connection.

```
R = {}

DNS = {'N1': {'IP': '127.0.0.1', 'PORT': 8081},
       'N2': {'IP': '127.0.0.1', 'PORT': 8082},
       'N3': {'IP': '127.0.0.1', 'PORT': 8083}, }
```

## Data transfer

To establish communication among client and servers we use sockets. 

So we can create the same function to receive data neither in client and servers.

For each server we should defined its own IP and PORT to listen.

```
import socket

HOST = '127.0.0.1'
PORT = 8080

def send_data(data, HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)


def back_data():
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
```

# Data Client 

As was mentioned before, our client is sending all the data information to the servers, collect it back and organise it again.

So, our client service should be listening and sending data at the same time. To do this, we use threadings to can run two functions at the same time. One function is going to send all the data to the servers and the second function is waiting for their answer.

```
import threading

def call():
    data_1 = pickle.dumps(M['A'])
    for i, j in zip(M['B'],DNS):
        data_2 = pickle.dumps(M['B'][i])
        send_data(data_1, DNS[j]['IP'], DNS[j]['PORT'])
        time.sleep(1)
        send_data(data_2, DNS[j]['IP'], DNS[j]['PORT'])


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
```

# Data server

To compute all the data in our server we can use simple operations.

And at the end return the result to our client server.

```
import pickle
import numpy as np

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

R = {'S1': list(result)}


print(R)
return_data(R)

```

## Data results

Finally we will have all the data back in our Result dictionary.

```
Connected by ('10.0.10.1', 53125)
Received{'S1': [30, 66, 102]}
Connected by ('10.0.10.1', 53128)
Received{'S2': [36, 81, 126]}
Connected by ('10.0.10.1', 53130)
Received{'S3': [42, 96, 150]}
{'S1': [30, 66, 102], 'S2': [36, 81, 126], 'S3': [42, 96, 150]}
```
