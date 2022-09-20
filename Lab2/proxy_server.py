#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            data_from_google = connect_to_host_and_get_data()
            time.sleep(0.5)
            conn.sendall(data_from_google)
            conn.close()


def connect_to_host_and_get_data():
    #QUESTION 2
    #connect to google
    host = 'www.google.com'
    port = 80
    buffer_size = 4096
    payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
        remote_ip = socket.gethostbyname(host)
        proxy_end.connect((remote_ip , port))
        proxy_end.sendall(payload.encode())
        proxy_end.shutdown(socket.SHUT_WR)

        data_from_host = b""
        while True:
            data = proxy_end.recv(buffer_size)
            if not data: break
            data_from_host += data

    return data_from_host


if __name__ == "__main__":
    main()
