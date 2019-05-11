'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python T431.py
    or if it doesn't work use this one:
        python3 T431.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from mpmath import *
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry, Radiobutton, Button, Style

mp.dps = 50000; mp.pretty = True

class T431(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("T431")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global v
        v = IntVar()
        v.set(1)
        
        global exp
        exp = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)
		
        
        rb1 = Radiobutton(frame1, text = "4*3^n-1", variable = v, value = 1,style='My.TRadiobutton')
        rb1.pack( anchor = W )
		
        rb2 = Radiobutton(frame1, text = "4*3^n+1", variable = v, value = 2,style='My.TRadiobutton')
        rb2.pack( anchor = W )
		
        
       
		
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Enter the exponent :", width=18,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2,textvariable=exp,style='My.TEntry')
        entry2.pack(fill=X, padx=5, expand=True)

        
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        result = Label(frame3, textvariable=res, width=42,background='orange')
        result.pack(side=LEFT, padx=60, pady=5)

		
        frame4 = Frame(self,style='My.TFrame')
        frame4.pack(fill=X)

        btntest = Button(frame4, text="Test", width=10, command=self.test,style='My.TButton')
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame4, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame4, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        
        elif msg == 'erre':
            tkinter.messagebox.showerror('Error!', 'Exponent must be greater than two')
			
    
        
    

    def test(self):
        try:
            
            
            n = int(exp.get())
			
           
            if n<3:
                self.errorMsg('erre')
            else:
				
               
               
            
                if v.get()==1:
                    N=4*3**n-1
                    s=7761798
                    ctr=1
                    while ctr<=n-2:
                        s=(s**3-3*s)%N
                        ctr=ctr+1
                    if int(s)==0:
                        value="4*3^"+str(n)+"-1 is prime"
                        res.set(self.makeAsItIs(value))
                    else:
                        value="4*3^"+str(n)+"-1 is composite"
                        res.set(self.makeAsItIs(value))
					
                else:
                    N=4*3**n+1
                    s=140452
                    ctr=1
                    while ctr<=n-2:
                        s=(s**3-3*s)%N
                        ctr=ctr+1
                    if int(s)==0:
                        value="4*3^"+str(n)+"+1 is prime"
                        res.set(self.makeAsItIs(value))
                    else:
                        value="4*3^"+str(n)+"+1 is composite"
                        res.set(self.makeAsItIs(value))
          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            exp.set('')
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    s.configure('My.TRadiobutton', background='orange')
    s.map('My.TRadiobutton', background=[('active', '#FFC133')])
    root.geometry("300x125")
    t431 = T431(root)
    root.mainloop()

if __name__ == '__main__':
    main()
