#
#
#
import os
import sys
import msvcrt
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from time import sleep, strftime
from threading import Thread

from zKMAction import *

#================================
#
#
KM_HOST = '192.168.0.9'
KM_PORT = 9999
KM_CLIENT_JOIN = '--join--'
KM_CLIENT_LEAVE = '--leave--'

KM_ENTER = 'enter'
KM_BS = 'bs'
KM_U = 'up'
KM_D = 'down'
KM_L = 'left'
KM_R = 'right'
KM_ADD = 'add'

KM_V_U = 'vup'
KM_V_D = 'vdown'
KM_V_M = 'vmute'

KM_L_U = 'lup'
KM_L_D = 'ldown'
KM_R_U = 'rup'
KM_R_D = 'rdown'

KM_L_CLICK = 'lclick'
KM_R_CLICK = 'rclick'

#================================
#
#
class KMServer:

    sock = None
    conn = None

    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(('',KM_PORT))
        self.sock.listen(0)
    
    def run_server(self):
        if  True: #---- kong ---- for future usage
            print('waiting...')
            self.conn, addr = self.sock.accept()
            print(f'connected to {addr}')
            Thread(target=self.check_connection).start()
            print('rx...')
            return True
        else:
            return False

    @staticmethod
    def send(conn, message):
        try:
            message += '\n'
            conn.send(message.encode())
        except:
            pass
    
    def wait_for_client_message(self):
        try:
            m = self.conn.recv(1024)
            print('rx-0')
            if  m == b'':
                self.conn.close()
                return None
            r = m.decode('utf-8')
            return r
        except:
            self.conn.close()
            self.conn = None
            return None

    def check_connection(self):
        while True:
            sleep(1)
            if  self.is_connected():
                self.send(self.conn, '+')
            else:
                if  self.is_connected():
                    self.conn.close()
                    self.conn = None
                break
    
    def check_client_message(self):
        if  self.is_connected():
            m = self.wait_for_client_message()
            if  m == None:
                return
            if  m == KM_CLIENT_JOIN:
                print('joined')
                while True:
                    sleep(0.0005)
                    try:
                        m = self.conn.recv(1024)
                        print('rx-1')

                        if  m.decode() == KM_CLIENT_LEAVE:
                            print('leaved')
                            break

                        try:
                            i = self.get_position(m.decode())
                            print(f'{i}')
                            for j in i:
                                print('move')
                                move_mouse(j[0]*3,j[1]*2)
                        except:
                            pass

                        if  m.decode() == KM_ENTER:
                            enter()
                        elif m.decode() == KM_BS:
                            bs()
                        elif KM_ADD in m.decode():
                            handle_key(m.decode()[-1])
                        elif m.decode() == KM_U:
                            up()
                        elif m.decode() == KM_D:
                            down()
                        elif m.decode() == KM_L:
                            left()
                        elif m.decode() == KM_R:
                            right()
                        
                        elif m.decode() == KM_V_U:
                            vol_up()
                        elif m.decode() == KM_V_D:
                            vol_down()
                        elif m.decode() == KM_V_M:
                            vol_mute()

                        elif m.decode() == KM_L_U:
                            left_up()
                        elif m.decode() == KM_L_D:
                            left_down()
                        elif m.decode() == KM_L_CLICK:
                            left_click()
                        elif m.decode() == KM_R_U:
                            right_up()
                        elif m.decode() == KM_R_D:
                            right_down()
                        elif m.decode() == KM_R_CLICK:
                            right_click()
                        else:
                            pass
                    except:
                        return

    def is_connected(self):
        if  'closed' in str(self.conn):
            return False
        else:
            return True

    def get_conn(self):
        return self.conn

    def get_position(self, pos):
        print(f'{pos}')
        d = []
        p = pos.split(',')
        n = len(p)
        for i in range(0,n,2):
            try:
                d.append((int(float(p[i])),int(float(p[i+1]))))
            except:
                continue
        return d
    
#================================
#
#
if  __name__ == '__main__':
    
    km = KMServer()

    while True:
        km.run_server()
        km.check_client_message()
        #---- kong ----

    sys.exit()

#
#
#