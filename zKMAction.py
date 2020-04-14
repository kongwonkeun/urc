#
#
#
import sys
import msvcrt
import win32api
import win32con

#================================
#
#
shift_without = {
    '0':0x30,'1':0x31,'2':0x32,'3':0x33,'4':0x34,'5':0x35,'6':0x36,'7':0x37,'8':0x38,'9':0x39,
    'a':0x41,'b':0x42,'c':0x43,'d':0x44,'e':0x45,'f':0x46,'g':0x47,'h':0x48,'i':0x49,'j':0x4A,
    'k':0x4B,'l':0x4C,'m':0x4D,'n':0x4E,'o':0x4F,'p':0x50,'q':0x51,'r':0x52,'s':0x53,'t':0x54,
    'u':0x55,'v':0x56,'w':0x57,'x':0x58,'y':0x59,'z':0x5A,
    '/':0xBF,',':0xBC,'-':0xBD,'.':0xBE,';':0xBA,'[':0xDB,'\\':0xDC,']':0xDD,
    "'":0xDE,' ':0x20,'=':0xBB,
}

shift_with = {
    ')':0x30,'!':0x31,'@':0x32,'#':0x33,'$':0x34,'%':0x35,'^':0x36,'&':0x37,'*':0x38,'(':0x39,
    'A':0x41,'B':0x42,'C':0x43,'D':0x44,'E':0x45,'F':0x46,'G':0x47,'H':0x48,'I':0x49,'J':0x4A,
    'K':0x4B,'L':0x4C,'M':0x4D,'N':0x4E,'O':0x4F,'P':0x50,'Q':0x51,'R':0x52,'S':0x53,'T':0x54,
    'U':0x55,'V':0x56,'W':0x57,'X':0x58,'Y':0x59,'Z':0x5A,
    '?':0xBF,'<':0xBC,'_':0xBD,'>':0xBE,':':0xBA,'{':0xDB,'|':0xDC,'}':0xDD,
    '"':0xDE,' ':0x20,'+':0xBB,
}

#================================
#
#
def handle_key(key):
    if  key in shift_without:
        press(shift_without[key])
    if  key in shift_with:
        press_with_shift(shift_with[key])

def press(keycode):
    win32api.keybd_event(keycode,0,0,0)

def press_with_shift(keycode):
    win32api.keybd_event(0xA0,0,1,0)
    press(keycode)
    win32api.keybd_event(0xA0,0,win32con.KEYEVENTF_EXTENDEDKEY|win32con.KEYEVENTF_KEYUP,0)

def move_mouse(x,y):
    p = win32api.GetCursorPos()
    win32api.SetCursorPos((p[0]+x,p[1]+y))

#================================
#
#
def vol_up():
    win32api.keybd_event(0xAF,0,0,0)

def vol_down():
    win32api.keybd_event(0xAE,0,0,0)

def vol_mute():
    win32api.keybd_event(0xAD,0,0,0)

#================================
#
#
def up():
    win32api.keybd_event(0x26,0,0,0)

def down():
    win32api.keybd_event(0x28,0,0,0)

def left():
    win32api.keybd_event(0x25,0,0,0)

def right():
    win32api.keybd_event(0x27,0,0,0)

def bs():
    win32api.keybd_event(0x08,0,0,0)

def enter():
    win32api.keybd_event(0x0D,0,0,0)

#================================
#
#
def left_up():
    p = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP  ,p[0],p[1],0,0)

def left_down():
    p = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,p[0],p[1],0,0)

def left_click():
    p = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,p[0],p[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,  p[0],p[1],0,0)

def right_up():
    p = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP  ,p[0],p[1],0,0)

def right_down():
    p = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,p[0],p[1],0,0)

def right_click():
    p = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,p[0],p[1],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,  p[0],p[1],0,0)

#================================
#
#
if  __name__ == '__main__':

    while True:
        if  msvcrt.kbhit():
            c = msvcrt.getch()
            #move_mouse(10,10)
            #vol_up()
            #press(0x37)
            #print(c)
            #handle_key('c')
            if  c == b'q':
                break

    sys.exit()

#
#
#