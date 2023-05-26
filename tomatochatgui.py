# 
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import socket
import random
from threading import Thread
from datetime import datetime

_script = sys.argv[0]
_location = os.path.dirname(_script)

import tomatochatgui_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+677+442")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("tomatoChat GUI")
        top.configure(background="#d9d9d9")

        self.top = top
        self.msg = tk.StringVar()

        self.msgbox = tk.Listbox(self.top)
        self.msgbox.place(x=0, y=0, height=422, width=604)
        self.msgbox.configure(background="white")
        self.msgbox.configure(cursor="fleur")
        self.msgbox.configure(disabledforeground="#a3a3a3")
        self.msgbox.configure(font="TkFixedFont")
        self.msgbox.configure(foreground="#000000")
        self.msgentry = tk.Entry(self.top)
        self.msgentry.place(x=0, y=420, height=30, width=514)
        self.msgentry.configure(background="white")
        self.msgentry.configure(disabledforeground="#a3a3a3")
        self.msgentry.configure(font="TkFixedFont")
        self.msgentry.configure(foreground="#000000")
        self.msgentry.configure(insertbackground="black")
        self.msgentry.configure(textvariable=self.msg)
        _style_code()
        self.sendmsg = ttk.Button(self.top)
        self.sendmsg.place(x=530, y=420, height=25, width=66)
        self.sendmsg.configure(command=tomatochatgui_support.sendmsg)
        self.sendmsg.configure(takefocus="")
        self.sendmsg.configure(text='''Send''')
        self.sendmsg.configure(compound='left')

class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("200x128+641+167")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("tomatoChat GUI Connection Window")
        top.configure(background="#d9d9d9")

        self.top = top
        self.ip_input = tk.StringVar()
        self.port_input = tk.StringVar()
        self.username_input = tk.StringVar()

        _style_code()
        self.ipentrylabel = ttk.Label(self.top)
        self.ipentrylabel.place(x=0, y=10, height=25, width=92)
        self.ipentrylabel.configure(background="#d9d9d9")
        self.ipentrylabel.configure(foreground="#000000")
        self.ipentrylabel.configure(font="TkDefaultFont")
        self.ipentrylabel.configure(relief="flat")
        self.ipentrylabel.configure(anchor='w')
        self.ipentrylabel.configure(justify='left')
        self.ipentrylabel.configure(text='''IP Address:''')
        self.ipentrylabel.configure(compound='left')
        self.portentrylabel = ttk.Label(self.top)
        self.portentrylabel.place(x=0, y=30, height=25, width=87)
        self.portentrylabel.configure(background="#d9d9d9")
        self.portentrylabel.configure(foreground="#000000")
        self.portentrylabel.configure(font="TkDefaultFont")
        self.portentrylabel.configure(relief="flat")
        self.portentrylabel.configure(anchor='w')
        self.portentrylabel.configure(justify='left')
        self.portentrylabel.configure(text='''Port:''')
        self.portentrylabel.configure(compound='left')
        self.ipentry = ttk.Entry(self.top)
        self.ipentry.place(x=90, y=10, height=21, width=86)
        self.ipentry.configure(textvariable=self.ip_input)
        self.ipentry.configure(takefocus="")
        self.ipentry.configure(cursor="ibeam")
        self.usernameenterylabel = ttk.Label(self.top)
        self.usernameenterylabel.place(x=0, y=50, height=26, width=86)
        self.usernameenterylabel.configure(background="#d9d9d9")
        self.usernameenterylabel.configure(foreground="#000000")
        self.usernameenterylabel.configure(font="TkDefaultFont")
        self.usernameenterylabel.configure(relief="flat")
        self.usernameenterylabel.configure(anchor='w')
        self.usernameenterylabel.configure(justify='left')
        self.usernameenterylabel.configure(text='''Username:''')
        self.usernameenterylabel.configure(compound='left')
        self.portentry = ttk.Entry(self.top)
        self.portentry.place(x=90, y=30, height=21, width=86)
        self.portentry.configure(textvariable=self.port_input)
        self.portentry.configure(takefocus="")
        self.portentry.configure(cursor="ibeam")
        self.connect = ttk.Button(self.top)
        self.connect.place(x=60, y=80, height=25, width=76)
        self.connect.configure(command=tomatochatgui_support.connect_to_server)
        self.connect.configure(takefocus="")
        self.connect.configure(text='''Connect''')
        self.connect.configure(compound='left')
        self.usernameentry = ttk.Entry(self.top)
        self.usernameentry.place(x=90, y=50, height=21, width=86)
        self.usernameentry.configure(textvariable=self.username_input)
        self.usernameentry.configure(takefocus="")
        self.usernameentry.configure(cursor="ibeam")

def start_up():
    tomatochatgui_support.main()

if __name__ == '__main__':
    tomatochatgui_support.main()




