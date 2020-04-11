#
#
#
import sys
import msvcrt
import socket

#================================
#
#
def client(host='127.0.0.1', port=9999):
    with socket.socket() as sock:
        sock.connect((host,port))
        while True:
            tx = input('>>> ')
            sock.sendall(tx.encode())
            rx = sock.recv(1024)
            print(f'{rx.decode()}')

#================================
#
#
if  __name__ == '__main__':

    client()
    sys.exit()

#
#
#