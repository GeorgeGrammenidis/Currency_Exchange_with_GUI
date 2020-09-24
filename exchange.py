from tkinter import *
expression=""
euro1=False
dollar1=False
euro2=False
dollar2=False
pound1=False
pound2=False
yen1=False
yen2=False

def Action (x):
       global expression
       x=str(x)
       expression= expression + x
       number.set(expression)

def Erase():
       global expression
       global euro1
       global euro2
       global dollar1
       global dollar2
       global pound1
       global pound2
       global yen2
       global yen1
       yen1=False
       yen2=False
       euro1=False
       euro2=False
       dollar1=False
       dollar2=False
       pound1=False
       pound2=False
       expression=""
       number.set("Left Column: Your current currency | Right Column: What you want to convert it to")

def fromyen():
       global euro1
       global dollar1
       global pound1
       global yen1
       yen1=True
       euro1=False
       dollar1=False
       pound1=False
       
def toyen():
       global euro2
       global dollar2
       global pound2
       global yen2
       yen2=True
       euro2=False
       dollar2=False 
       pound2=False
       
       
def frompound():
       global euro1
       global dollar1
       global pound1
       global yen1
       yen1=False
       euro1=False
       dollar1=False
       pound1=True
       
def topound():
       global euro2
       global dollar2
       global pound2
       global yen2
       yen2=False
       euro2=False
       dollar2=False 
       pound2=True
       
def fromeuro():
       global euro1
       global dollar1
       global yen1
       global pound1
       pound1=False
       yen1=False
       euro1=True
       dollar1=False

def fromdollar():
       global euro1
       global dollar1
       global yen1
       global pound1
       pound1=False
       yen1=False
       euro1=False
       dollar1=True

def toeuro():
       global euro2
       global dollar2
       global pound2
       global yen2
       pound2=False
       yen2=False
       euro2=True
       dollar2=False

def todollar():
       global euro2
       global dollar2
       global yen2
       global pound2
       yen2=False
       pound2=False
       euro2=False
       dollar2=True
       
def Exchange():
       global expression
       global euro1
       global dollar1
       global euro2
       global dollar2
       global yen1
       global yen2
       global pound1
       global pound2
       if (euro1==True) and (dollar2==True):
              try:
                     money=int(expression)
                     money=1.1*money
                     money=str(money)
                     money= money + "USDs"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 01")
       elif (dollar1==True) and (euro2==True):
              try:
                     money=int(expression)
                     money=0.9*money
                     money=str(money)
                     money= money + " euros"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 02")
       elif (dollar1==True) and (pound2==True):
              try:
                     money=int(expression)
                     money=0.76*money
                     money=str(money)
                     money= money + " pounds"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 03")
       elif (pound1==True) and (dollar2==True):
              try:
                     money=int(expression)
                     money=1.31*money
                     money=str(money)
                     money= money + " USDs"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 04")
       elif (euro1==True) and (pound2==True):
              try:
                     money=int(expression)
                     money=0.84*money
                     money=str(money)
                     money= money + " pounds"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 05")
       elif (pound1==True) and (euro2==True):
              try:
                     money=int(expression)
                     money=1.19*money
                     money=str(money)
                     money= money + " euros"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 06")
       elif (yen1==True) and (dollar2==True):
              try:
                     money=int(expression)
                     money=0.092*money
                     money=str(money)
                     money= money + " USDs"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 07")
       elif (yen1==True) and (euro2==True):
              try:
                     money=int(expression)
                     money=0.0083*money
                     money=str(money)
                     money= money + " euros"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 08")
       elif (yen1==True) and (pound2==True):
              try:
                     money=int(expression)
                     money=0.007*money
                     money=str(money)
                     money= money + " pounds"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 09")
       elif (euro1==True) and (yen2==True):
              try:
                     money=int(expression)
                     money=120.56*money
                     money=str(money)
                     money= money + " yen"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 10")
       elif (dollar1==True) and (yen2==True):
              try:
                     money=int(expression)
                     money=109.28*money
                     money=str(money)
                     money= money + " yen"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 11")
       elif (pound1==True) and (yen2==True):
              try:
                     money=int(expression)
                     money=142.8*money
                     money=str(money)
                     money= money + " yen"
                     expression=""
                     number.set(money)
              except:
                     expression=""
                     number.set("Error 12")
       else:
              number.set("Select two different currencies")
              
              

       
if __name__=="__main__":
       gui=Tk()
       gui.configure(background="green")
       gui.geometry("2000x1500")
       gui.title("Exchange")
       number=StringVar()
       number.set("Type your amount. Left: Your currency Right: What you want to convert it to")
       field=Entry(gui, textvariable=number)
       field.grid(columnspan=10,ipadx=1000)
       
       
       button1=Button(gui, text="1", fg="yellow", bg="blue", command=lambda: Action(1), height=5, width=10)
       button1.grid(column=0, row=1)
       
       button2=Button(gui, text="2", fg="yellow", bg="blue", command=lambda: Action(2), height=5, width=10)
       button2.grid(column=1, row=1)
       
       button3=Button(gui, text="3", fg="yellow", bg="blue", command=lambda: Action(3), height=5, width=10)
       button3.grid(column=2, row=1)
       
       button4=Button(gui, text="4", fg="yellow", bg="blue", command=lambda: Action(4), height=5, width=10)
       button4.grid(column=0, row=2)

       button5=Button(gui, text="5", fg="yellow", bg="blue", command=lambda: Action(5), height=5, width=10)
       button5.grid(column=1, row=2)

       button6=Button(gui, text="6", fg="yellow", bg="blue", command=lambda: Action(3), height=5, width=10)
       button6.grid(column=2, row=2)

       button7=Button(gui, text="7", fg="yellow", bg="blue", command=lambda: Action(7), height=5, width=10)
       button7.grid(column=0, row=3)

       button8=Button(gui, text="8", fg="yellow", bg="blue", command=lambda: Action(8), height=5, width=10)
       button8.grid(column=1, row=3)

       button9=Button(gui, text="9", fg="yellow", bg="blue", command=lambda: Action(9), height=5, width=10)
       button9.grid(column=2, row=3)

       button0=Button(gui, text="0", fg="yellow", bg="blue", command=lambda: Action(0), height=5, width=10)
       button0.grid(column=0, row=4)

       clear=Button(gui, text="Reset", fg="yellow", bg="blue", command=lambda: Erase(), height=5, width=10)
       clear.grid(column=1, row=4)

       dot=Button(gui, text=".", fg="yellow", bg="blue", command=lambda: Action("."), height=5, width=10)
       dot.grid(column=2, row=4)

       Dollar1=Button(gui, text="Dollar", fg="yellow", bg="blue", command=lambda: fromdollar() , height=5, width=10)
       Dollar1.grid(column=3, row=1)

       Dollar2=Button(gui, text="Dollar", fg="yellow", bg="blue", command=lambda: todollar() , height=5, width=10)
       Dollar2.grid(column=4, row=1)

       Euro1=Button(gui, text="Euro", fg="yellow", bg="blue", command=lambda: fromeuro() , height=5, width=10)
       Euro1.grid(column=3, row=2)

       Euro2=Button(gui, text="Euro", fg="yellow", bg="blue", command=lambda: toeuro() , height=5, width=10)
       Euro2.grid(column=4, row=2)

       Pound1=Button(gui, text="Pound", fg="yellow", bg="blue", command=lambda: frompound() , height=5, width=10)
       Pound1.grid(column=3, row=3)

       Pound2=Button(gui, text="Pound", fg="yellow", bg="blue", command=lambda: topound() , height=5, width=10)
       Pound2.grid(column=4, row=3)

       Yen1=Button(gui, text="Yen", fg="yellow", bg="blue", command=lambda: fromyen() , height=5, width=10)
       Yen1.grid(column=3, row=4)

       Yen2=Button(gui, text="Yen", fg="yellow", bg="blue", command=lambda: toyen() , height=5, width=10)
       Yen2.grid(column=4, row=4)
       
       calculate=Button(gui, text="Calculate", fg="yellow", bg="blue", command=lambda: Exchange(), height=5, width=10)
       calculate.grid(column=0, row=5)
       

              
gui.mainloop()
