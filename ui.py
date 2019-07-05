
from tkinter import messagebox
import sys
import MySQLdb as db 
import mysql.connector
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    ui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    ui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    try:
            
                
                db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="test")        # name of the data base
    except Exception:
             messagebox.showerror("Oops!", "This is embarrassing. We are not able to connect to the DB")
    cur = db.cursor()
    
    def getUser(self):  
        try:
            messagebox.showinfo("Please Wait!", "All the data is being fetched....")
            cur = db.cursor()
            cur.execute("SELECT * FROM user_details")
            result1 = cur.fetchall()
            for y in result1:
                Listbox1.insert(print("HEllo"))
                
                       
         
        except Exception:("Sorry", "The program is not responding")
    # det getUserByID(self):
    #     try: 
    #         messagebox.showinfo("Request Successful!", "The selected query is being processed.")
    #         cur = db.cursor()
    #         cur.execute("SELECT * FROM User_details WHERE User_id = ?", User_id())
    #         result = cur.fetchall()
    #         for x in result:
    #             self.Listbox1.insert(result)
        
  
    db.close()            
    

        
        
    def __init__(self, top=None):
     
                
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+433+86")
        top.title("Project App")
        top.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.25, rely=0.178, relheight=0.3
                , relwidth=0.567)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(width=340)

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.147, rely=0.222, height=27, width=69
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {Georgia} -size 14")
        self.Label1.configure(text='''User ID''')

        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(relx=0.618, rely=0.593, height=31, width=74
                , bordermode='ignore')
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Submit''')

        self.Button2 = tk.Button(self.Labelframe1)
        self.Button2.place(relx=0.118, rely=0.593, height=31, width=84
                , bordermode='ignore')
        self.Button2.configure(activebackground="#f9f9f9")
        self.Button2.configure(command = self.getUser,text='''Show All''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.2, rely=0.044, height=31, width=359)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Twitter Swifter''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.3, rely=0.933, height=21, width=229)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''---APP---''')

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.117, rely=0.578, relheight=0.347
                , relwidth=0.807)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(width=484)

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.467, rely=0.244,height=23, relwidth=0.277)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

if __name__ == '__main__':
    vp_start_gui()





