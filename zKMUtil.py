#
#
#
import ctypes
import getpass
import msvcrt
import os
import shutil
import signal
import subprocess
import sys
import win32com.client
import socket

#================================
#
#
USER_NAME = getpass.getuser() # login user name
PROCESS_PER_EXEC = 2 # an app and its loader
WIN_SHOW = 1
WIN_HIDE = 0

G_running = False
G_quit = False

#================================
#
#
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def check_q():
    if  msvcrt.kbhit():
        c = msvcrt.getch()
        if  c == b'q':
            return True
    return False

def wait_user_input():
    global G_quit
    print('--- type q to quit ---')
    while True:
        if  check_q() == True or G_quit == True:
            break

def is_running(file):
    global G_running
    base, ext = os.path.splitext(os.path.basename(file))
    call = 'TASKLIST', '/FI', f'imagename eq {base}.exe'
    output = subprocess.check_output(call)
    output = output.decode('euc-kr')
    print(output)
    names = output.strip().split('\r\n')
    names = names[2:] # remove table form
    n = names[-1]
    if  n.lower().startswith(base.lower()):
        G_running = True
        return len(names)
    else:
        return 0

def kill_all(file):
    base, ext = os.path.splitext(os.path.basename(file))
    win_mgmt = win32com.client.GetObject('winmgmts:')
    all_proc = win_mgmt.InstancesOf('Win32_Process')
    for p in all_proc:
        if  p.Properties_('Name').Value == f'{base}.exe':
            pid = p.Properties_('ProcessID').Value
            os.kill(pid, 9)

def show_console():
    k32 = ctypes.WinDLL('kernel32')
    u32 = ctypes.WinDLL('user32')
    win = k32.GetConsoleWindow()
    u32.ShowWindow(win, WIN_SHOW)

def hide_console():
    k32 = ctypes.WinDLL('kernel32')
    u32 = ctypes.WinDLL('user32')
    win = k32.GetConsoleWindow()
    u32.ShowWindow(win, WIN_HIDE)

def raise_ctrl_c():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)

#================================
#
#
if  __name__ == '__main__':

    file = os.path.realpath(__file__)
    print(file)

    file = 'python.exe'
    print(is_running(file))
    kill_all(file)
    #wait_user_input()

    wait_user_input()
    sys.exit()

#
#
#