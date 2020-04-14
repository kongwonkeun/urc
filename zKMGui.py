#
#
#
import sys
import socket

from tkinter import * # pylint: disable=unused-wildcard-import
from tkinter import ttk
from tkinter.font import * # pylint: disable=unused-wildcard-import

import zKMUtil

#===============================
#
#
WIN_W = 400
WIN_H = 200

#===============================
#
#
class Gui:

    def __init__(self):

        self.callback = None

        self.win = Tk()
        self.win.title('win')
        self.w = self.win.winfo_screenwidth()
        self.h = self.win.winfo_screenheight()
        self.x = int(self.w/2 - WIN_W/2)
        self.y = int(self.h/2 - WIN_H/2)
        self.win.geometry(f'+{self.x}+{self.y}')
        self.win.withdraw()

        self.top = Toplevel()
        self.top.title('top')
        self.top.geometry(f'{WIN_W}x{WIN_H}+{self.x}+{self.y}')

        self.font20 = Font(family='맑은 고딕', size=20, weight='bold', slant='italic')
        self.font18 = Font(family='맑은 고딕', size=18, weight='bold', slant='italic')
        self.font16 = Font(family='맑은 고딕', size=16, weight='bold', slant='italic')
        self.font14 = Font(family='맑은 고딕', size=14, weight='bold', slant='italic')

        self.name = ''
        self.ip = ''

    #===========================
    #
    #
    def show_ip_addr(self):
        try:
            self.name = socket.gethostname()
            print(self.name)
            self.ip = zKMUtil.get_ip_address()
            print(self.ip)
        except:
            self.name = 'there is no host name and'
            self.ip = 'ip address'
        Label(self.top, text=self.name, fg="black", font=self.font20).pack(padx=2, pady=2)
        Label(self.top, text=self.ip, fg="green", font=self.font20).pack(padx=2, pady=2)
        Button(self.top, text='OK', width=10, command=self.ok_name).pack(padx=2, pady=2)
        self.top.mainloop()

    def ok_name(self):
        self.top.destroy()
        self.win.destroy()

#===============================
#
#
if  __name__ == '__main__':

    gui = Gui()
    gui.show_ip_addr()
    sys.exit()

#
#
#