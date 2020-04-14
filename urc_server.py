#
#
#
import os
import sys

import zKMServer
import zKMGui
import zKMTray
import zKMUtil

#================================
#
#
if  __name__ == '__main__':
    
    ui = zKMGui.Gui()
    ui.show_ip_addr()

    file = os.path.realpath(__file__)
    tray = zKMTray.Tray(file, sys.argv)
    zKMUtil.hide_console()

    km = zKMServer.KMServer()
    while True:
        km.run_server()
        km.check_client_message()

    sys.exit()

#
#
#