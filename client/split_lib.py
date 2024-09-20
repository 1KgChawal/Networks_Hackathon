# Library file for both the functions
import requests
import socket
import os

HOST = '127.0.0.1'  # Server IP
PORT = 65432        # Server port

url = 'http://localhost:5000/'
url_upload = url + 'upload'
url_download = url + 'download/'

count = 0

def split_store(file_name) :
    # Split store code
    # debug = open('./client/debug.txt','a')
    f = open('./client/mem/' + file_name, 'rb')
    flag = True
    i = 0 
    while True:
        data = f.read(1024)
        file_to_send = open('./client/mem/' + file_name + str(i), 'wb')
        file_to_send.write(data)
        file_to_send.close()
        # debug.write('>>>')
        if flag :
            #HTTP
            # debug.write('>>>HTTP')
            requests.post('http://localhost:5000/upload', files = {'file': open('./client/mem/' + file_name + str(i), 'rb')})
            # debug.write('HTTP<<<<')
        else :
            #TCP
            file_path = './client/mem/' + file_name + str(i)
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
            file_name_ = file_name + str(i)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((HOST, PORT))
                client_socket.sendall(b'upload'.ljust(1024))  # Send operation type
            
                # Send file name and file size
                client_socket.sendall(file_name_.encode().ljust(1024))
                client_socket.sendall(str(file_size).encode().ljust(1024))

                # Send the entire file in one go
                with open(file_path, 'rb') as file:
                    client_socket.sendall(file.read())  # Read and send the file
                # debug.write(f"File '{file_name_}' uploaded.")
        if not data:
            break
        flag = not flag
        i+=1
        # debug.write(f"File '{file_name}' split into {i} parts.")
    global count
    count = i
    pass

def split_fetch(file_name) :
    # Split fetch code
    i = 0
    flag = True
    local_path = './client/mem/'
    while True :

        if i == count :
            break

        if flag :
            #HTTP
            response = requests.get(url_download+file_name+str(i), stream=True)
            if response.status_code == 200:
                with open(local_path+file_name, 'ab') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
        else :
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((HOST, PORT))
                client_socket.sendall(b'download'.ljust(1024))

                client_socket.sendall((file_name+str(i)).encode().ljust(1024))

                file_size = 1024

                file_data = client_socket.recv(file_size)

                file_path = local_path + file_name
                with open(file_path, 'ab') as file:
                    file.write(file_data)

        i += 1
        flag = not flag
    pass