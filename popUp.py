
import tkinter
from tkinter import *
from tkinter import messagebox
from findMatches import score_calc, reset

from Score import Score


#root=Tk()
#root.title("calculator")

def sent():
    global e
    from Score import Score
    from constants import getLevel
    from findMatches import time_taken
    name = e.get()
    score1 = Score(name,time_taken(),getLevel())
    score1.storeScore()
    messagebox.showinfo("Message", "Your result has been saved!")
    top.destroy()
    reset()
    
    
    


def yes(yesB, noB, l):
    global e
    yesB.destroy()
    noB.destroy()
    noB.destroy()

    e=Entry(top,bg="#102027",fg="white")
    e.grid(row=5,column=1,columnspan=2,padx=10,pady=5)
    l1=Label(top,text="Enter you name",bg="#102027",fg="white")
    l1.grid(row=4,column=1,columnspan=2,padx=10,pady=5)
    submit=Button(top,text="submit",bg="#102027",fg="white",font=("Arial",20),command=sent)
    submit.grid(row=6,column=1,columnspan=2,padx=10,pady=5)


def no() :
    top.destroy()
    #root.destroy()


    

def pop():
    
    score= score_calc()
    global top
    global yes_button
    global no_button
    top =Toplevel()
    top.title("well done you win !!")
    top.geometry("300x350")
    top.config(background="#102027")
    l1=Label(top,text=f"Congratulations you got {score} ",font=("Arial",14),bg="#102027" ,fg="white")
    l1.grid(row=1,column=1,columnspan=2,padx=10,pady=5)
    label_cong=Label(top,text="Do you want to save this score",font=("Arial",14),bg="#102027",fg="white")
    label_cong.grid(row=2,column=1,columnspan=2,padx=10,pady=5)
    yes_button=Button(top,text="yes",bg="#102027",fg="white",command=lambda: yes(yes_button, no_button, label_cong),width=10,font=("Arial",10))
    yes_button.grid(row=3,column=1,padx=10,pady=5)
    no_button= Button(top, text="no",bg="#102027",fg="white", command=no,width=10,font=("Arial",10))
    no_button.grid(row=3, column=2,padx=10,pady=5)





# b1=Button(root,text="click",command=pop)
# b1.pack()


#mainloop()